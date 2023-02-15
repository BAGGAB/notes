#!/usr/bin/env python3
import logging
import os
from functools import partial
from multiprocessing import Pool
from time import time

from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    ts = time()
    download_dir = setup_download_dir()
    links = get_links()
    download = partial(download_link, download_dir)
    with Pool(4) as p:
        p.map(download, links)
    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()
