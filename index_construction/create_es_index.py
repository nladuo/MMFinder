import pymongo
from elasticsearch import Elasticsearch


es = Elasticsearch()
index_mappings = {
  "mappings": {
      "properties": {
        "vec":    {
            "type": "dense_vector",
            "dims": 2622,
        },
      }
    },
}


if es.indices.exists(index='mm_index') is True:
	es.indices.delete(index="mm_index")
print("create mm_index")
es.indices.create(index='mm_index', body=index_mappings)


client = pymongo.MongoClient()
db = client.MMFinder
images_coll = db.images

count = 0

for image in images_coll.find():
    data = {
        "id": image["path"],
        "vec": image["vec"],
    }
    res = es.index(index="mm_index", id=image["path"], body=data)
    print(res)

    count += 1
