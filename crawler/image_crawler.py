""" Crawl the url of MM image in db."""
import requests
from bs4 import BeautifulSoup
import pymongo


def download_html(d_url):
    while True:
        try:
            resp = requests.get(d_url, timeout=2)
            return resp.content.decode("utf8")
        except KeyboardInterrupt:
            raise
        except:
            pass


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
    html = download_html(url)
    soup = BeautifulSoup(html, "lxml")
    a = soup.find("article", {"class": "clearfix"}).find("figure").find("a")
    next_url = a.attrs["href"]
    src = a.find("img").attrs["src"]
    alt = a.find("img").attrs["alt"]
    print(alt, src)
    insert_pic(src, alt)
    return next_url


def parse_all_imgs(url):
    init_url = url
    count = 0
    while True:
        next_url = parse_detail(url)
        if init_url not in next_url:
            break
        url = next_url
        count += 1
        if count >= 8:  # 防止审美疲劳,一组图最多8张
            break


def parse_list(url):
    html = download_html(url)
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("article", {"class": "placeholder"})

    for item in items:
        a = item.find("figure").find("a")
        href = a.attrs["href"]
        print(href)
        parse_all_imgs(href)

if __name__ == "__main__":
    collection = get_collection()

    for i in range(1, 204):
        print("crawling page {page}..".format(page=i))
        url = "https://m.mzitu.com/page/{page}/".format(page=i)
        parse_list(url)
