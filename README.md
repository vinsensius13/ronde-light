# 🌕 Ronde-TFLITE 🍡

FastAPI-based image classification API for detecting traditional Ronde icons and labeling them using a Keras `.h5` model.

---

## 🚀 Features

* 🌟 Classify image of cultural objects (like Ronde sets)
* 📁 Accepts `.jpg`, `.png` and other image formats via multipart upload
* 🧠 Uses TensorFlow (Keras `.h5`) model for inference
* 📦 Easy to deploy via Render, Docker, or locally
* 🔓 CORS enabled (accepts requests from anywhere)
* 🧪 Auto-generated interactive Swagger docs (`/docs`)

---

## 💠 Installation

```bash
# Clone this repo
git clone https://github.com/yourusername/ronde-tflite.git
cd ronde-tflite

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 Model Structure

* `models/ronde_anget_light.h5` → Pretrained Keras model for classification
* `models/labelsronde.json` → Label mapping, format:

```json
{
  "0": "ronde-bulat-polos",
  "1": "bukit-kursi-meriam"
  // ...
}
```

---

## 🚦 API Endpoint

### `POST /predict/`

Endpoint for predicting image label using uploaded image.

#### 🔧 Request

* **Content-Type:** `multipart/form-data`
* **Field:** `file` (required) – image file (e.g. `.jpg`, `.png`)

#### 📄 Example cURL

```bash
curl -X POST "https://ronde-light.onrender.com/predict/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@yourimage.jpg;type=image/jpeg"
```

#### ✅ Response

```json
{
  "label": "bukit-kursi-meriam",
  "label_id": "1",
  "confidence": 35.53,
  "threshold_check": "❓ Nggak yakin, Baka! Coba foto lagi!"
}
```

#### ❗ Threshold

* Confidence ≥ 60%: `"✅ Sukses Yakin"`
* Confidence < 60%: `"❓ Nggak yakin, Baka!"`

---

## 🐳 Docker (Optional)

Build & run the app using Docker.

```bash
docker build -t ronde-tflite .
docker run -p 8000:8000 ronde-tflite
```

---

## 🌍 Access API Docs

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## 🧬 Tech Stack

* Python 3.10+
* FastAPI
* TensorFlow (Keras)
* Pillow (image handling)
* Uvicorn

---

## 💡 Notes

* This project is a cultural object image classifier, tailored for Indonesian traditional food context.
* Model used is trained on custom dataset of various ronde components.

---

## 🧙 Author & Team

Made by **Vinsen**, **Aichan**, and **Team Nuswapada**
Style: FastAPI + Tsundere-powered feedback 😠
