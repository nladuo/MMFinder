import pymongo
import numpy as np


client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images

count = 0

with open("mm_index_input.txt", "w") as f:
    for image in images_coll.find():
        path = image["path"]
        vec = "|".join([str(i) for i in image["vec"]])

        print(count, path)
        f.write(f"{path}\t{vec}\n")
        count += 1
