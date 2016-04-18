# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import codecs


def get_single_page_info(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select(
        'body > div.wrap.clearfix.con_bg'
        ' > div.con_l > div.pho_info > h4 > em')[0]
    address = soup.select(
        'body > div.wrap.clearfix.con_bg '
        '> div.con_l > div.pho_info > p > span.pr5')[0]
    price = soup.select('#pricePart > div.day_l > span')[0]
    house_img = soup.select('#curBigImage')[0]
    owner_img = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0]
    owner_gender = \
        '女性' if soup.select(
            '#floatRightBox > div.js_box.clearfix > div.member_pic > div'
        )[0].get('class') == ['member_ico1'] else '男性'
    # print(title, address, price, house_img, owner_img, owner_gender)
    info_dict = {
        '标题': title.get_text(),
        '地址': address.get_text().strip(),
        '日租价格': price.get_text(),
        '房屋图片': house_img.get('src'),
        '房东图片': owner_img.get('src'),
        '房东性别': owner_gender
    }
    return info_dict


def get_list_info(city='sz', pages=100):
    results = []
    detail_page_urls = []
    multi_pages = [
        'http://sz.xiaozhu.com/search-duanzufang-p{page}-0/'.format(page=i)
        for i in range(1, pages+1)]
    for single_pages in multi_pages:
        time.sleep(2)
        web_data = requests.get(single_pages)
        soup = BeautifulSoup(web_data.text, "lxml")
        for detail_page_url_tags in soup.select('#page_list > ul > li > a'):
            detail_page_urls.append(detail_page_url_tags.get('href'))
    for detail_page_url in detail_page_urls:
        results.append(get_single_page_info(detail_page_url))
        print(results)
    return results
if __name__ == '__main__':
    result = get_list_info(pages=1)
    f = codecs.open('xiaozhu.txt', 'w','utf-8')
    f.writelines(str(x) + '\n' for x in result)
    f.close()
