# coding=utf-8

import requests
from lxml import etree

url = 'http://www.spiderbuf.cn/s02/'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 获取网页源码内容并且打印出来
html = requests.get(url, headers=myheaders).text

# 存为文件 02.html
f = open('02.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 获取根节点
root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('data02.txt', 'w', encoding='utf-8')

for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        # 用 str 转换，防止是 None 而报错
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')

f.close()
# print(html)