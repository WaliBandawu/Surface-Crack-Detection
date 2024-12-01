# Surface-Crack-Detection

##Overview
This project is a Surface Crack Detection Web Application built using Flask. It leverages a pre-trained deep learning model (dima806/surface_crack_image_detection) from the Hugging Face Transformers library for image classification. Users can upload images to detect surface cracks, and the app provides predictions with annotated images.

##Features
Image Classification: Classifies images to detect surface cracks with confidence scores.
Image Annotation: Annotates uploaded images with the top prediction label and confidence.
Web Interface: Intuitive HTML-based user interface for uploading images and viewing results.
Static Image Storage: Uploaded and annotated images are stored in dedicated folders.
Prerequisites
Python: Install Python 3.8 or higher.
Libraries:
Flask
Transformers
Pillow
Folder Setup:
static/uploads: To store uploaded images.
static/annotated: To store annotated images.
Installation
Clone the repository:

bash

git clone https://github.com/your-repo/surface-crack-detection.git
cd surface-crack-detection
Install dependencies:

bash

pip install -r requirements.txt
Create necessary folders:

bash

mkdir -p static/uploads static/annotated
How to Run
Start the Flask application:

bash

python app.py
Access the app: Open your browser and navigate to http://127.0.0.1:5000.

## File Structure
app.py: Main Flask application code.
templates/index.html: Frontend HTML template for the web interface.
static/uploads/: Stores uploaded images.
static/annotated/: Stores annotated images.
Usage
Navigate to the homepage (/).
Upload an image using the "Choose File" button.
Click the "Upload and Predict" button.
View predictions and annotated images on the same page.
Model Information
Model: dima806/surface_crack_image_detection
Pipeline: Hugging Face's image-classification pipeline.
API Endpoints
/
Method: GET
Description: Renders the home page.
/predict
Method: POST
Description: Accepts an uploaded image, runs predictions, and returns results along with the annotated image URL.
/<path:filename>
Method: GET
Description: Serves static files (uploaded or annotated images).
Example Output
Predictions: Displays labels and confidence scores for cracks.
Annotated Image: Highlights predictions directly on the uploaded image.
Future Enhancements
Add more model options for image classification.
Implement batch processing for multiple images.
Enhance UI for better user experience.
License
This project is licensed under the MIT License.

Enjoy using the Surface Crack Detection App! 😊






