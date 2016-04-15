from bs4 import BeautifulSoup


def get_page(path):
    try:
        web_data = open(path, 'r')
        soup = BeautifulSoup(web_data, 'lxml')  # instance of BeautifulSoup
        images = soup.select("body > div > div > div.col-md-9 > div > div > div > img ")
        titles = soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")
        prices = soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
        reviews = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
        stars = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")
    except IOError:
        print("Error: can\'t find file or read data")
    finally:
        # 检查文件中是否存在某个变量：locals()
        if 'web_data' in locals():
            web_data.close()
            print("file closed")

if __name__ == "__main__":
    local_path = './resources/index.html'
    get_page(local_path)
