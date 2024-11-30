from flask import Flask, request, jsonify, render_template, send_file
from transformers import pipeline
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)
pipe = pipeline("image-classification", model="dima806/surface_crack_image_detection")

UPLOAD_FOLDER = "static/uploads"
ANNOTATED_FOLDER = "static/annotated"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    try:
        # Open the uploaded image
        image = Image.open(io.BytesIO(image_file.read()))
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image.save(image_path)
    except Exception as e:
        return jsonify({"error": f"Invalid image file: {str(e)}"}), 400

    try:
        # Get predictions
        predictions = pipe(image)
        top_prediction = predictions[0]  # Assume the top prediction is the most relevant

        # Annotate the image with prediction label
        annotated_image = annotate_image(image, top_prediction)
        annotated_path = os.path.join(ANNOTATED_FOLDER, f"annotated_{image_file.filename}")
        annotated_image.save(annotated_path)
    except Exception as e:
        return jsonify({"error": f"Model prediction failed: {str(e)}"}), 500

    # Prepare the result
    result = {
        "predictions": [
            {"label": pred["label"], "confidence": round(pred["score"], 4)}
            for pred in predictions
        ],
        "image_url": f"/{annotated_path}",
    }
    return jsonify(result)

def annotate_image(image, prediction):
    """Annotate the image with the prediction label."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    label = f"{prediction['label']} ({round(prediction['score'] * 100, 2)}%)"

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), label, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Draw a black rectangle for the label background
    draw.rectangle([(0, 0), (text_width + 10, text_height + 10)], fill="black")

    # Draw the label text
    draw.text((5, 5), label, fill="white", font=font)
    return image


@app.route('/<path:filename>')
def serve_static_file(filename):
    """Serve static files (uploaded or annotated images)."""
    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
