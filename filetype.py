#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:07:07 2020

@author: fenghuoxizhuhou
"""
import tkinter
import urllib3
import requests
#top = tkinter.Tk()
#top.mainloop()
input_data = 'site:bjzhuoda.com'
data = str('?q='+input_data)
https = urllib3.PoolManager()
url = "https://www.google.com%s" % data
result = https.request('GET',url)
print(result)