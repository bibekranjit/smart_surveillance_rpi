from flask import Flask, jsonify, render_template, request
from flask_sock import Sock
from detection.ipwebcam import get_video_frame, get_audio_wav
from detection.object_detector import detect_objects_from_frame
from detection.audio_classifier import classify_audio
from utils.announcer import announce
from utils.logger import log_event
import cv2
import os
import threading
import time
import json
from config import IP_WEBCAM_HOST, IP_WEBCAM_PORT, EVENT_MESSAGES

app = Flask(__name__)
sock = Sock(app)
clients = []

running = True

def send_to_clients(data):
    for ws in clients:
        try:
            ws.send(json.dumps(data))
        except:
            clients.remove(ws)

@sock.route('/ws')
def websocket(ws):
    clients.append(ws)
    while True:
        try:
            _ = ws.receive()
        except:
            break

def continuous_detection_loop():
    print("🌀 Continuous detection loop started...")
    while running:
        print("🔁 Loop tick")
        frame = get_video_frame()
        if frame is not None:
            print("📸 Frame captured successfully.")
            visual_events = detect_objects_from_frame(frame)
            for event_key in visual_events:
                if event_key in EVENT_MESSAGES:
                    announce(EVENT_MESSAGES[event_key])
                    log_event(event_key)
                    send_to_clients({"type": "visual", "event": event_key})
        else:
            print("⛔ No frame captured. Skipping visual detection.")

        time.sleep(5)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", ip=IP_WEBCAM_HOST, port=IP_WEBCAM_PORT)

@app.route("/detect-all", methods=["GET"])
def detect_all():
    return jsonify({"message": "Detection is running in background."})

if __name__ == "__main__":
    detection_thread = threading.Thread(target=continuous_detection_loop, daemon=True)
    detection_thread.start()
    app.run(port=5000, debug=False, use_reloader=False)
