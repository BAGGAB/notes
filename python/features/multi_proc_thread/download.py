import json
import logging
import os
from pathlib import Path
from collections import OrderedDict
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}

def get_links():

    req = Request('https://pokeapi.co/api/v2/pokemon/',headers=headers, method='GET')
    with urlopen(req) as resp:
        # print(resp.read())
        data = json.loads(resp.read().decode('utf-8'))
    return [item['url'] for item in data['results']]

def download_link(directory: Path, link):
    download_path = Path('images/' + link.rsplit('/', 2)[1])
    req = Request(link,headers=headers, method='GET')
    with urlopen(req) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir