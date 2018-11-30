#!/usr/bin/env python
# coding=utf8
""" Crawl the url of MM image in db."""
import requests
from bs4 import BeautifulSoup
import pymongo


def get_collection():
    client = pymongo.MongoClient("localhost", 27017)
    db = client["mm_finder"]
    coll = db.pics
    coll.ensure_index('url', unique=True)
    return coll


def insert_pic(url, alt):
    try:
        collection.insert({"url": url, "has_downloaded": False, "alt": alt})
    except: pass


def parse_detail(url):
    print url
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content.decode("gbk"), "lxml")
    imgs = soup.find("div", {"class": "postContent"}).find_all("img")

    for img in imgs:
        print img
        try:
            insert_pic(img["src"], img["alt"])
        except: pass


def parse_whole(url):
    def get_nextpage(soup):
        lis = soup.find("div", {"id": "wp_page_numbers"}).find_all("li")
        for li in lis:
            if li.get_text() == u"下一页":
                return "http://www.meizitu.com/a/" + li.a["href"]
        return None

    def get_albums(soup):
        lis = soup.find_all("li", {"class": "wp-item"})
        albums = []
        for li in lis:
            albums.append(li.a["href"])
        return albums

    while url is not None:
        print("new_page-->", url)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode("gbk"), "lxml")
        albums = get_albums(soup)
        for album in albums:
            parse_detail(album)
        url = get_nextpage(soup)


def get_tags():
    resp = requests.get("http://www.meizitu.com/")
    soup = BeautifulSoup(resp.content.decode("gbk"), "lxml")
    items = soup.find("div", {"class": "tags"}).find_all("a")

    tags = []
    for item in items:
        tags.append(item["href"])
    return set(tags)

if __name__ == "__main__":
    collection = get_collection()
    for tag in get_tags():
        parse_whole(tag)
