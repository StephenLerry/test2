# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:14:52 2018

@author: lenovo
"""

#字典


msp={"地址":"北京","收件人":"王","电话号码":"142555555"}
print(msp["地址"])
print(msp["收件人"])
print(msp["电话号码"])

a={"xingming":"刘先生","shenggao":"170cm"}
print(a["xingming"]+a["shenggao"])


gequ1={"geshou":"薛之谦",
      "gequ":["动物世界","演员","认真的雪"],
      "昵称":"小生",
      "认识过的女朋友":["21","22","25","23"]}
gequ=gequ1["gequ"]
print(gequ)
print(len(gequ))
print(max(gequ1["认识过的女朋友"]))



xinxi={"未来5天的天气":["大雨","阳","多云","阴","阴天"],
       "未来五天的温度":["30度","33度","27度","26度","27度"],
       "星期":['星期一','星期二','星期三','星期四','星期五']} 
print("最高温度"+max(xinxi["未来五天的温度"]))
tianqi=xinxi["未来5天的天气"]
xingqi=xinxi["星期"]
wdu=xinxi["未来五天的温度"]
print("今天是"+str(tianqi[0])+str(xingqi[0])+str(wdu[0]))
print(str(tianqi[1])+str(xingqi[1])+str(wdu[1]))
print(str(tianqi[2])+str(xingqi[2])+str(wdu[2]))
print(str(tianqi[3])+str(xingqi[3])+str(wdu[3]))
print(str(tianqi[4])+str(xingqi[4])+str(wdu[4]))

