import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

urls = ['https://book.douban.com/subject/6813370/',
        'https://book.douban.com/subject/1032672/',
        'https://book.douban.com/subject/1753077/',
        'https://book.douban.com/subject/1418180/',
        'https://book.douban.com/subject/3136271/',
        'https://book.douban.com/subject/1203293/',
        'https://book.douban.com/subject/24934182/']
words = []

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    tags = soup.select('a[class=" tag"]')
    with open('d:/test.txt','a') as w:
        for name in tags:
            words.append(name.get_text().lower())
            w.write(name.get_text().lower() + ',')
    time.sleep(3)
    print('wait...')

p = pd.Series(words)
freq = p.value_counts()

with open('d:/test.txt', 'a') as w:
    w.write('\n' + str(freq))

print(freq)