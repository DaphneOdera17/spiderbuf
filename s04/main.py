# coding=utf-8
import re

import requests
from lxml import etree

base_url = 'http://www.spiderbuf.cn/s04/?pageno=%d'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 取页数
html = requests.get(base_url % 1, headers=myheaders).text
root = etree.HTML(html)

lis = root.xpath('//ul[@class="pagination"]/li')
page_text = lis[0].xpath('string(.)')

# 利用正则表达式提取数字
length = re.findall('[\d]', page_text)
length = int(length[0])

for i in range(1, length + 1):
    url = base_url % i # 用 i 来替换 %d
    # 获取网页源码内容并且打印出来
    html = requests.get(url, headers=myheaders).text

    # 存为文件 02.html
    f = open('04_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()

    # 获取根节点
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('data04_%d.txt' %i, 'w', encoding='utf-8')

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