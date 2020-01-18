from .vgg_model import get_feature_extractor
from .web_utils import preprocess_image
import face_recognition
from PIL import Image
from elasticsearch import Elasticsearch
import numpy as np
import tensorflow as tf

graph = tf.Graph()
with graph.as_default():
    session = tf.Session()
    with session.as_default():
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
    with graph.as_default():
        with session.as_default():
            features = vgg_feature_extractor.predict(img)
    vec = features[0].tolist()
    return vec


def call_ES_search(vec):
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, doc['vec']) + 1.0",
                "params": {"query_vector": vec}
            }
        }
    }
    es = Elasticsearch()
    searched = es.search("mm_index", body={
        "size": 30,
        "query": script_query,
    }, timeout=None)

    results = []
    for hit in searched["hits"]["hits"]:
        print(hit["_id"], hit["_score"])
        results.append(hit['_id'])

    return results
