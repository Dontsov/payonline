# -*- coding: utf-8 -*-
'''
Данный файл --- остаток от первой версии программы, где был выбран более сложный и во многом неправильный 
способ передачи и обработки данных. На данный момент никак не используется.
'''
from settings import *
import urllib, urllib2
from hashlib import md5
import hashlib
import time
import datetime
from pyramid.httpexceptions import HTTPFound
import urllib2
import json


def get_security_key(params):
    key = md5('&'.join('='.join(i) for i in params)).hexdigest()
    '''key = hashlib.md5()
    key.update(params)
    return key.hexdigest()'''
    return key

page = CONFIG['PAYONLINE_URL']
raw_params = [('MerchantId', CONFIG['MerchantId']), 
              ('OrderId',    CONFIG['OrderId']),
              ('Amount',     CONFIG['Amount']), 
              ('Currency', CONFIG['Currency']),] #В тестовом варианте следующего параметра нет 
              #('PrivateSecurityKey' , CONFIG['PrivateSecurityKey']),]
params = urllib.urlencode(raw_params)
# Добавляем SecurityKey в список параметров
post_params = params+'&SecurityKey='+'03fa466f12f5ddf1195947c1faa6c101'     #+get_security_key(params)


def post_request(page, post_params):
    request = urllib2.Request(page, post_params)
    page = urllib2.urlopen(request)
    return HTTPFound(location = page)



def myview():
    json_payload = json.dumps({'a':1})
    headers = {'Content-Type':'application/json; charset=utf-8'}
    req = urllib2.Request('http://yandex.ru/', json_payload, headers)
    return urllib2.urlopen(req)
''''
def info_add(name, email):
    dt = datetime.datetime.now()
    file = open(dt.strftime('%Y.%m.%d__:%H:%M') +".txt", "w+")
    info = dt.strftime('%Y.%m.%d___:%H:%M') + '___:' +  name +'___:' + email
    file.write(info)
    file.close()
    return file
'''
def index():
    ind = HTTPFound('https://secure.payonlinesystem.com/ru/payment/select/')
    return ind
    
#f = open('test.txt', 'w')
#f.write(post_request(page, params))


     