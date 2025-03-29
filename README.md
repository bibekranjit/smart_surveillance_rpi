# 🎯 Smart Surveillance System with IP Webcam + YOLOv8 (Mask Detection)

A real-time smart surveillance system that uses an **Android IP Webcam** feed to detect **face mask violations** (with/without/incorrect) using a trained **YOLOv8 model**. The system alerts, logs, and visualizes detection events in a Flask-based web dashboard.

---

## 📦 Features

- 🔁 Real-time object detection using YOLOv8 (`best.pt`)
- 📡 Works with IP Webcam (`IP Camera` Android app)
- 🧠 Face mask classes: `With_Mask`, `Without_Mask`, `Incorrect_Mask`
- 📢 Optional voice alerts using `espeak`
- 🧾 Logs all detection events to text file
- 🌐 Flask Web Dashboard with MJPEG video stream
- 🔌 WebSocket support to push real-time events

---

## 🖥 Folder Structure

ipwebcam_event_detector/
├── app.py                 # Flask server with continuous detection loop and video stream
├── config.py              # IP webcam configuration and event messages
├── detection/
│   ├── __init__.py
│   ├── ipwebcam.py        # Capture frame from IP webcam
│   ├── audio_classifier.py # Optional YAMNet-based audio classification
│   └── object_detector.py # YOLOv8 face mask detection logic
├── models/
│   └── best.pt            # Trained YOLOv8 model (e.g. face mask detection)
├── utils/
│   ├── announcer.py       # Optional audio alerts (e.g. via espeak)
│   └── logger.py          # Event logger for visual/audio alerts
├── templates/
    └── dashboard.html     # Flask HTML UI template



---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/bibekranjit/smart_surveillance_rpi.git
cd smart_surveillance_rpi

python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate (Linux/Mac)

pip install -r requirements.txt
```

### Update config.py
``` bash
IP_WEBCAM_HOST = "192.168.2.11"
IP_WEBCAM_PORT = 8080
```

### Run app.py

```bash
python app.py
```