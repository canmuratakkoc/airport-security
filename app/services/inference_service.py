import io
import base64
from io import BytesIO
from flask import current_app
from ultralytics import YOLO            # ya da torch.load / tf.keras.load_model
from PIL import Image, Image as PILImage
import numpy as np

_models = {}

def _get_model(key: str):
    if key not in _models:
        path = current_app.config[key]
        _models[key] = YOLO(path)
    return _models[key]

def _read_image(file_storage):
    img = Image.open(io.BytesIO(file_storage.read())).convert("RGB")
    return np.array(img)


def _read_image_bytes(data: bytes):
    img = Image.open(io.BytesIO(data)).convert("RGB")
    return np.array(img)

def predict_model_a(file_storage):
    model = _get_model("MODEL_A_PATH")
    img = _read_image(file_storage)
    results = model(img, conf=0.2)     # eşiği %20’ye düşürdük
    res = results[0]                   # tek sonuç
    # JSON verisi
    preds = res.to_df().to_dict(orient="records")
    # Annotated görüntü
    annotated = res.plot()             # numpy array
    buf = BytesIO()
    PILImage.fromarray(annotated).save(buf, format="JPEG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return {"predictions": preds, "annotated_image": b64}

def predict_model_b(file_storage):
    model = _get_model("MODEL_B_PATH")
    img = _read_image(file_storage)
    results = model(img, conf=0.2)
    res = results[0]
    preds = res.to_df().to_dict(orient="records")
    annotated = res.plot()
    buf = BytesIO()
    PILImage.fromarray(annotated).save(buf, format="JPEG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return {"predictions": preds, "annotated_image": b64}


def predict_model_b_bytes(data: bytes):
    model = _get_model("MODEL_B_PATH")
    img = _read_image_bytes(data)
    results = model(img, conf=0.2)
    res = results[0]
    preds = res.to_df().to_dict(orient="records")
    annotated = res.plot()
    buf = BytesIO()
    PILImage.fromarray(annotated).save(buf, format="JPEG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return {"predictions": preds, "annotated_image": b64}
