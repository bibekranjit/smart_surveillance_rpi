import cv2
import requests
import numpy as np
from config import IP_WEBCAM_URL

def get_video_frame():
    cap = cv2.VideoCapture(f"{IP_WEBCAM_URL}/video")
    print(f"Connecting to {IP_WEBCAM_URL}/video")
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("last_frame.jpg", frame)
    cap.release()
    return frame if ret else None

def get_audio_wav(filename="audio.wav"):
    try:
        url = f"{IP_WEBCAM_URL}/audio.wav"
        r = requests.get(url, stream=True, timeout=10)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return filename
    except:
        return None