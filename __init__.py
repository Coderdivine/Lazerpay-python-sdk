import requests
import numpy as np
import pandas as pd
import string    
import random # define the random module
#0x337610d27c682E347C9cD60BD4b3b107C9d34dDd
#0xD275Da57B35089a51A3E4659AcDF13311Ebd6183
from Web3Package import WebProvider
WebProviders = WebProvider()
class LazerPayFinance():
    def __init__(self,secretKey,publicKey,Partial,chain):
        self.chain = chain
        self.secretKey = secretKey
        self.publicKey = publicKey
        self.publicKey = publicKey
        self.Partial = Partial
    def walletBalance(self,coin):
        #The coin balance you want to get, eg USDT, DAI, BUSD, USDC
        url = 'https://api.lazerpay.engineering/api/v1/wallet/balance/?coins=USDC'
        #requesting = requests.Session()
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
            }
        #requesting.headers.update({'Authorization':self.secretKey})
        response = requests.get(url,headers=headers)
        return response.json()
    def Authentication(self,method,url,params,type):
        requesting = requests.Session()
        #requesting.auth = ('user', 'pass')
        if type == "public":
           requesting.headers.update({'x-api-key':self.publicKey})
        else:
           requesting.headers.update({'x-api-key':self.secretKey})
        if method == "POST":
            r = requesting.post(url,params)
           # return r.json()
        else:
            r = requesting.get(url)
            return r.json()
    def initializePayment(self,params):
        url = 'https://api.lazerpay.engineering/api/v1/transaction/initialize'
        # params = {
        #     'reference':'',
        #     'customer_name':'',
        #     'customer_email':'',
        #     'coin':'',
        #     'currency':'',
        #     'amount':10,
        #     'accept_partial_payment':self.Partial
        # }
        #requesting = requests.Session()
        headers = {
            'Content-type':'application/json',
            'x-api-key':self.publicKey
        }
        #requesting.headers.update({'x-api-key':self.publicKey})
        response = requests.post(url,json=params,headers=headers)
        return response.json()
    def getFiats(self):
        #The amount field should be in your fiat currency. 
        # The currencies we support are USD, AED, GBP, EUR and NGN
        response = {
            0:'USD',
            1:'AED',
            2:'GBP',
            3:'EUR',
            4:'NGN'
        }
        return response
    def getCoins(self):
        url = 'https://api.lazerpay.engineering/api/v1/coins'
        headers = {
            'Content-type':'application/json',
            'x-api-key':self.publicKey
        }
        # requesting = requests.Session()
        # requesting.headers.update({'x-api-key':self.publicKey})
        response = requests.get(url,headers=headers)
        return response.json()
    def createLink(self,params):
        url = 'https://api.lazerpay.engineering/api/v1/payment-links'
        # params = {
        #     'title':'hello',
        #     'description':'this is hello',
        #     'type':'standard',
        #     'currency':'USD',
        #  #   'redirect_url':'https://docs.lazerpay.finance'
        # }
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'authorization':self.secretKey
        }
        response = requests.post(url,json=params,headers=headers)
        return response.json()
    def verifyPayment(self,reference_address):
        url = 'https://api.lazerpay.engineering/api/v1/transaction/verify/'+reference_address
        # requesting = requests.Session()
        # requesting.headers.update({'x-api-key':self.publicKey})
        print(url)
        headers = {
            'Content-type':'application/json',
            'x-api-key':self.publicKey
        }
        response = requests.get(url,headers=headers)
        return response.json()
    def createReferenceString(self,length):  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))    
        return str(ran)
    def previousLink(self):
        url = 'https://api.lazerpay.engineering/api/v1/payment-links'
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        response = requests.get(url,headers=headers)
        return response.json()
    def FetchSingleLink(self,reference):
        url = 'https://api.lazerpay.engineering/api/v1/payment-links/'+reference
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        response = requests.get(url,headers=headers)
        return response.json()
    def updateLink(self,reference,params):
        url = 'https://api.lazerpay.engineering/api/v1/payment-links/'+reference
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        # params = {
        #     'status':'active',
        # }
        response = requests.put(url,json=params,headers=headers)
        return response.json()
    def transferCrypto(self,params):
        url = 'https://api.lazerpay.engineering/api/v1/transfer'
        # params = {
        #     'reference':'92992-82u2892-000',
        #     'amount':'10',
        #     'recipient':'0xf000...',
        #     'coin':'USDT',
        #     'metadata':{
        #         'type':'Crypto transfer'
        #     },
        #     'blockchain':'Binance Smart Chain'
        # }
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        response = requests.post(url,json=params,headers=headers)
        return response.json()
    def swapCrypto(self,params):
        url = 'https://api.lazerpay.engineering/api/v1/swap/crypto'
        # params = {
        #     'reference':'just a string',
        #     'amount':'10',
        #     'fromCoin':'USDC',
        #     'toCoin':'USDT',
        #     'metadata':{
        #         'type':'Crypto Swap'
        #     },
        #     'blockchain':'Binance Smart Chain'
        # }
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        response = requests.post(url,json=params,headers=headers)
        return response.json()
    def swapCharge(self,params):
        url = 'https://api.lazerpay.engineering/api/v1/swap/crypto/amount-out'
        # params = {
        #     'amount':'10',
        #     'fromCoin':'DAI',
        #     'toCoin':'USDT',
        #     'blockchain':'Binance Smart Chain'
        # }
        # requesting = requests.Session()
        # requesting.headers.update({'Authorization':self.secretKey})
        headers = {
            'Content-type':'application/json',
            'Authorization':self.secretKey
        }
        response = requests.post(url,json=params,headers=headers)
        return response.json()
    def getRate(self):
        url = 'https://api.lazerpay.engineering/api/v1/rate'
        requesting = requests.Session()
        requesting.headers.update({'Authentication':self.publicKey})
        # headers = {
        #     'Content-type':'application/json',
        #     'Authorization':self.publicKey
        # }
        response = requesting.get(url)
        return response.json()
    def createRandomAccount(self):
        acc = WebProviders.getAccounts()
        return acc
    def getBalance(self,address,type):
        bal = WebProviders.getBalance(address,type)
        return bal
print('___tesing___')
#py -m pip install setuptools twine
#py setup.py sdist
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
print('__DONE___')

