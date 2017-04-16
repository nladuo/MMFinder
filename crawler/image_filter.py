#!/usr/bin/env python
# coding=utf8
""" Download the mm with one face images."""
import requests
import pymongo
import os
from PIL import Image
from bson.objectid import ObjectId
import face_recognition
from multiprocessing import Pool, Manager


def get_collection():
    client = pymongo.MongoClient("localhost", 27017, connect=False)
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


def get_face_num(image_name):
    image_path = './mm_images/%s' % image_name
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image)
    if len(locations) == 1:  # save the face of mm
        top, right, bottom, left = locations[0]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        with open("./mm_images/face-%s" % image_name, "wb") as f:
            pil_image.save(f)
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

    if get_face_num(image_name) != 1:
        os.remove(image_path)
        print "removed:", image_name


def handle_pic(pic, lock):
    print pic["alt"], pic["url"]
    try:
        download_image(pic["_id"], pic["url"])
    except:
        pass
    with lock:
        update_pic(pic["_id"])

if __name__ == "__main__":
    collection = get_collection()
    pics = collection.find({
        'has_downloaded': False
    })

    pool = Pool(10)
    lock = Manager().Lock()

    for pic in pics:
        pool.apply_async(handle_pic, args=(pic, lock))

    pool.close()
    pool.join()

