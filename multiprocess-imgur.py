__author__ = 'midhunc'
from functools import partial
from multiprocessing.pool import Pool
from download import setup_download_dir, get_links, download_link
from time import time
import os

def main():
   ts = time()
   client_id = os.getenv('IMGUR_CLIENT_ID')
   if not client_id:
       raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
   download_dir = setup_download_dir()
   links = [l for l in get_links(client_id) if l.endswith('.jpg')]
   download = partial(download_link, download_dir)
   p = Pool(8)
   '''with Pool(8) as p:'''
   p.map(download, links)
   print('Took {}s'.format(time() - ts))

if __name__ == '__main__':
    main()