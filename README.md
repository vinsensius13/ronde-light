# Ronde-Keras API

A lightweight FastAPI-based image classification API for predicting cultural landmarks using a pre-trained Keras `.h5` model based on MobileNetV2. Built for fast inference and easy integration with mobile or web frontends.

---

## 🚀 Project Overview

This API takes an image input (JPG/PNG), preprocesses it, and returns the predicted label with confidence score based on a deep learning model trained for landmark recognition. The model identifies various historical and cultural landmarks, specifically tailored for Pulau Penyengat.

---

## 🎓 Technologies Used

* **FastAPI**: A modern, high-performance web framework for building APIs with Python 3.6+.
* **TensorFlow**: Used to load and run the pre-trained `.h5` Keras model (MobileNetV2).
* **Pillow (PIL)**: Image processing and resizing.
* **NumPy**: Efficient numerical operations on image arrays.
* **Uvicorn**: ASGI server to run the FastAPI app.
* **CORS Middleware**: Handles cross-origin resource sharing for client-server communication.

---

## 🔧 Project Structure

```
ronde-keras/
├── models/
│   ├── bocchichan_model_inference.h5
│   └── labelsbocchi.json
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .venv/ (optional)
```

---

## 🔄 How It Works

### 1. Load Model & Labels

```python
model = tf.keras.models.load_model("models/bocchichan_model_inference.h5")
with open("models/labelsbocchi.json", "r") as f:
    labels = json.load(f)
```

### 2. Preprocess Uploaded Image

```python
def preprocess_image(image_file):
    img = Image.open(image_file).resize((224, 224)).convert("RGB")
    img_array = np.asarray(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)
```

### 3. Predict Endpoint

```python
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
        "threshold_check": "✅ Yeay beneran sukses!" if confidence >= 60 else "❓ Nggak yakin, Baka! Coba ambil foto lagi!"
    }
```

---

## 🚫 CORS Middleware (Security)

Allow all origins, methods, and headers to enable integration with any frontend (mobile/web).

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🔍 OpenAPI & Swagger UI

Access your API documentation at:

* Swagger UI: [`/docs`](https://ronde-light.onrender.com/docs)
* OpenAPI JSON: [`/openapi.json`](https://ronde-light.onrender.com/openapi.json)

---

## 🚧 Deployment (Render)

API is deployed on [Render](https://render.com) using the Docker method for easy scalability and fast performance.

---

## ✅ Example API Call (cURL)

```bash
curl -X 'POST' \
  'https://ronde-light.onrender.com/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@IMG_1228.JPG;type=image/jpeg'
```

### Example Response

```json
{
  "label": "Makam Engku Putri",
  "label_id": "2",
  "confidence": 83.96,
  "threshold_check": "✅ Yeay beneran sukses!"
}
```

---

## 🧭 Installation & Local Running

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/ronde-keras.git
cd ronde-keras
```

### 2. Setup virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API locally

```bash
uvicorn app:app --reload
```

Visit [`http://localhost:8000/docs`](http://localhost:8000/docs) for Swagger UI.

---

## 📄 Requirements

```
fastapi
uvicorn
tensorflow
pillow
python-multipart
```

---

## 🛠️ Future Improvements

* Add support for TensorFlow Lite (.tflite) inference
* Integrate token-based authentication
* Limit CORS to trusted domains
* Add exception handling for file input errors
* Add confidence-based fallback suggestions

---

## 👋 Contributing

Feel free to fork and PR your changes. Contributions for feature requests, bug fixes, and optimizations are welcome!

---

## 🌟 Acknowledgement

Model by: vinsensius13 & Nuswapada team

---


