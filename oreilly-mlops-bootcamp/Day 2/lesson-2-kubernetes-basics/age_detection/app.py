import os
import cv2
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load age detection model from OpenCV
age_model = cv2.dnn.readNetFromCaffe('model/deploy_age.prototxt', 'model/age_net.caffemodel')

@app.route('/detect_age', methods=['POST'])
def agedetection():
    try:
        # Receive image file
        image = request.files['image']
        # Read the image
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

        # Preprocess the image for age detection
        blob = cv2.dnn.blobFromImage(img, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

        # Set the input to the pre-trained age detection model
        age_model.setInput(blob)

        # Perform age detection
        age_preds = age_model.forward()
        i = age_preds[0].argmax()
        age_interval = ['(0, 3)', '(4, 7)', '(8, 14)', '(15, 24)',
                '(25, 37)', '(38, 47)', '(48, 59)', '(60, 100)'][i]

        return jsonify({'age_interval': age_interval})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
