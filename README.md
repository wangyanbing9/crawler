# crawler
# install lxml:
#     1.Download from: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
#     2.'pip3 install wheel' in command line
#     3.'pip3 install xxx.whl' in the right directory
# install BeautifulSoup4:
#     1. 'pip3 install beautifulwoup4'
# install Requests
#     1. 'pip3 install requests'

# requests，用这个库能很方便的下载网页，不用标准库里面各种urllib；BeautifulSoup用来解析网页，不然自己用正则的话很烦。
# requests使用，1直接使用库内提供的get、post等函数，在比简单的情况下使用，2利用session，session能保存cookiees信息，方便的自定义request header，可以进行登陆操作。
# BeautifulSoup使用，先将requests得到的html生成BeautifulSoup对象，然后进行解析，可以用select进行css选择器操作，然后用get、getText等获取信息。