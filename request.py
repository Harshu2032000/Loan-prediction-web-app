# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:17:29 2021

@author: Harshu
"""

import requests

url = 'http://localhost:5000/results'
r = requests.post(url)

print(r.json())
#json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400