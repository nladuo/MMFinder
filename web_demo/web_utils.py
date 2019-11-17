from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
import numpy as np
import os
import uuid
from PIL import Image


def get_file_extension(filename):
    if "." not in filename:
        return ""

    return filename.rsplit('.', 1)[1].lower()


def allowed_file(filename):
    ALLOWED_EXTENSIONS = [
        "png",
        "jpg",
        "jpeg",
    ]
    return get_file_extension(filename) in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img


def save_upload_file(original_name, file):
    UPLOAD_DIR = "./dist/static/upload_images"

    _, ext = os.path.splitext(original_name)

    encrypted_name = str(uuid.uuid4()) + ext

    print(encrypted_name)

    file.save(os.path.join(UPLOAD_DIR, encrypted_name))
    return encrypted_name


def get_image_scale(image_name):
    path = f"../mm_images/{image_name}"
    size = Image.open(path).size
    return size[1] / size[0]


def re_arrange_images(image_names):
    """
        因为css是纵向排列的，但一般要横着看，所以这里把图片重新排序。
        (本来应该在前端写的，不过我不会写css，就代码改了)
    """
    image_scales = [get_image_scale(name) for name in image_names]
    columns = {}
    scales = []
    for i in range(5):
        columns[i] = []
        scales.append(0)

    for i, name in enumerate(image_names):
        which_col = scales.index(min(scales))
        image_scale = image_scales[i]

        columns[which_col].append(name)
        scales[which_col] += image_scale

    results = []
    for i in range(5):
        results += columns[i]

    return results
