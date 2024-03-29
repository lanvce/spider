import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return  None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime'
                       +'.*?>(.*?)</p>.*?score.*?integer">(.*?)</i>.*?>(.*?)</i>.*?</dd>',re.S)

    items=re.findall(pattern,html)
    print(items)
def main():
    url='https://maoyan.com/board/4?offset=0'
    html=get_one_page(url)
    parse_one_page(html)
    #print(html)

if __name__=='__main__':
    main()