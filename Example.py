from __init__ import LazerPayFinance
lazerpay = LazerPayFinance('sk_test_Fh4xj28OXmTO3Ou08zu9xl9h4nslTysGugQI0l3s6J2bdT5T1I','pk_test_0bE5tKpLON8OGVdmjqAxL0woAwCEth65Lkg9hdxr9jvvCiiKv4',True,'Binance Smart Chain')
ref = lazerpay.createReferenceString(20)
print("ref => " + str(ref))
walletbalance = lazerpay.walletBalance('USDT')
print("wallet_balance =>")
print(walletbalance)
#initializePayment
p_1 = {
            'reference':ref,
            'customer_name':'Chimdi',
            'customer_email':'chimdi4332@gmail.com',
            'coin':'USDC',
            'currency':'NGN',
            'amount':10,
            'accept_partial_payment':True
        }
#initializePayment = lazerpay.initializePayment(p_1)
#print("initializePayment =>")
#print(initializePayment)
#getFiats = lazerpay.getFiats()
#print("getFiats =>")
#print(getFiats)
#getCoins = lazerpay.getCoins()
#print("getCoins =>")
#print(getCoins)
p_2 = {
            'title':'hello',
            'description':'this is hello',
            'type':'standard',
            'currency':'USD',
            'redirect_url':'https://docs.lazerpay.finance'
        }
createLink = lazerpay.createLink(p_2)
print("createLink =>")
print(createLink)
#verifyPayment = lazerpay.verifyPayment(ref)
#print("verifyPayment =>")
#print(verifyPayment)
previousLink = lazerpay.previousLink()
print("previousLink =>")
print(previousLink)
FetchSingleLink = lazerpay.FetchSingleLink(ref)
print("FetchSingleLink =>")
print(FetchSingleLink)
p_3 = {
            'status':'active',
        }
updateLink = lazerpay.updateLink(ref,p_3)
print("updateLink =>")
print(updateLink)
p_4 = {
            'reference':'92992-82u2892-000',
            'amount':'10',
            'recipient':'0xf000...',
            'coin':'USDT',
            'metadata':{
                'type':'Crypto transfer'
            },
            'blockchain':'Binance Smart Chain'
        }
transferCrypto = lazerpay.transferCrypto(p_4)
print("transferCrypto =>")
print(transferCrypto)
p_5 = {
            'reference':'just a string',
            'amount':'10',
            'fromCoin':'USDC',
            'toCoin':'USDT',
            'metadata':{
                'type':'Crypto Swap'
            },
            'blockchain':'Binance Smart Chain'
        }
swapCrypto = lazerpay.swapCrypto(p_5)
print("swapCrypto = >")
print(swapCrypto)
p_6 = {
            'reference':'just a string',
            'amount':'10',
            'fromCoin':'USDC',
            'toCoin':'USDT',
            'metadata':{
                'type':'Crypto Swap'
            },
            'blockchain':'Binance Smart Chain'
        }
swapCharge = lazerpay.swapCharge(p_6)
print("swapCharge =>")
print(swapCharge)
getRate = lazerpay.getRate()
print("getRate =>")
print(getRate)
print("__DONE__")