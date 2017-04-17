# coding=utf-8
from flask import Flask, send_from_directory, request
import json
import os
import sys
import shutil

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
            # ensure the face image exist
            if os.path.exists("../crawler/mm_images/face-%s" % image_path):
                first_image = image_path
            break

    if first_image == "":
        return json.dumps({"code": 1})

    return json.dumps({"code": 0, "path": first_image})


@app.route('/api/handle_face')
def handle_face():
    path = request.args.get('path')
    opt = request.args.get('opt')
    if path is None or opt is None:
        return json.dumps({"code": 1})

    face_path = "../crawler/mm_images/face-" + path
    image_path = "../crawler/mm_images/" + path

    print os.path.exists(face_path), face_path

    if os.path.exists(face_path) and os.path.exists(image_path):
        if opt == "like":
            shutil.move(face_path, "./girls/likes/")
        elif opt == "dislike":
            shutil.move(face_path, "./girls/dislikes/")
        else:
            shutil.move(face_path, "./girls/ignores/")
        shutil.move(image_path, "../crawler/mm_images/history/")
        return json.dumps({"code": 0})
    else:
        return json.dumps({"code": 1})





if __name__ == '__main__':
    app.run(port=3389, debug=True)
