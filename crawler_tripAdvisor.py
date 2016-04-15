from bs4 import BeautifulSoup
import requests
import time
urls = ['https://www.tripadvisor.com.hk' \
        '/Attractions-g60763-Activities-oa{}' \
        '-New_York_City_New_York.html#ATTRACTION_LIST'.format(
         str(page)) for page in range(0, 990, 30) ]


def get_attractions(url, data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, "lxml")
    titles = soup.select('div.property_title > a[target="_blank]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select("div.p13n_reasoning_v2")
    time.sleep(2)
    if data is None:
        for title, img, cate in zip(titles, imgs, cates):
            data = {
                'title': title.get_text(),
                'img': img.get('src'),
                'cate': list(cate.stripped_strings),
            }
            print(data)
if __name__ == "__main__":
    for single_usr in urls:
        get_attractions(single_usr)