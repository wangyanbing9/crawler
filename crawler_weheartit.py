import time
import os
import re
import urllib
import requests
from bs4 import BeautifulSoup


class DownloadImg(object):
    """Download images"""

    SAVE_FOLDER = '\\download\\'

    def download(self):
        web_data = requests.get(URL)
        soup = BeautifulSoup(web_data.text, 'lxml')
        img_links = soup.select(
            '#main-container > div > div.grid-thumb.'
            'grid-responsive > div > div > div > a > img')
        pattern = re.compile('[0-9]+')
        for img_link in img_links[:10]:
            img_link = img_link.get('src')
            file_name = pattern.search(img_link).group(0)
            print(img_link)
            print(file_name)
            urllib.request.urlretrieve(
                img_link, os.getcwd() + self.SAVE_FOLDER +
                str(file_name) + '.jpg')
            time.sleep(1)
if __name__ == '__main__':
    URL = 'http://weheartit.com/inspirations/avrillavigne'
    download_img = DownloadImg()
    download_img.download()
