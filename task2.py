import sys
import os
import urllib 		# 这个是python的内置模块  urllib3和urllib2侧重点不一样，需要另外下载
	# 导入包以后如果不清楚怎么用或者不清楚包的结构，可以使用help(module)查看帮助
from urllib import request,parse

'''
2.1 学习beautifulsoup
学习beautifulsoup，并使用beautifulsoup提取内容。
使用beautifulsoup提取丁香园论坛的回复内容。
丁香园直通点：http://www.dxy.cn/bbs/thread/626626#626626 。
参考资料：https://blog.csdn.net/wwq114/article/details/88085875

'''
import urllib.request
from bs4 import BeautifulSoup as bs
def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    url = 'http://www.dxy.cn/bbs/thread/626626'
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    html = bs(response, 'lxml')
    getItem(html)
def getItem(html):
    datas = [] # 用来存放获取的用户名和评论
    for data in html.find_all("tbody"):
        try:
            userid = data.find("div", class_="auth").get_text(strip=True)
            print(userid)
            content = data.find("td", class_="postbody").get_text(strip=True)
            print(content)
            datas.append((userid,content))
        except:
            pass
    print(datas)



if __name__ == '__main__':
    main()
