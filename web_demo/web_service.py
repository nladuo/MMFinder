from vgg_model import get_feature_extractor
from web_utils import preprocess_image
import face_recognition
from PIL import Image


IMAGES_PATH = "../mm_images"
vgg_feature_extractor = get_feature_extractor()
TMP_FACE_PATH = './dist/tmp-face.png'


def get_face_and_save(path):
    image = face_recognition.load_image_file(path)
    locations = face_recognition.face_locations(image)
    if len(locations) == 1:  # save the face of mm
        top, right, bottom, left = locations[0]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        with open(TMP_FACE_PATH, "wb") as f:
            pil_image.save(f)
    return len(locations)


def get_face_representation():
    img = preprocess_image(TMP_FACE_PATH)
    features = vgg_feature_extractor.predict(img)
    vec = features[0].tolist()
    return vec


def call_SPTAG_search(vec):
    pass

