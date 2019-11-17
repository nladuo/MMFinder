from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
import numpy as np
import os
import uuid


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
