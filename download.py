__author__ = 'midhunc'
import json
import logging
import os
from pathlib import Path
from urllib2 import urlopen, Request

logger = logging.getLogger(__name__)

def get_links(client_id):
   headers = {'Authorization': 'Client-ID {}'.format(client_id)}
   req = Request('https://api.imgur.com/3/gallery/', headers=headers)
   response = urlopen(req)
   decoded = response.read()
   data = json.loads(decoded.decode('utf-8'))
   #print(data)
   response.close()
   return (map(lambda  item: item['link'], data['data']))

def download_link(directory, link):
   logger.info('Downloading %s', link)
   download_path = directory / os.path.basename(link)
   image = urlopen(link)
   with download_path.open('wb') as f:
       f.write(image.read())

def setup_download_dir():
   download_dir = Path('images')
   if not download_dir.exists():
       download_dir.mkdir()
   return download_dir

