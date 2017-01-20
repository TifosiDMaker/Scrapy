# -*- coding: utf-8 -*-
import pymysql as mdb
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

conn = mdb.connect('localhost', 'root', 'root')
cursor = conn.cursor()

from_addr = '394939236@qq.com'
password = 'arrxhvxsrxejbjje'
to_addr = 'tifosi19921030@gmail.com'
smtp_server = 'smtp.qq.com'

m = 1
while m > 0:
    conn.select_db('aqi')
    TABLE_NAME = 'aqi'
    sql = """select aqi from aqi ORDER BY `aqi`.`id` desc"""
    cursor.execute(sql)
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

    goodmsg = MIMEText("""警报解除，赶紧出去野吧！当前的空气质量为%d。""", 'plain', 'utf-8' % d)
    badmsg = MIMEText('空气变坏了！！戴口罩啊！！当前的空气质量为%d。', 'plain', 'utf-8' % d)
    goodmsg['From'] = _format_addr('关心你的云老王 <%s>' % from_addr)
    badmsg['From'] = _format_addr('关心你的云老王 <%s>' % from_addr)
    goodmsg['To'] = _format_addr('被云老王关心的你 <%s>' % to_addr)
    badmsg['To'] = _format_addr('被云老王关心的你 <%s>' % to_addr)
    goodmsg['Subject'] = Header('空气不好，多喝热水啊~', 'utf-8').encode()
    badmsg['Subject'] = Header('空气不好，多喝热水啊~', 'utf-8').encode()

    if a > 100:
        if b < 100:
            if c < 100:
                if d < 100:
                    server = smtplib.SMTP_SSL(smtp_server, 465)
                    server.set_debuglevel(1)
                    server.login(from_addr, password)
                    server.sendmail(from_addr, [to_addr], goodmsg.as_string())
                    server.quit()
    else:
        if b > 100:
            if c > 100:
                if d > 100:
                    server = smtplib.SMTP_SSL(smtp_server, 465)
                    server.set_debuglevel(1)
                    server.login(from_addr, password)
                    server.sendmail(from_addr, [to_addr], badmsg.as_string())
                    server.quit()
    time.sleep(3600)