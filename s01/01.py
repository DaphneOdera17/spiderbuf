# coding=utf-8

import requests
from lxml import etree

url = 'http://www.spiderbuf.cn/s01/'

# 获取网页源码内容并且打印出来
html = requests.get(url).text

# 存为文件 01.html
f = open('01.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 获取根节点
root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('data01.txt', 'w', encoding='utf-8')

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