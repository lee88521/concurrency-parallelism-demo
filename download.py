import json
import os
import requests

from itertools import chain
from pathlib import Path

from bs4 import BeautifulSoup


def get_links(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return [img.attrs.get('data-src') for img in
            soup.find_all('div', class_='img-wrap')
            if img.attrs.get('data-src') is not None]


def download_link(directory, link):
    img_name = '{}.jpg'.format(os.path.basename(link))
    download_path = directory / img_name
    r = requests.get(link)
    with download_path.open('wb') as fd:
            fd.write(r.content)


def setup_download_dir(directory):
    download_dir = Path(directory)
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
