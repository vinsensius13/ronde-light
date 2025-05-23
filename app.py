from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import json

app = FastAPI()

# === Allow All CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Load Keras H5 Model ===
model = tf.keras.models.load_model("models/ronde_anget_light.h5")

# === Load Labels ===
with open("models/labelsronde.json", "r") as f:
    labels = json.load(f)
label_keys = list(labels.keys())

# === Image Preprocessing Function ===
def preprocess_image(image_file):
    img = Image.open(image_file).resize((224, 224)).convert("RGB")
    img_array = np.asarray(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)

# === Predict Endpoint ===
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img_array = preprocess_image(file.file)

    output = model.predict(img_array)
    pred_idx = int(np.argmax(output))
    confidence = float(np.max(output)) * 100
    label_id = label_keys[pred_idx]

    return {
        "label": labels[label_id],
        "label_id": label_id,
        "confidence": round(confidence, 2),
        "threshold_check": "✅ Sukses Yakin" if confidence >= 60 else "❓ Nggak yakin, Baka! Coba foto lagi!"
    }
