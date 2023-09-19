# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:23:49 2022

@author: Lenovo
"""
import os
import requests
from bs4 import BeautifulSoup
import time 
# 用户请求头
headers={
    'User-Agent': ........
    }
# 用session()函数简化下面的函数
session = requests.Session()
session.headers.update(headers)
# 将请求的页面内的标题打印出来
def mulu(wang):
    suozai = session.get(wang)
    suozai.encoding = 'utf-8'
    soup = BeautifulSoup(suozai.text,'html.parser')
    mulu = soup.find('div',class_='list_notice list_search col2 clearfix',style='margin-top:10px;')
    yuansu = mulu.find_all('h3')
    o = 1
    for i in yuansu:
        i = i.text
        print(str(o)+i)
        o = o+1

def xunzhao(wang1,wang2):
   zhu = session.get(wang1)
   soup = BeautifulSoup(zhu.text,'html.parser')
   half_fu = soup.find('div',class_='list_notice list_search col2 clearfix',style='margin-top:10px;')
   #print(wang1,wang2)

   linka = half_fu.select(wang2)
   
   for i in linka:
      linkb = i['href']
      #print(linkb)
      #print('http://www.xdkj.tyut.edu.cn'+linkb[2:])
      shuliang = 0
      for i in linkb:
        shuliang=shuliang+1
        
      if yeshu==1:
        if shuliang>40:
          full_fu = session.get(linkb)
          full_fu.encoding = 'utf-8'
          #print(full_fu)
          soup2 = BeautifulSoup(full_fu.text,'html.parser')
          #print(soup2)
          bittles = soup2.select('div .v_news_content')
          texts = soup2.select('div .vsbcontent_img')
          for bittle in bittles:
             print(bittle.text)
             for wen in texts:
                print(wen.text)
        else:
          full_fu = session.get('http://www.xdkj.tyut.edu.cn'+linkb[2:])
          full_fu.encoding = 'utf-8'
          #print(full_fu)
          soup2 = BeautifulSoup(full_fu.text,'html.parser')
          #print(soup2)
          bittles = soup2.select('div .news_hd')
          texts = soup2.select('div .v_news_content')
          for bittle in bittles:
             print(bittle.text)
             for wen in texts:
                print(wen.text)
      else:
        if shuliang>40:
          full_fu = session.get(linkb)
          full_fu.encoding = 'utf-8'
          #print(full_fu)
          soup2 = BeautifulSoup(full_fu.text,'html.parser')
          #print(soup2)
          bittles = soup2.select('div .v_news_content')
          texts = soup2.select('div .vsbcontent_img')
          for bittle in bittles:
             print(bittle.text)
             for wen in texts:
                print(wen.text)
        else:
          full_fu = session.get('http://www.xdkj.tyut.edu.cn'+linkb[5:])
          full_fu.encoding = 'utf-8'
          #print(full_fu)
          soup2 = BeautifulSoup(full_fu.text,'html.parser')
          #print(soup2)
          bittles = soup2.select('div .news_hd')
          texts = soup2.select('div .v_news_content')
          for bittle in bittles:
             print(bittle.text)
             for wen in texts:
                print(wen.text)

moshi = input('请输入你需要的文章的数量类型，如若单篇请输入1，如若多篇请输入2\n')        
moshi = int(moshi)
queren = 0
while queren==0:  
  yeshu = input('请输入需要第几页的文章\n')
  yeshu = int(yeshu)
  #总页数
  zhu = requests.get('http://www.xdkj.tyut.edu.cn/xwzx/tzgg.htm',headers=headers)
  soup = BeautifulSoup(zhu.text,'html.parser')
  zys=soup.find_all('span',class_='p_no')
  zys=zys[4]
  zys=zys.text
  zys=int(zys)
  #定义网站
  wang1 = 'http://www.xdkj.tyut.edu.cn/xwzx/tzgg/'+str(format(zys-yeshu+1))+'.htm'
  wang1_1 = 'http://www.xdkj.tyut.edu.cn/xwzx/tzgg.htm'
  if yeshu ==1:
      mulu(wang1_1)
  else:
      mulu(wang1)
  queren = input('您所需查找的文章是否在此页，如果在请输入1，如果不在请输入0\n')
  queren=int(queren)
if moshi == 1:  
  #yeshu = input('请输入需要第几页的文章\n')
  #yeshu = int(yeshu)
  pianfu = input('请输入需要第几篇文章\n')
  pianfu = int(pianfu)
  wang2_1='#line_u10_'+str(pianfu-1)
else:
  #yeshu = input('请输入需要第几页的文章\n')
  #yeshu = int(yeshu)
  pianfu1 = input('请输入需要文章的开始篇幅\n')
  pianfu1 = int(pianfu1)
  pianfu2 = input('请输入需要文章的结束篇幅\n')
  pianfu2 = int(pianfu2)
  wang2s=['#line_u10_{}'.format(num) for num in range(pianfu1-1,pianfu2)]
'''
#总页数
zhu = requests.get('http://www.xdkj.tyut.edu.cn/xwzx/tzgg.htm',headers=headers)
soup = BeautifulSoup(zhu.text,'html.parser')
zys=soup.find_all('span',class_='p_no')
zys=zys[4]
zys=zys.text
zys=int(zys)
#定义网站
wang1 = 'http://www.xdkj.tyut.edu.cn/xwzx/tzgg/'+str(format(zys-yeshu+1))+'.htm'
wang1_1 = 'http://www.xdkj.tyut.edu.cn/xwzx/tzgg.htm'
'''
#wang2s=['#line_u10_{}'.format(num) for num in range(pianfu1-1,pianfu2)]
#wang2_1='#line_u10_'+str(pianfu-1)
#print(wang1)
#print(wang2s)
input('press <Enter>')

if moshi == 1:
   if yeshu == 1: 
      xunzhao(wang1_1,wang2_1)
   else :
      xunzhao(wang1,wang2_1)
else:  
  #调用函数打印文章
   if yeshu == 1:
     for wang in wang2s: 
        xunzhao(wang1_1,wang)
        time.sleep(5)
   else :
      for wang in wang2s: 
        xunzhao(wang1,wang)
        time.sleep(5)
print('已经显示完全')
os.system('pause')
