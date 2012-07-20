# -*- coding: utf-8 -*-
from pyramid.view import view_config
import colander
import urllib, urllib2
from hashlib import md5
from deform import Form
from deform import ValidationFailure
from formpay import *
from settings import *
from pyramid.response import Response

class FormPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer="templates/formpay_view.pt")
    def form_view(self):
        values = {
                "url_pay" : CONFIG['PAYONLINE_URL'],
                "Currency" : CONFIG['Currency'],
                "MerchantId" : CONFIG['MerchantId'],
                "PrivateSecurityKey" : CONFIG['PrivateSecurityKey'],
                "OrderId" : CONFIG['OrderId'],
                "Amount" : CONFIG['Amount'],
                "SecurityKey" : CONFIG['SecurityKey'],
            }
            
        return {"values": values}
    
    def get_security_key(self, params):
        key = md5('&'.join('='.join(i) for i in params)).hexdigest()
        '''key = hashlib.md5()
         key.update(params)
         return key.hexdigest()'''
        return key
    # Данная функция нужна для правильной подаче параметров для вычисления SecurityKey
    def get_params(self): 
        params = [('MerchantId', CONFIG['MerchantId']), 
              ('OrderId',    CONFIG['OrderId']),
              ('Amount',     CONFIG['Amount']), 
              ('Currency', CONFIG['Currency']), #В тестовом варианте следующего параметра нет 
              ('PrivateSecurityKey' , CONFIG['PrivateSecurityKey']),]
        return params
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

''' Это когда научусь страницы генерировать    
    @view_config(renderer="templates/return_view.pt")
    def return_view(self):
        return {"return_title": CONFIG_VIEW['return_view'],}

    @view_config(renderer="templates/fail_view.pt")
    def fail_view(self):
        return {"page_title": CONFIG_VIEW['fail'], "projects": cause_fail[0],}'''

    
    
    
    
    
    
        

    