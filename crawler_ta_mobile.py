from bs4 import BeautifulSoup
import requests
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
    '/48.0.2564.23 Mobile Safari/537.36'
}
url_ta = 'https://www.tripadvisor.com.hk/' \
      'Attractions-g60763-Activities-oa30-New_York_City_New_York.html'


def get_mobile_data(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
    time.sleep(2)
    for img in imgs:
        print(img.get('src'))
if __name__ == "__main__":
    get_mobile_data(url_ta)  # 手机端也无法爬取到图片地址了


