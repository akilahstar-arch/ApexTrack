# ApexTrack

ApexTrack is a small, beginner-friendly GPS telemetry program written in **Python only**. It uses Python's built-in libraries, so there are no packages to install. Enter GPS readings to see speed, pace, distance, elevation change, and GPS accuracy.

> **Simple-version note:** A browser's `navigator.geolocation.watchPosition()` is a JavaScript API, not a Python API. To keep this project pure Python and easy to understand, this version asks you to enter each GPS reading. A future web version could use a small amount of JavaScript to read the browser's GPS.

## Requirements

- Python 3.8 or newer
- A terminal or command prompt
- GPS coordinates and readings to enter (for example, from a phone's location app)

No third-party packages are needed.

## Run ApexTrack

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python app.py
```

If your computer uses `python3`, run `python3 app.py` instead. Enter latitude, longitude, elevation, and accuracy for each reading. Enter `q` when asked for a new reading to finish the session.

## What the program calculates

- **Distance:** Haversine formula, in kilometres.
- **Speed:** distance since the previous reading divided by the time between readings.
- **Pace:** elapsed session time per kilometre.
- **Elevation:** current elevation, plus accumulated climb and descent.
- **Accuracy:** displays the accuracy radius supplied with each reading.

The readings are kept in memory while the program runs. The program does not save or upload your location.

## How the code is organized

- `app.py` contains the whole program.
- `haversine_km()` calculates distance between two points on Earth.
- `ask_number()` repeats a question if the input is not a number.
- `main()` asks for readings and prints telemetry.

## Roadmap

- Connect to a GPS receiver through a clearly documented Python interface.
- Save a session to a local CSV file.
- Add a simple route plot using an optional mapping library.
- Add distance split summaries and unit preferences.
- Add automated tests for distance and pace calculations.

The roadmap features would add optional components; the core beginner edition stays small and dependency-free.
