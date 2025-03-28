from pathlib import Path
from ultralytics import YOLO

model_path = "models/yolov8n.pt"
if not Path(model_path).exists():
    print("⚠️ Model not found, downloading...")
    model = YOLO("yolov8n.pt")  # This will auto-download to cache
else:
    print("🔥 Model found, loading...")
    model = YOLO(model_path)

def detect_objects(image_path):
    results = model(image_path)[0]
    classes = [model.names[int(cls)] for cls in results.boxes.cls]
    events = []
    if "person" in classes and "unknown" in classes:
        events.append("unknown_person")
    if "cat" in classes or "dog" in classes:
        events.append("animal_intrusion")
    if "backpack" in classes or "suitcase" in classes:
        events.append("suspicious_object")
    if classes.count("person") > 3:
        events.append("high_crowd")
    if "face" in classes and "mask" not in classes:
        events.append("no_mask")
    return events