# coding=utf-8
from flask import Flask, send_from_directory
from PIL import Image
import face_recognition
import json
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


app = Flask(__name__, static_folder='www')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('./www/static', path)


@app.route('/mm_images/<path:path>')
def serve_mm_images(path):
    return send_from_directory('../crawler/mm_images', path)


@app.route('/api/get_face_url')
def get_face_url():
    first_image = ""
    for image_path in os.listdir("../crawler/mm_images"):
        if image_path != ".gitignore":
            first_image = image_path
            break

    if first_image == "":
        return json.dumps({"code": 1})

    image = face_recognition.load_image_file("../crawler/mm_images/%s" % first_image)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) != 1:
        return json.dumps({"code": 1})

    top, right, bottom, left = face_locations[0]
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    with open("../crawler/mm_images/face-%s" % first_image, "wb") as f:
        pil_image.save(f)

    return json.dumps({"code": 0, "path": first_image})

if __name__ == '__main__':
    app.run(port=3389, debug=True)
