# Hand Gesture Controlled Cursor
A real-time computer vision project that allows users to control the mouse cursor using hand gestures via a webcam. This system leverages OpenCV, MediaPipe, and automation libraries to create a touchless Human-Computer Interaction interface.


## Features
- Real-time hand tracking using webcam
- Finger detection and gesture recognition
- Cursor movement mapped to hand position
- Left click using gesture
- Right click / double click (optional gestures)
- Drag and drop functionality
- Smooth and responsive interaction

## Tech Stack
- Python
- OpenCV (cv2)
- MediaPipe
- NumPy
- PyAutoGUI
- pynput
- math, time

## Project Structure
```bash
gesturecontrol_for_mouse/
│
├── main.py                # Main application script
├── hand_tracking.py      # Hand detection module (MediaPipe logic)
├── mouse_control.py      # Gesture → mouse mapping logic
├── utils.py              # Helper functions
│
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/gesturecontrol_for_mouse.git
cd gesturecontrol_for_mouse
```
### 2. Create virtual environment
```bash
python3.10 -m venv gesture_env
source gesture_env/bin/activate
```
### 3. Install dependencies
``` bash
pip install -r requirements.txt
```

## Usage
Run the main script:
``` bash
python main.py
```
Ensure your webcam is connected and accessible.

## Gesture Controls
| Gesture               | Action                  |
| --------------------- | ----------------------- |
| Index finger up       | Move cursor             |
| Index + Middle finger | Click                   |
| Closed fist           | Drag                    |
| Two fingers pinch     | Scroll / special action |

## How It Works
#### 1. Hand Detection
- Uses MediaPipe to extract 21 hand landmarks
#### 2. Gesture Recognition
- Determines which fingers are up/down using landmark positions
#### 3. Cursor Mapping
- Maps hand coordinates to screen resolution
#### 4. Mouse Control
- Uses PyAutoGUI / pynput to simulate mouse actions

## Limitations
- Performance depends on lighting conditions
- Accuracy may drop with complex backgrounds
- Requires stable webcam input
- Slight latency in real-time tracking

## Applications
- Touchless interfaces
- Accessibility tools
- Smart environments
- AR/VR interaction systems
