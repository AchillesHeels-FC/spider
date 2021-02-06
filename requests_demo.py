# coding=utf-8
import re
import logging
import requests
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth


class Config(object):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/52.0.2743.116 Safari/537.36'}
    proxies = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}


def build_prepared_req():
    url = 'http://httpbin.org/post'
    data = {'name': 'germey'}
    session = requests.Session()
    request_ob = requests.Request('POST', url, data=data, headers=Config.headers)
    prepped = session.prepare_request(request_ob)
    response = session.send(prepped)
    print(response.text)


def auto_auth():
    response = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
    # response = requests.get('http://localhost:5000', auth=('username', 'password'))
    print(response.status_code)


def get_html_context():
    # 这里我们加入了headers信息，其中包含了User - Agent字段信息，也就是浏览器标识信息。如果不加这个，知乎会禁止抓取。
    responses = requests.get(r"https://www.zhihu.com/explore", headers=Config.headers)
    # print(responses.encoding, responses.apparent_encoding
    # 如果你在正则表达式里面使用了括号，那么匹配的结果（返回给你的结果）是括号里面的内容，并且是一个分组(group)
    pattern = re.compile('Explore.*?Card-.*?Title.*?data-za-detail-view-id.*?>(.*?)</a>', re.S)
    # context = re.findall(pattern, responses.text)
    context = pattern.findall(responses.text)
    print(context)


def get_bin_context():
    responses = requests.get(r"https://github.com/favicon.ico", headers=Config.headers)
    # 音频和视频文件也可以用这种方法获取
    with open('../playground/favicon.ico', 'wb') as f:
        f.write(responses.content)


def get_cookie():
    responses = requests.get("https://www.baidu.com", headers=Config.headers)
    # print(responses.cookies)
    for key, value in responses.cookies.items():
        print(key + '=' + value)


def remain_lohin_status():
    headers = {'Cookies': '_zap=1893e70e-3cd9-4773-92ee-2db8e922669a; '
                          '_xsrf=50d29d42-fd28-4aa3-bdea-80558df5a347; '
                          'd_c0="AGDiV0JElRCPTkyjkweKv1QSiGMVDa1gsS8=|1577675021"; '
                          'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1577675023;'
                          ' Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1577696074; '
                          'KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1577704020|1577704020',
               'Host': 'www.zhihu.com',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    responses = requests.get("https://www.zhihu.com", headers=headers)
    print(responses.text)


def session():
    # 用Session，可以做到模拟同一个会话而不用担心Cookies的问题。它通常用于模拟登录成功之后再进行下一步的操作。Session在平常用得非常广泛，可以用于模拟在一个浏览器中打开同一站点的不同页面
    session = requests.session()
    session.get('http://httpbin.org/cookies/set/number/123456789')
    responses = session.get('http://httpbin.org/cookies')
    print(responses.text)


def ssl_check():
    # urllib3.disable_warnings()
    logging.captureWarnings(True)
    response = requests.get('https://www.12306.cn', verify=False)
    # 当然我们也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
    # response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
    print(response.status_code)


def main():
    get_html_context()
    # get_bin_context()
    # get_cookie()
    # remain_lohin_status()
    # session()
    # ssl_check()


if __name__ == '__main__':
    main()
