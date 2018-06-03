# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:35 2018

@author: lenovo
"""
#引用其它工具包import
#联网
import urllib.request as r

address="http://api.openweathermap.org/data/2.5/weather?q=meishan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)
#转化成字典模式
import json
data=json.loads(info)
print("欢迎使用全球天气APP")
city_pinyin=input("请输入城市拼音:")
print("1.查看当前城市天气,2.查看其它城市天气，3.保存当前城市")
menno=input("请输入菜单：")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=="3":
    print("3.保存当前城市")
temp=data["main"]["temp"]
temp_max=data["main"]["temp_max"]
pressure=data["main"]["pressure"]
description=data["weather"][0]["description"]
print("当前天气温度"+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description)























