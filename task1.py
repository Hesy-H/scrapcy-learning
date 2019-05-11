import requests
import re
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        res=requests.get(url)
        if res.status_code==200:
            return  res.text
        return  None
    except RequestException:
        return  None
def parse_one_html(html):
    regex='<em class="">(\d+)</em>.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)</p >.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>'
    pattern=re.compile(regex,re.S)
    items=re.findall(pattern,html)
    for item in items:
        content=""
        for every_list in item[2].split():
            content=content+"".join(every_list)
        content=re.sub('&nbsp;',' ',content)
        content=re.sub('<br>', '', content)
        print(item[0],item[1],content,item[3],item[4],item[5])
def main(url):
    html=get_one_page(url)
    parse_one_html(html)
    
main('https://movie.douban.com/top250')
