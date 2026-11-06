# ApexTrack World Clock

ApexTrack is a beginner-friendly digital clock written in Python. It displays the current local time in Los Angeles, New York, London, Tokyo, Sydney, and UTC, updating every second. It uses only Python's standard library—there are no packages to install.

## Requirements

- Python 3.9 or newer
- A terminal or command prompt
- A time zone database provided by your operating system (usually already available on macOS and Linux)

Python includes the `zoneinfo` module for time zones. On some Windows installations, Python may not have access to time zone data; if that happens, use a Python installation with an IANA time zone database available.

## Run the clock

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python app.py
```

If your computer uses `python3`, run `python3 app.py` instead. The clock refreshes once per second. Press **Ctrl+C** to stop it.

## How it works

- `TIME_ZONES` is a list of city names and time zone names.
- `ZoneInfo` accounts for time zone rules, including daylight saving time.
- `datetime.now()` gets the current time in each selected zone.
- `strftime()` formats the time and date for display.
- `time.sleep(1)` waits one second between screen updates.

To add a city, add a `(city name, IANA time zone)` pair to `TIME_ZONES`. For example:

```python
("Paris", "Europe/Paris"),
```

## Project files

- `app.py` contains the complete clock program.
- `requirements.txt` notes that the project uses only Python's standard library.

## Future ideas

- Let the user choose which cities to show.
- Add 24-hour time format.
- Add alarms for selected time zones.
- Build a graphical interface using an optional Python library.
