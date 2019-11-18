from flask import Flask, send_from_directory, request
import json
from backend.web_utils import allowed_file, save_upload_file, re_arrange_images
from backend.web_service import get_face_and_save, get_face_representation, call_SPTAG_search, UPLOAD_DIR
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


@app.route('/api/get_upload_images/<path:path>')
def serve_upload_images(path):
    return send_from_directory('./dist/static/upload_images', path)


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
                face_count = get_face_and_save(filename)
                if face_count == 0:
                    os.remove(f"{UPLOAD_DIR}/{filename}")
                    return json.dumps({'success': False, 'msg': '未检测出图片中的人脸'})
                elif face_count > 1:
                    os.remove(f"{UPLOAD_DIR}/{filename}")
                    return json.dumps({'success': False, 'msg': '检测出图片不止一张人脸（必须保证上传图片只有一张人脸）'})

                return json.dumps({'success': True, 'filename': filename, 'msg': '成功'})
            else:
                return json.dumps({'success': False, 'msg': '文件类型错误，请上传png,jpg,jpeg格式的图片'})


@app.route('/api/search')
def api_search_image():
    filename = request.args.get("filename")
    face_img_path = f"{UPLOAD_DIR}/face-{filename}"
    if not os.path.exists(face_img_path):
        return json.dumps({
            "success": False,
            "msg": "请求图片不存在，参数错误"
        })

    vec = get_face_representation(filename)
    image_names = call_SPTAG_search(vec)

    return json.dumps({
        "success": True,
        "data": re_arrange_images(image_names)
    })


if __name__ == '__main__':
    app.run(port=3889, debug=True)

