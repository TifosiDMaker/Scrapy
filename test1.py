import requests,re,time
s=requests.Session()
s.get('http://www.heibanke.com/accounts/login/')
data={'username':'test','password':'test123','csrfmiddlewaretoken':s.cookies.get('csrftoken')}
content=s.post('http://www.heibanke.com/accounts/login/',data=data).content.decode('utf-8')
rkey=r'title="password_pos">(\d+)'
rvalue=r'title="password_val">(\d+)'
d={}
pas=''
if content.find('注销')!=-1:
    while True:
        content=s.get('http://www.heibanke.com/lesson/crawler_ex03/pw_list/').content.decode('utf-8')
        key=re.findall(rkey,content)
        value=re.findall(rvalue,content)
        di=dict(zip(key,value))
        d.update(di)
        print(len(d),d)
        if len(d)==100:
            break
    for i in range(1,101):
       try:
           pas=''.join(d[str(i)])+pas
       except KeyError:
           continue
    pas=list(pas)
    pas.reverse()
    pas=''.join(pas)
    content=s.post('http://www.heibanke.com/lesson/crawler_ex03/',data={'username':'admin','password':pas,'csrfmiddlewaretoken':s.cookies.get('csrftoken')}).content.decode('utf-8')
    if content.find('恭喜')!=-1:
        print('密码是'+pas,'恭喜过关')
    else:
        print('密码错误请检查')