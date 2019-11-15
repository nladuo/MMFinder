import pymongo
import face_recognition
from PIL import Image
import os

client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images


IMAGES_PATH = "../mm_images"


def get_face_and_save(path):
    image_path = f'{IMAGES_PATH}/{path}'
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image)
    if len(locations) == 1:  # save the face of mm
        top, right, bottom, left = locations[0]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        with open(f'{IMAGES_PATH}/faces/face-{path}', "wb") as f:
            pil_image.save(f)
    return len(locations)


def check_file_type(path):
    allow_types = [".png", ".jpg", ".jpeg"]
    for t in allow_types:
        if path.endswith(t):
            return True
    return False


for i, path in enumerate(os.listdir(IMAGES_PATH)):
    if not check_file_type(path):
        continue

    if images_coll.find({"path": path}).count() != 0:
        continue

    print(i, path)
    try:
        if get_face_and_save(path) != 1:
            continue
    except:
        continue
    images_coll.insert({
        "path": path
    })
