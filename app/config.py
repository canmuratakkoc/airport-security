import os

class Config:
    # … mevcut ayarlarınız …
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # ML modellerimizin yolları
    MODEL_A_PATH = os.path.join(BASE_DIR, os.pardir, "ml_models", "model_a.pt")
    MODEL_B_PATH = os.path.join(BASE_DIR, os.pardir, "ml_models", "model_b.pt")
