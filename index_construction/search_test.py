from SPTAG_rpc_search_client import SPTAG_RpcSearchClient, DataBean
import pymongo
import os
import random
from vgg_model import get_feature_extractor, preprocess_image
import numpy as np

image_names = []
for i, path in enumerate(os.listdir("../mm_images")):
    if "jpg" in path:
        image_names.append(path)
    if i > 100:
        break

random.shuffle(image_names)
test_img = image_names[0]
test_face_path = f"../mm_images/faces/face-{test_img}"

search_client = SPTAG_RpcSearchClient("127.0.0.1", "8888")


client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images

vgg_feature_extractor = get_feature_extractor()


def get_face_representation(path):
    img = preprocess_image(path)
    features = vgg_feature_extractor.predict(img)
    vec = features[0].tolist()
    return vec


vec = np.array(get_face_representation(test_face_path), dtype=np.float32)
bean = DataBean(_id="", vec=vec)
os.system(f"imgcat {test_face_path}")
results = search_client.search([bean], 20)
for item in results[0]:
    k = [i for i in item.keys()][0]
    print(k, item[k])
    os.system(f"imgcat ../mm_images/faces/face-{k}")
