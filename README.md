# Study-Support-Smartphone-Alert-System

## Overview

This system supports the user in focusing on studying by detecting unnecessary smartphone use during study time.
The system uses a Raspberry Pi, USB camera, object detection model, sensors, LEDs, LCD, buzzer, Discord API, Google Calendar API, and Google Spreadsheet API.

---

## Main Functions

* Start and stop Study Mode using a push button
* Display messages on LCD
* Check study schedules using Google Calendar API
* Turn on the green LED while studying
* Measure study time
* Measure away time
* Measure smartphone usage time
* Measure brightness, temperature, and humidity
* Detect the user, hand, and smartphone using an object detection model
* Evaluate smartphone usage based on the distance between the hand and the smartphone
* Decide warning level based on smartphone usage time
* Send warning notifications to Discord
* Control red LED and piezo buzzer during warning
* Make a final study report
* Send the final report to Discord
* Display the final report on LCD
* Save the final report to Google Spreadsheet
* Visualize study data with graphs in Google Spreadsheet

---

## Python Code Architecture

```text
project/
│
├── main.py                  # Main control program
├── study_mode.py            # Study mode state and time management
├── button_control.py        # Push button control
│
├── detection.py             # Camera and object detection control
├── smartphone_usage.py      # Smartphone usage evaluation
├── sitting_detection.py     # Sitting / away evaluation
│
├── warning.py               # Warning level control
├── led_control.py           # Red and green LED control
├── buzzer_control.py        # Piezo buzzer control
│
├── lcd.py                   # LCD message control
├── LCD1602.py               # Low-level LCD control code
│
├── environment_sensor.py    # Brightness, temperature, and humidity
├── check_calendar.py        # Google Calendar API control
├── discord_send.py          # Discord notification control
│
├── final_report.py          # Final report creation
├── send_sheet.py            # Google Spreadsheet API control
├── sheet_visualization.py   # Graph visualization in Google Spreadsheet
│
├── model/
│   └── best.pt              # Trained object detection model
│
├── data/
│   └── study_log.csv        # Local study log
│
├── .env                     # API keys and private settings
├── .gitignore
└── README.md
```

---

## Module Roles

| File                     | Role                                                                 |
| ------------------------ | -------------------------------------------------------------------- |
| `main.py`                | Controls the whole system flow                                       |
| `study_mode.py`          | Manages study mode, study time, away time, and smartphone usage time |
| `button_control.py`      | Starts and stops Study Mode using the push button                    |
| `detection.py`           | Captures images and detects person, hand, and smartphone             |
| `smartphone_usage.py`    | Checks whether the smartphone is used based on object distance       |
| `sitting_detection.py`   | Checks whether the user is sitting or away                           |
| `warning.py`             | Decides Warning Level 1 and Warning Level 2                          |
| `led_control.py`         | Controls green LED and red LED                                       |
| `buzzer_control.py`      | Controls the piezo buzzer                                            |
| `lcd.py`                 | Displays system messages on LCD                                      |
| `environment_sensor.py`  | Measures brightness, temperature, and humidity                       |
| `check_calendar.py`      | Gets study schedules from Google Calendar                            |
| `discord_send.py`        | Sends warning messages and final reports to Discord                  |
| `final_report.py`        | Creates the final study report                                       |
| `send_sheet.py`          | Saves report data to Google Spreadsheet                              |
| `sheet_visualization.py` | Creates graphs in Google Spreadsheet                                 |

---

## Warning Flow

### Warning Level 1

Condition:

* Smartphone usage time is longer than the first threshold time
* Example: more than 1 minute

Actions:

* Send Discord notification one time
* Blink the red LED
* Count the warning

### Warning Level 2

Condition:

* Smartphone usage time is longer than the second threshold time
* Example: more than 2 minutes

Actions:

* Send Discord notification one time
* Turn on the piezo buzzer
* Continue buzzer warning until the user stops using the smartphone
* Count the warning

---

## Final Report

After Study Mode is stopped, the system creates a final report.

The final report includes:

* Study time
* Away time
* Smartphone usage time
* Brightness
* Temperature
* Humidity
* Number of warnings
* Evaluation of studying quality

The final report is sent to:

* LCD
* Discord
* Google Spreadsheet

---

## Development Schedule

### Zero Phase

* Develop the system architecture
* Decide the role of each Python file
* Decide GPIO pin assignment
* Create the circuit diagram
* Decide warning conditions
* Decide final report contents

### First Phase

* Implement the basic Python operation flow
* Implement push button control
* Implement Study Mode start and stop
* Implement LED, LCD, and buzzer control
* Implement study time, away time, and smartphone usage time structure
* Implement Discord notification
* Implement Google Calendar API
* Implement Google Spreadsheet API
* Test each hardware component separately
* Start collecting images for the detection model

### Second Phase

* Prepare and label the image dataset
* Train the object detection model
* Detect person, hand, and smartphone
* Implement the trained model into the system
* Implement sitting detection
* Implement smartphone usage detection
* Connect detection results with warning control
* Test Warning Level 1 and Warning Level 2

### Third Phase

* Test the whole system
* Adjust threshold values
* Adjust camera angle
* Test final report creation
* Test Discord and Google Spreadsheet connection
* Test graph visualization
* Prepare for demonstration

This README is a temporary draft and may be updated during development.
