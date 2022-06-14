# -*- coding: utf-8 -*-
"""magicalbricks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DFfCPz26tHe8Vid50fqARdgDeWoPryqH
"""

!pip install bs4

import requests
#help(requests)
from bs4 import BeautifulSoup

url='https://www.magicbricks.com/flats-in-new-delhi-for-sale-pppfs?mbtracker=google_paid_brand_desk_other&ccode=brand_sem&gclid=CjwKCAiAsYyRBhACEiwAkJFKoqzxUkRIrBy5YATHNCyzavxaG4umZTpsPfDJ4V56rRRanq7-FUwPxxoCJ24QAvD_BwE'
for i in range(1,11):
  print(url+str(i))

import time
from IPython.display import clear_output

page_url='https://www.magicbricks.com/flats-in-new-delhi-for-sale-pppfs?mbtracker=google_paid_brand_desk_other&ccode=brand_sem&gclid=CjwKCAiAsYyRBhACEiwAkJFKoqzxUkRIrBy5YATHNCyzavxaG4umZTpsPfDJ4V56rRRanq7-FUwPxxoCJ24QAvD_BwE'
amo_unt=[]
tit_le=[]
cont_ag=[]
lab_el=[]
sq_ft=[]
ad_s=[]

for i in range(1,11):
  url=page_url+str(i)

    #we are pausing for 3secs
  time.sleep(3)
  response=requests.get(url)
  soup=BeautifulSoup(response.text,'html')
  amount=soup.find_all('div',attrs={'class':'mb-srp__card__price--amount'})
  for a in amount:
    amo_unt.append(a.text)
  title=soup.find_all('h2',attrs={'class':'mb-srp__card--title'})
  for t in title:
    tit_le.append(t.text)
  cont_agent=soup.find_all('div',attrs={'class':"mb-srp__action action--single mb-srp__card__action"})
  for c in cont_agent:
    cont_ag.append(c.text)
  label=soup.find_all('div',attrs={'class':"mb-srp__card__summary--label"})
  for l in label:
    lab_el.append(l.text)
  sqft=soup.find_all('div',attrs={'class':"mb-srp__card__price--size"})
  for s in sqft:
    sq_ft.append(s.text)
  ads=soup.find_all('div',attrs={'class':"mb-srp__card__ads--name"})
  for ad in ads:
    ad_s.append(ad.text)

len(cont_ag)

len(tit_le)

len(amo_unt)

len(sq_ft)

len(ad_s)

len(lab_el)

import pandas as pd
data=pd.DataFrame({'amount':amo_unt[slice(90)],
                   'title':tit_le[slice(90)],
                    'cont_agent':cont_ag[slice(90)],
                       'sqft':sq_ft[slice(90)],
                          'ads':ad_s[slice(90)],
                          'label':lab_el[slice(90)]})
data

data.to_csv('realestate.csv')