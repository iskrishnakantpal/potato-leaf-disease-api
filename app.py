from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model("potatoes.keras")

# You can modify this list based on your actual classes
class_names = ['Early Blight', 'Late Blight', 'Healthy']

def preprocess_image(img):
    img = img.resize((224, 224))  # Modify if your model uses different size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    processed_img = preprocess_image(img)
    predictions = model.predict(processed_img)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return jsonify({
        'prediction': predicted_class,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True)
