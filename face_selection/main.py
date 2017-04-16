# coding=utf-8
from flask import Flask, send_from_directory
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
        if image_path != ".gitignore" and \
                (not image_path.startswith("face-")):
            first_image = image_path
            break

    if first_image == "":
        return json.dumps({"code": 1})

    return json.dumps({"code": 0, "path": first_image})

if __name__ == '__main__':
    app.run(port=3389, debug=True)
