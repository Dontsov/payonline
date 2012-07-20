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
'''    
class ReturnViews():
    def __init__(self, return_params):
        self.return_params
        
    @view_config(renderer="templates/return_view.pt")
    def response_print(self):
        response = request.response
        return response 
        '''
   
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

''' Это когда научусь страницы генерировать    
    @view_config(renderer="templates/return_view.pt")
    def return_view(self):
        return {"return_title": CONFIG_VIEW['return_view'],}

    @view_config(renderer="templates/fail_view.pt")
    def fail_view(self):
        return {"page_title": CONFIG_VIEW['fail'], "projects": cause_fail[0],}'''

    
    
    
    
    
    
        

    