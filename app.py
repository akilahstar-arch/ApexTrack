"""A beginner-friendly GPS telemetry tracker using only Python's standard library."""

import math
import time


def haversine_km(lat1, lon1, lat2, lon2):
    """Return the distance between two latitude/longitude points in km."""
    earth_radius_km = 6371.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    latitude_change = lat2 - lat1
    longitude_change = lon2 - lon1

    part = (
        math.sin(latitude_change / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(longitude_change / 2) ** 2
    )
    return earth_radius_km * 2 * math.atan2(math.sqrt(part), math.sqrt(1 - part))


def ask_number(prompt):
    """Ask until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, such as 37.7749.")


def main():
    print("\nApexTrack - Simple GPS Telemetry\n")
    print("Enter each GPS reading when you have one. Type q to finish.\n")

    previous_fix = None
    total_distance_km = 0.0
    total_gain_m = 0.0
    total_loss_m = 0.0
    previous_altitude_m = None
    start_time = time.time()

    while True:
        answer = input("Press Enter for a GPS reading, or type q to quit: ")
        if answer.lower() == "q":
            break

        latitude = ask_number("  Latitude (-90 to 90): ")
        longitude = ask_number("  Longitude (-180 to 180): ")
        altitude = ask_number("  Elevation in metres: ")
        accuracy = ask_number("  GPS accuracy radius in metres: ")

        if not -90 <= latitude <= 90:
            print("Latitude must be between -90 and 90. Try that reading again.\n")
            continue
        if not -180 <= longitude <= 180:
            print("Longitude must be between -180 and 180. Try that reading again.\n")
            continue
        if accuracy < 0:
            print("Accuracy cannot be negative. Try that reading again.\n")
            continue

        current_time = time.time()
        speed_kmh = 0.0

        if previous_fix is not None:
            distance_km = haversine_km(
                previous_fix["latitude"], previous_fix["longitude"],
                latitude, longitude,
            )
            seconds = current_time - previous_fix["time"]
            total_distance_km += distance_km
            if seconds > 0:
                speed_kmh = distance_km / (seconds / 3600)

            altitude_change = altitude - previous_altitude_m
            if altitude_change > 0:
                total_gain_m += altitude_change
            else:
                total_loss_m += abs(altitude_change)

        elapsed_seconds = current_time - start_time
        if total_distance_km > 0:
            pace_minutes_per_km = (elapsed_seconds / 60) / total_distance_km
            pace_whole_minutes = int(pace_minutes_per_km)
            pace_seconds = int((pace_minutes_per_km - pace_whole_minutes) * 60)
            pace = f"{pace_whole_minutes}:{pace_seconds:02d} min/km"
        else:
            pace = "--:-- min/km"

        print("\n  --- Live telemetry ---")
        print(f"  Speed:       {speed_kmh:.1f} km/h")
        print(f"  Pace:        {pace}")
        print(f"  Distance:    {total_distance_km:.3f} km")
        print(f"  Elevation:   {altitude:.1f} m")
        print(f"  Climb:       {total_gain_m:.1f} m")
        print(f"  Descent:     {total_loss_m:.1f} m")
        print(f"  GPS accuracy: within about {accuracy:.1f} m")
        print(f"  Coordinates: {latitude:.6f}, {longitude:.6f}\n")

        previous_fix = {
            "latitude": latitude,
            "longitude": longitude,
            "time": current_time,
        }
        previous_altitude_m = altitude

    print("\nSession finished.")
    print(f"Total distance: {total_distance_km:.3f} km")
    print(f"Climb: {total_gain_m:.1f} m | Descent: {total_loss_m:.1f} m")


if __name__ == "__main__":
    main()
