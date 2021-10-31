#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd

url = 'http://localhost:9696/predict'

df = pd.read_csv("heart.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")


response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
