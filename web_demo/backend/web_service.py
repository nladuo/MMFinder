from .vgg_model import get_feature_extractor
from .web_utils import preprocess_image
import face_recognition
from PIL import Image
from .SPTAG_rpc_search_client import SPTAG_RpcSearchClient, DataBean
import numpy as np

vgg_feature_extractor = get_feature_extractor()
vgg_feature_extractor.predict(np.zeros((1, 224, 224, 3)))

IMAGES_PATH = "../mm_images"
UPLOAD_DIR = './dist/static/upload_images'


def get_face_and_save(filename):
    img_path = f"{UPLOAD_DIR}/{filename}"
    image = face_recognition.load_image_file(img_path)
    locations = face_recognition.face_locations(image)
    if len(locations) == 1:  # save the face of mm
        top, right, bottom, left = locations[0]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        with open(f"{UPLOAD_DIR}/face-{filename}", "wb") as f:
            pil_image.save(f)
    return len(locations)


def get_face_representation(filename):
    face_img_path = f"{UPLOAD_DIR}/face-{filename}"
    img = preprocess_image(face_img_path)
    features = vgg_feature_extractor.predict(img)
    vec = features[0].tolist()
    return vec


def call_SPTAG_search(vec):
    vec = np.array(vec, dtype=np.float32)
    search_client = SPTAG_RpcSearchClient("127.0.0.1", "8888")
    bean = DataBean(_id="", vec=vec)
    results = search_client.search([bean], 30)
    result_images = []
    for item in results[0]:
        k = [i for i in item.keys()][0]
        print(k, item[k])
        result_images.append(k)
    return result_images
