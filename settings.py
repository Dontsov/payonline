# -*- coding: utf-8 -*-
'''CONFIG = {
    'MerchantId': 8266,
    'PrivateSecurityKey': '03fa466f12f5ddf1195947c1faa6c101',
    'PAYONLINE_URL': 'https://secure.payonlinesystem.com/ru/payment/select/',
    'Currency': 'RUB',
    'CallBackUrl':'',
    'OrderId':'0045', #Идентификатор заказа в системе ТСП
    'Amount':'2.00', #Cумма заказа
    #'OrderDescription':'', #Описаие заказа
    'SecurityKey':'03fa466f12f5ddf1195947c1faa6c101',
    'FailUrl': ''
}
'''
CONFIG = {
    'MerchantId': 8266,
    'PrivateSecurityKey': '03fa466f12f5ddf1195947c1faa6c101',
    'PAYONLINE_URL': 'https://secure.payonlinesystem.com/ru/payment/',
    'Currency': 'RUB',
    'CallBackUrl':'',
    'OrderId':'0045', #Идентификатор заказа в системе ТСП
    'Amount':'2.00', #Cумма заказа
    #'OrderDescription':'', #Описаие заказа
    'SecurityKey':'03fa466f12f5ddf1195947c1faa6c101',
    'FailUrl': ''
}

CONFIG_VIEW = {
    'return_view ': 'Спасибо Вам за покупку',
    'fail'        : 'Произошла ошибка',
}

cause_fail = {0 : 'ошибка раз', 1 : 'ошибка два',}, 
