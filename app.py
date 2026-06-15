from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
import io
import base64

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

def detect_glasses(frame):
    """Server-side glasses detection using eye region analysis"""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)
    
    detections = []
    if results.detections:
        h, w = frame.shape[:2]
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y = int(bbox.xmin * w), int(bbox.ymin * h)
            bw, bh = int(bbox.width * w), int(bbox.height * h)
            
            # Extract eye region (upper 40% of face)
            eye_region = frame[y:y+int(bh*0.4), x:x+bw]
            gray = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)
            
            # Edge detection for glasses frames
            edges = cv2.Canny(gray, 50, 150)
            edge_density = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
            
            # Horizontal line detection (glasses frames)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=20, 
                                   minLineLength=bw*0.3, maxLineGap=10)
            has_glasses = edge_density > 0.05 and lines is not None and len(lines) > 2
            
            detections.append({
                'bbox': [x, y, bw, bh],
                'has_glasses': bool(has_glasses),
                'confidence': float(edge_density * 10)
            })
    
    return detections

@socketio.on('frame')
def handle_frame(data):
    """Receive frame from client, process, return results"""
    # Decode base64 image
    img_data = base64.b64decode(data.split(',')[1])
    img = Image.open(io.BytesIO(img_data))
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Detect glasses
    results = detect_glasses(frame)
    emit('detection_result', {'faces': results})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)