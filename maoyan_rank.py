# coding=utf-8
import requests


class Config(object):
    url_pattern = r'http://maoyan.com/board/4'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/52.0.2743.116 Safari/537.36'}


def get_web_page():
    response = requests.get(Config.url_pattern, headers=Config.headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    response_text = get_web_page()
    print(response_text)


if __name__ == '__main__':
    main()
