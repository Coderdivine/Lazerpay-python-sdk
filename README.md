# LazerPay Python sdk

This python sdk helps devlopers interact with LazerPay api in a very simple and easy way. It also have cool features to use for testing.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install LazerPayFinance.

```bash
pip install LazerPayFinance
```

If the approach is not working try this

```bash
py -m pip instal LazerPayFinance
```

## Usage

firstly you will nedd to import and call the function like the following example given below

```python
import LazerPayFinance
lazerpay = LazerPayFinance('sk_test_Fh4xj28OXmTO3Ou08zu9xl9h4nslTysGugQI0l3s6J2bdT5T1I','pk_test_0bE5tKpLON8OGVdmjqAxL0woAwCEth65Lkg9hdxr9jvvCiiKv4',True,'Binance Smart Chain')
```

You would need both your public key and secret key to call this function.

### How create a random reference string

The example below shows you how to create random reference string.

```python
ref = lazerpay.createReferenceString(20)
```

this function takes a single parameter which is the length of the string and also returns a random string of the length specified.

### Wallet Balance

To check a wallet balance a you need to do is call this function below

```python
walletbalance = lazerpay.walletBalance('USDT')
print("wallet_balance =>")
print(walletbalance)
```

This takes only one argument which is the name of the coin you wish to check.

#### Note: Lazerpay only support limited amount of token. To get the list of token supported by LazerPay you will need to call this function.

```python
getCoins = lazerpay.getCoins()
print("getCoins =>")
print(getCoins)
```

This would return the list of token supported bt lazerpay.

## Fiats

To get the list of supported fiat simply call this function.

```python
getFiats = lazerpay.getFiats()
print("getFiats =>")
print(getFiats)
```

This would return the list of supported fiats.

Here's a quick example on how to use LazerPayFinance using Python

```python
import LazerPayFinance
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
        'title':'Hello this a new link',
        'description':'Description of payment',
        'amount':450,
        'type:':'standard',
        'logo':'https://www.thisisjustalogo.com',
        'currency':'NGN',
        'redirect_url':'https://hesichimdi.xyz'
        }
createLink =  lazerpay.createLink(p_2)
print("createLink =>")
# print(createLink)
ref = createLink['data']['reference']
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
#done
p_4 = {
            'reference':'92992-82u2892-0800',
            'amount':10.00,
            'recipient':'0xD275Da57B35089a51A3E4659AcDF13311Ebd6183',
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
            'amount':10.00,
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
            'amount':10.00,
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
getRate = lazerpay.getRate('USDT','NGN')
print("getRate =>")
print(getRate)
createRandomAccount = lazerpay.createRandomAccount()
print('createRandomAccount=>')
print(createRandomAccount)
getBalance = lazerpay.getBalance("0xD275Da57B35089a51A3E4659AcDF13311Ebd6183","to")#toWei. Use from to convert from wei to ether
print("getBalance =>")
print(getBalance)
print("__DONE__")

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
