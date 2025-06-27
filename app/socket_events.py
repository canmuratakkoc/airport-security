from flask_socketio import SocketIO, emit
import base64

from .services.inference_service import predict_model_b_bytes

ALERT_WEAPONS = {"gun", "knife", "pistol", "rifle"}

socketio = SocketIO(cors_allowed_origins="*")


@socketio.on('frame')
def handle_frame(data):
    try:
        if isinstance(data, str) and ',' in data:
            data = data.split(',', 1)[1]
        image_bytes = base64.b64decode(data)
        result = predict_model_b_bytes(image_bytes)

        # Alert logic: yüz + silah/bıçak
        has_face = False
        has_weapon = False
        for pred in result.get("predictions", []):
            name = str(pred.get("name", "")).lower()
            if name in {"face", "person", "head"}:
                has_face = True
            if name in ALERT_WEAPONS:
                has_weapon = True

        result["alert"] = has_face and has_weapon

        emit('result', result)
    except Exception as e:
        emit('error', {'message': str(e)})
