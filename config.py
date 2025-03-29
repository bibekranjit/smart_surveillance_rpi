# IP_WEBCAM_HOST = "10.111.65.218"  # replace with your IP

IP_WEBCAM_HOST = "192.168.2.11"  # replace with your IP
IP_WEBCAM_PORT = 8080
IP_WEBCAM_URL = f"http://{IP_WEBCAM_HOST}:{IP_WEBCAM_PORT}"

EVENT_MESSAGES = {
    "fire_alarm": "Fire alarm detected! Evacuate immediately.",
    "glass_breaking": "Possible intrusion detected! Alerting security.",
    "baby_crying": "Baby crying detected. Notifying guardian.",
    "doorbell": "Doorbell detected. Please check the entrance.",
    "gunshot": "Gunshot detected! Take cover and call emergency services.",
    "unknown_person": "Unrecognized person at the door. Proceed with caution.",
    "low_light": "Low visibility detected. Turning on night mode.",
    "no_mask": "Face mask not detected! Please wear a mask.",
    "high_crowd": "High crowd density detected. Maintain social distancing.",
    "suspicious_object": "Unattended object detected. Please inspect.",
    "animal_intrusion": "Animal intrusion detected! Stay alert.",
    "motion_detected": "Unauthorized movement detected! Security alert triggered.",
    "Incorrect_Mask": "Incorrect mask usage detected. Please adjust your mask.",
    "With_Mask": "Mask detected. Area safe.",
    "Without_Mask": "Face mask not detected! Please wear a mask."
}