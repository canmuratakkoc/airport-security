import os

class Config:
    # … mevcut ayarlarınız …
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # SQLAlchemy, JWT vb.
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///"+os.path.join(BASE_DIR,"app.db"))
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY","çok-gizli")

    # ML modellerimizin yolları
    MODEL_A_PATH = os.path.join(BASE_DIR, os.pardir, "ml_models", "model_a.pt")
    MODEL_B_PATH = os.path.join(BASE_DIR, os.pardir, "ml_models", "model_b.pt")
