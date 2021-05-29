# -*- coding: utf-8 -*-
# @Time    : 5/29/2021 2:13 PM
# @Author  : Chen0495
# @Email   : 1346565673@qq.com|chenweiin612@gmail.com
# @File    : main.py
# @Software: PyCharm

import requests as rq
from bs4 import BeautifulSoup as BS
import numpy as np
import pandas as pd

rq.adapters.DEFAULT_RETRIES = 5
s = rq.session()
s.keep_alive = False # 关闭多余连接

header = { # 请更改cookie
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4501.0 Safari/537.36 Edg/92.0.891.1',
    'cookie' : 'wengine_vpn_ticketwebvpn_jsu_edu_cn=ddf59d5e95556bfc; show_vpn=1; refresh=1'
}

# 请更改url
r = rq.get('https://webvpn.jsu.edu.cn/https/77726476706e69737468656265737421fae05988693a7b45300d8db9d6562d/jsxsd/kscj/cjcx_list', headers = header, verify=False)

soup = BS(r.text,'html.parser')

head = []
for th in soup.find_all("th"):
    head.append(th.text)
while '' in head:
    head.remove('')
head.remove('序号')
context = np.array(head)


x = []
flag = 0
for td in soup.find_all("td"):
    if flag!=0 and flag%11!=1:
        x.append(td.text)
    if flag%11==0 and flag!=0:
        context = np.row_stack((context,np.array(x)))
        x.clear()
    flag+=1

context = np.delete(context,0,axis=0)
data = pd.DataFrame(context,columns=head)
print(data)

# 生成文件,亲更改文件名
data.to_csv('./CWL_2018403667.csv',encoding='utf-8-sig')
