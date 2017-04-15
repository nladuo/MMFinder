#!/usr/bin/env python
# coding=utf8
""" Download the mm with one face images."""
import requests
import pymongo
import os
from bson.objectid import ObjectId
import face_recognition


def get_collection():
    client = pymongo.MongoClient("localhost", 27017)
    db = client["mm_finder"]
    coll = db.pics
    coll.ensure_index('url', unique=True)
    return coll


def update_pic(_id):
    try:
        collection.update({'_id': ObjectId(_id)}, {
            '$set': {
                'has_downloaded': True
            }
        })
    except: pass


def get_face_num(path):
    image = face_recognition.load_image_file(path)
    locations = face_recognition.face_locations(image)
    return len(locations)


def download_image(_id, url):
    ext = os.path.splitext(url)[1]
    image_name = str(_id) + ext

    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Referer": "http://www.meizitu.com/a/xinggan.html",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
               }
    resp = requests.get(url, headers=headers)
    image_path = './mm_images/%s' % image_name
    with open(image_path, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    print "saved:", image_name

    if get_face_num(image_path) != 1:
        os.remove(image_path)
        print "removed:", image_name


if __name__ == "__main__":
    collection = get_collection()
    pics = collection.find({
        'has_downloaded': False
    })
    for pic in pics:
        print pic["alt"], pic["url"]
        try:
            download_image(pic["_id"], pic["url"])
        except:pass
        update_pic(pic["_id"])

