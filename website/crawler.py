#!/usr/bin/env python
""" Crawl the MM images, and Serve for desktop Client."""
import requests
from bs4 import BeautifulSoup


def parse_detail():
    resp = requests.get("http://www.meizitu.com/a/5517.html")
    soup = BeautifulSoup(resp.content, "lxml")
    imgs = soup.find("div", {"id": "picture"}).find_all("img")

    for img in imgs:
        print img


def parse_whole():
    resp = requests.get("http://www.meizitu.com/a/bijini.html")
    soup = BeautifulSoup(resp.content, "lxml")
    items = soup.find_all("li", {"class": "wp-item"})

    for item in items:
        print item


if __name__ == "__main__":
    parse_whole()


