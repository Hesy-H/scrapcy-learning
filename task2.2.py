'''
2.2学习xpath 
学习xpath，使用lxml+xpath提取内容。
使用xpath提取丁香园论坛的回复内容。
丁香园直通点：http://www.dxy.cn/bbs/thread/626626#626626 。
参考资料：https://blog.csdn.net/naonao77/article/details/88129994
'''
import requests
from lxml import etree

url = 'http://www.dxy.cn/bbs/thread/626626#626626'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) '
    }

def get_code(url):
    page = requests.get(url)    #页面获得
    if page.status_code == 200:
            return page.text   #源代码获得
    else:
        return None

def analysis(html):
    #下一步，运用Xpath来提取 回复内容
    # //td [@class='postbody']
    html = etree.HTML(get_code(url))
    #目前的问题：在哪里使用XPath？怎么使用？——对html使用xpath
    result = html.xpath('//td[@class="postbody"]/text()') #获得td节点下的文本
    for i in result:    #去杂
        print(i)
def main():
    html = get_code(url)
    analysis(html)

if __name__ == '__main__':    #执行此文件时，执行以下方法
    main()   
