from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from face_recognition_api.face_recognition.cli import test_image, scan_known_people, image_files_in_folder
from recognition_scripts.recognition_output_json import test_image_output_json
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/recognition', methods=['POST'])
def compare_known_to_unknowns():
    data = request.get_json()
    if not data or not data['known'] or not data['unknown']:
        abort(400)
    known_images_folder = os.path.join(os.getcwd(), data['known'])
    unknown_images_folder = os.path.join(os.getcwd(), data['unknown'])
    known_names, known_face_encodings = scan_known_people(known_images_folder)
    output = [test_image_output_json(image_file, known_names, known_face_encodings) for image_file in image_files_in_folder(unknown_images_folder)]

    return jsonify({'recognitionResults': output}), 201

if __name__ == "__main__":
    app.run()
