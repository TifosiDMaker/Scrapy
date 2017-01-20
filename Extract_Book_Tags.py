import requests
from lxml import html
import time
import urllib.request
from openpyxl import Workbook
import numpy as np


def decode(chinese):
    return urllib.request.quote(chinese)

with open('d:/hottags.txt', 'r') as f:
    hot_tags = f.read().split(',')

wb = Workbook()
ws = wb.active

urls = []
pages = [20, 40]
d = {}
j = []
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'book.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer': 'https://www.google.com/'
}
for elem in map(decode,hot_tags):
    for page in pages:
        urls.append('https://book.douban.com/tag/%s?start=%d&type=S' % (elem, page))
for url in urls:
    print('Processing: ' + url)
    r = requests.get(url,headers=headers)
    tree = html.fromstring(r.text)
    d.clear()
    name = ''.join(tree.xpath('/html/head/title/text()'))
    name = name[:-1]
    name = name[name.index(':') + 2:]
    for i in range(19):
        key = tree.xpath('//*[@id="subject_list"]/ul/li[' + str(i + 1) + ']/div[2]/h2/a/@title')
        value = tree.xpath('//*[@id="subject_list"]/ul/li[' + str(i + 1) + ']/div[2]/h2/a/@href')
        if value == '':
            break
        d[''.join(key)] = ''.join(value)
    #time.sleep(0.5)
    time.sleep(np.random.rand() * 5)
    for key in d:
        j.clear()
        r = requests.get(d[key],headers=headers)
        book = html.fromstring(r.text)
        j.append(key)
        for k in range(8):
            j.append(''.join(book.xpath('//*[@id="db-tags-section"]/div/span[' + str(k + 1) + ']/a/text()')))
        j.append(''.join(book.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')))
        ws.append(j)
        #time.sleep(0.5)
        time.sleep(np.random.rand() * 5)
    wb.save('d:/'+ name + '.xlsx')