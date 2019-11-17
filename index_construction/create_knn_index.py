from SPTAG_rpc_client import DataBean, SPTAG_RpcClient
import pymongo
import numpy as np


client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images

rpc_client = SPTAG_RpcClient("127.0.0.1", "8888")
INDEX_NAME = "mm_images_index"
# rpc_client.delete_index(INDEX_NAME)

count = 0
for image in images_coll.find():
    path = image["path"]
    vec = np.array(image["vec"], dtype=np.float32)

    bean = DataBean(path, vec)
    # beans.append(bean)
    print(count, path)
    rpc_client.add_data(INDEX_NAME, [bean])
    count += 1

print("all data index to", INDEX_NAME)
