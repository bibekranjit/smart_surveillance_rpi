import cv2
import math
from ultralytics import YOLO
from config import EVENT_MESSAGES

print("🔥 Model found, loading...")
model = YOLO("models/best.pt") 
classNames = ['Incorrect_Mask', 'With_Mask', 'Without_Mask']

box_colors = {
    "Incorrect_Mask": (0, 0, 255),
    "With_Mask": (0, 255, 0),
    "Without_Mask": (255, 0, 0)
}

def detect_objects_from_frame(frame):
    events = []
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            class_name = classNames[cls]

            print(f"🧠 Detected: {class_name} | Confidence: {conf}")
            events.append(class_name)

            # Optionally draw box
            color = box_colors[class_name]
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{class_name} ({conf})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return events