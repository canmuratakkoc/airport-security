from flask_socketio import SocketIO, emit
import base64

from .services.inference_service import predict_model_b_bytes

socketio = SocketIO(cors_allowed_origins="*")


@socketio.on('frame')
def handle_frame(data):
    try:
        if isinstance(data, str) and ',' in data:
            data = data.split(',', 1)[1]
        image_bytes = base64.b64decode(data)
        result = predict_model_b_bytes(image_bytes)
        emit('result', result)
    except Exception as e:
        emit('error', {'message': str(e)})
