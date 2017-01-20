# -*- coding: utf-8 -*-

import requests
from lxml import html
from datetime import datetime
import pymysql as mdb
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
	
def getutc():
    s = str(datetime.utcnow())
    s = s[:-3]
    s = s.split(' ')
    now = s[0] + 'T' + s[1] + 'Z'
    return now

conn = mdb.connect('localhost', 'root', 'root')
cursor = conn.cursor()

from_addr = '394939236@qq.com'
password = 'arrxhvxsrxejbjje'
to_addr = ['tifosi19921030@gmail.com','878561409@qq.com']
smtp_server = 'smtp.qq.com'

l = 1
ID = 30

while l > 0:
    conn = mdb.connect('localhost', 'root', 'root')
    cursor = conn.cursor()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'aqicn.org'
    }
    headers['Cookie'] = '__uvt=; __atuvc=1%7C2; waqi-w-station={%22url%22:%22http://aqicn.org/city/beijing/%22%2C%22name%22:%22Beijing%22%2C%22idx%22:1451%2C%22time%22:%22' + getutc() + '%22}; waqi-w-history=[{%22url%22:%22http://aqicn.org/city/beijing/%22%2C%22name%22:%22Beijing%22%2C%22idx%22:1451%2C%22time%22:%22' + getutc() + '%22}%2C{%22url%22:%22http://aqicn.org/city/beijing/us-embassy/%22%2C%22name%22:%22Beijing%20US%20Embassy%22%2C%22idx%22:3303%2C%22time%22:%22' + getutc() + '%22}]; __utmt=1; __utma=42180789.429949210.1484277193.1484543589.1484545824.5; __utmb=42180789.1.10.1484545824; __utmc=42180789; __utmz=42180789.1484534812.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); uvts=5WiImXGj4uGYbyOs'
    url = 'http://aqicn.org/city/beijing/'

    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.text)
    num = tree.xpath('//*[@id="aqiwgtvalue"]/text()')
    clock = tree.xpath('//*[@id="aqiwgtutime"]/text()')
    clock = str(clock[0])[-5:]
    conn.select_db('aqi')
    TABLE_NAME = 'aqi'
    sql = """INSERT INTO aqi
             VALUES ('%d', '%s', '%s', '%d')""" % (ID, datetime.now().strftime("%Y-%m-%d"), clock,int(num[0]))

    cursor.execute(sql)
    conn.commit()
	
    sqll = """select aqi from aqi ORDER BY `aqi`.`id` desc"""
    cursor.execute(sqll)
    results = cursor.fetchall()
    i = 0
    list = []
    for rows in results:
        if i > 3:
            break
        list.append(rows[0])
        i += 1
    conn.close()

    a = list[3]
    b = list[2]
    c = list[1]
    d = list[0]

    goodmsg = MIMEText("警报解除，赶紧出去野吧！当前的空气质量为%d。"% d, 'plain', 'utf-8')
    badmsg = MIMEText('空气变坏了！！戴口罩啊！！当前的空气质量为%d。'% d, 'plain', 'utf-8')
    goodmsg['From'] = _format_addr('关心你的云老王 <%s>' % from_addr)
    badmsg['From'] = _format_addr('关心你的云老王 <%s>' % from_addr)
    goodmsg['To'] = _format_addr('被云老王关心的你 <%s>' % to_addr)
    badmsg['To'] = _format_addr('被云老王关心的你 <%s>' % to_addr)
    goodmsg['Subject'] = Header('空气变好，high起来啊~', 'utf-8').encode()
    badmsg['Subject'] = Header('空气不好，多喝热水啊~', 'utf-8').encode()

    if a > 100:
        if b < 100:
            if c < 100:
                if d < 100:
                    server = smtplib.SMTP_SSL(smtp_server, 465)
                    server.set_debuglevel(1)
                    server.login(from_addr, password)
                    server.sendmail(from_addr, to_addr, goodmsg.as_string())
                    server.quit()
    else:
        if b > 100:
            if c > 100:
                if d > 100:
                    server = smtplib.SMTP_SSL(smtp_server, 465)
                    server.set_debuglevel(1)
                    server.login(from_addr, password)
                    server.sendmail(from_addr, to_addr, badmsg.as_string())
                    server.quit()
    ID += 1
    time.sleep(3600)
