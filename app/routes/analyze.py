from flask import Blueprint, request, jsonify
from app.services.inference_service import predict_model_a, predict_model_b

analyze_blueprint = Blueprint("analyze", __name__)

@analyze_blueprint.route("/model-a", methods=["POST"])
def analyze_a():
    if "file" not in request.files:
        return jsonify({"error": "file param is missing"}), 400
    file = request.files["file"]
    result = predict_model_a(file)
    return jsonify(result)

@analyze_blueprint.route("/model-b", methods=["POST"])
def analyze_b():
    if "file" not in request.files:
        return jsonify({"error": "file param is missing"}), 400
    file = request.files["file"]
    result = predict_model_b(file)
    return jsonify(result)
