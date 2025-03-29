import cv2
import requests
import numpy as np
from config import IP_WEBCAM_URL

# def get_video_frame():
#     try:
#         cap = cv2.VideoCapture(f"{IP_WEBCAM_URL}/video")
#         if not cap.isOpened():
#             print("⚠️ Unable to open webcam stream.")
#             return None
#         ret, frame = cap.read()
#         cap.release()
#         if ret:
#             print("📸 Frame captured successfully.")
#             return frame
#         else:
#             print("⚠️ Failed to read frame from stream.")
#             return None
#     except Exception as e:
#         print("❌ Exception in get_video_frame:", e)
#         return None

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
    

def get_video_frame():
    try:
        cap = cv2.VideoCapture(f"{IP_WEBCAM_URL}/video")
        if not cap.isOpened():
            print("⚠️ Unable to open webcam stream.")
            return None

        ret, frame = cap.read()
        cap.release()

        if ret:
            print("📸 Frame captured successfully.")
            return frame
        else:
            print("⚠️ Failed to read frame from stream.")
            return None
    except Exception as e:
        print("❌ Exception in get_video_frame:", e)
        return None