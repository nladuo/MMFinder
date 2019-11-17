from flask import Flask, send_from_directory, request
import json
from web_utils import allowed_file, save_upload_file
import random
import os


app = Flask(__name__, static_folder='dist')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('./dist/static', path)


@app.route('/api/get_images/<path:path>')
def serve_images(path):
    return send_from_directory('../mm_images', path)


@app.route('/api/upload_image', methods=["POST"])
def api_upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return json.dumps({'success': False, 'msg': '请求参数错误'})
        file = request.files['file']
        if file.filename == '':
            return json.dumps({'success': False, 'msg': '没选择文件'})
        else:
            if file and allowed_file(file.filename):
                origin_file_name = file.filename
                # 保存文件
                filename = save_upload_file(origin_file_name, file)
                return json.dumps({'success': True, 'filename': filename, 'msg': '成功'})
            else:
                return json.dumps({'success': False, 'msg': '文件类型错误，请上传png,jpg,jpeg格式的图片'})


@app.route('/api/search')
def api_search_image():
    image_names = []
    for i, path in enumerate(os.listdir("../mm_images")):
        if allowed_file(path):
            image_names.append(path)
        if i > 100:
            break
    random.shuffle(image_names)

    return json.dumps({
        "success": True,
        "data": image_names[:30]
    })


if __name__ == '__main__':
    app.run(port=3889, debug=True)

