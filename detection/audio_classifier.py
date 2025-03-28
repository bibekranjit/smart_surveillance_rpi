import tensorflow as tf
import numpy as np
import librosa

class_names = None
model = None

def load_yamnet_model():
    global model, class_names
    model = tf.keras.models.load_model("models/yamnet.h5")
    class_names = list(np.loadtxt("models/yamnet_class_map.csv", dtype=str, delimiter=","))

def classify_audio(file):
    global model, class_names
    if model is None:
        load_yamnet_model()
    waveform, sr = librosa.load(file, sr=16000)
    waveform = waveform[:model.input_shape[1]]  # crop to fixed length
    waveform = np.reshape(waveform, (1, -1))
    predictions = model.predict(waveform)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index].lower()
    keywords = {
        "fire alarm": "fire_alarm",
        "glass": "glass_breaking",
        "baby cry": "baby_crying",
        "doorbell": "doorbell",
        "gunshot": "gunshot"
    }
    for k in keywords:
        if k in predicted_class:
            return keywords[k]
    return None
