from flask import Flask, jsonify, render_template, Response, send_file
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
import requests

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

@app.route("/stream")
def stream():
    import cv2
    import numpy as np

    def generate():
        while True:
            try:
                # Get frame as JPEG from IP Webcam
                resp = requests.get(f"http://{IP_WEBCAM_HOST}:{IP_WEBCAM_PORT}/shot.jpg", timeout=2)
                if resp.status_code != 200:
                    continue

                # Decode JPEG to OpenCV image
                img_arr = np.frombuffer(resp.content, np.uint8)
                frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

                # Run detection and draw boxes
                detect_objects_from_frame(frame)

                # Encode back to JPEG for MJPEG stream
                _, jpeg = cv2.imencode('.jpg', frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
                time.sleep(0.1)
            except Exception as e:
                print(f"Stream error: {e}")
                continue

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/detect-all", methods=["GET"])
def detect_all():
    return jsonify({"message": "Detection is running in background."})

if __name__ == "__main__":
    detection_thread = threading.Thread(target=continuous_detection_loop, daemon=True)
    detection_thread.start()
    app.run(port=5000, debug=False, use_reloader=False)
