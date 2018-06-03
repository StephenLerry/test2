# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:47:34 2018

@author: lenovo
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(url).read().decode('utf-8','ignore')
print(info)

#josn(str)转换成dict

import json
w=json.loads(info)
w['weather'][0]['descripition']
w['main']['temp']
