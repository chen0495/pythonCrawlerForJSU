# pythonCrawlerForJSU
## 介绍
python简单爬虫,爬取吉首大学成绩单
学校的成绩单居然不支持导出,太坑了,算个绩点居然还要手打,我吐了,花2个多小时写了此python程序来生成可方便求和平均的Excel文件,帮助JSU学子脱离手算烦恼...

## 环境
- python 3.5即以上
- request、BeautifulSoup、numpy、pandas.

安装**BeautifulSoup**使用命令`pip install BeautifulSoup4`

## 配置及使用
1. 登陆学校成绩单查询网站,修改cookie.  
![修改cookie](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img/20210529162841.png)  

2. **按F12后按Ctrl+R刷新一下**,获取cookie的方法见下图:  
![获取cookie](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img/20210529163144.png)  

3. 修改爬虫url为自己的成绩单网址.  
![修改url](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img/20210529163330.png)  

4. 运行src/main.py文件即可在/result下得到csv文件.

## 结果展示
![结果](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img/20210529162057.png)
