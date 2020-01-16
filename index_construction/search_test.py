# from SPTAG_rpc_search_client import SPTAG_RpcSearchClient, DataBean
import pymongo
import os
import random
from vgg_model import get_feature_extractor, preprocess_image
import numpy as np
from elasticsearch import Elasticsearch


image_names = []
for i, path in enumerate(os.listdir("../mm_images")):
    if "jpg" in path:
        image_names.append(path)
    if i > 100:
        break

# random.shuffle(image_names)
test_img = image_names[49]
test_face_path = f"../mm_images/faces/face-{test_img}"


client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images

vgg_feature_extractor = get_feature_extractor()


def get_face_representation(path):
    img = preprocess_image(path)
    features = vgg_feature_extractor.predict(img)
    vec = features[0].tolist()
    return vec


query_vector = get_face_representation(test_face_path)

script_query = {
    "script_score": {
        "query": {"match_all": {}},
        "script": {
            "source": "cosineSimilarity(params.query_vector, doc['vec']) + 1.0",
            "params": {"query_vector": query_vector}
        }
    }
}
es = Elasticsearch()
searched = es.search("mm_index", body={
    "size": 20,
    "query": script_query,
}, timeout=None)

for hit in searched["hits"]["hits"]:
    print(hit["_id"], hit["_score"])
    os.system(f"imgcat ../mm_images/faces/face-{hit['_id']}")
