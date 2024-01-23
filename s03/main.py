# coding=utf-8

import requests
from lxml import etree

url = 'http://www.spiderbuf.cn/s03/'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 获取网页源码内容并且打印出来
html = requests.get(url, headers=myheaders).text

# 存为文件 02.html
f = open('03.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 获取根节点
root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('data03.txt', 'w', encoding='utf-8')

for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        # 不管 td 中包含了多少个标签，都可以把里面的文本内容取出来
        s = s + str(td.xpath('string(.)')) + '|'
        # 用 str 转换，防止是 None 而报错
        # s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')

f.close()
# print(html)