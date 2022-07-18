<p>
<img title="Lazerpay" src= "https://res.cloudinary.com/njokuscript/image/upload/v1646279538/lazerpay_logo_no-bg_trkkye.png" width="300px"/>
</p>

#### The Lazerpay v1 Python SDK

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install LazerPayFinance.

```bash
pip install LazerPayFinance
```
If the approach is not working try this
```bash
py -m pip instal LazerPayFinance
```
```python
import LazerPayFinance
lazerpay = LazerPayFinance(LAZER_PUBLIC_KEY, LAZER_SECRET_KEY,True,'Binance Smart Chain')
```
The function above takes four parameters
##### LAZER_PUBLIC_KEY
##### LAZER_SECRET_KEY
##### Partial Payment (True,False)
##### Current Supported Network

Use TEST API keys for testing, and LIVE API keys for production

## Lazerpay Methods exposed by the sdk

**1**. **Payment**

- Initialize Payment
- Confirm Payment

**2**. **Payout**

- Crypto Payout
- Bank Payout ~ This is coming to V2

**3**. **Swap**

- Crypto swap
- Get Crypto Swap Amount Out

**4**. **Payment Links**

- Create payment links
- Get all payment links
- Get a single payment link
- Update a payment Link

**5**. **Misc**

- Get all accepted coins
- Get wallet balance

**6**. **Wallet**

- Get random wallet address
- Get random reference

## Payment

#### `Initialize Payment`
This describes to allow your customers to initiate a crypto payment transfer.
```python
import LazerPayFinance
lazerpay = LazerPayFinance(LAZER_PUBLIC_KEY, LAZER_SECRET_KEY,True,'Binance Smart Chain')

initializePayment = {
            'reference':82927118-282816-1,
            'customer_name':'Chimdindu',
            'customer_email':'chimdi4332@gmail.com',
            'coin':'USDC',
            'currency':'NGN',
            'amount':10,
            'accept_partial_payment':True
        }
initializePayment = lazerpay.initializePayment(initializePayment )
print("initializePayment =>")
print(initializePayment)
```
#### `Confirm Payment`

This describes to allow you confirm your customers transaction after payment has been made.
```python
verifyPayment = lazerpay.verifyPayment(ref)
print("verifyPayment =>")
print(verifyPayment)
```
## Transfer

#### `Crypto Payout`

This describes to allow you withdraw the crypto in their lazerpay balance to an external address
```python
p_4 = {
            'reference':'92992-82u2892-0800',
            'amount':10.00,
            'recipient':'0xD275Da57B35089a51A3E4659AcDF13311Ebd6183',#hex value
            'coin':'USDT',
            'metadata':{
                'type':'Crypto transfer'
            },
            'blockchain':'Binance Smart Chain'
        }
transferCrypto = lazerpay.transferCrypto(p_4)
print("transferCrypto =>")
print(transferCrypto)
```
## Swap

#### `Crypto swap`

This describes to allow you swap swap between two stable coins 
```python
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
```
#### `Get Crypto Swap Amount Out`

This describes the amount you will receive on swap even before initiating the swap  
```python
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
```
## Payment Links

#### `Create a payment link`

This describes to allow you create a Payment link programatically
```python
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
print(createLink)
```
#### `Update a payment link`

This describes disabling or enabling a payment link by updating it
```python
p_3 = {
            'status':'active',
        }
updateLink = lazerpay.updateLink(ref,p_3)
print("updateLink =>")
print(updateLink)
```
#### `Get all payment links`

This describes to allow you get all Payment links created
```python
previousLink = lazerpay.previousLink()
print("previousLink =>")
print(previousLink)
```
#### `Get a single payment link`

This describes to allow you get a Payment link by it's identifier
```python
FetchSingleLink = lazerpay.FetchSingleLink(ref)#reference string
print("FetchSingleLink =>")
print(FetchSingleLink)
```
## Misc

#### `Get Accepted Coins`

This gets the list of accepted cryptocurrencies on Lazerpay
```python
getCoins = lazerpay.getCoins()
print("getCoins =>")
print(getCoins)
```
#### `Get Wallet Balance`

Get get wallet balance by specifying the coin
```python
walletbalance = lazerpay.walletBalance('USDT')
print("wallet_balance =>")
print(walletbalance)
```
#### `Get Wallet Balance`

Get get wallet balance by specifying the Address
```python
getBalance = lazerpay.getBalance(ADRESS,"to") #toWei. Use 'from' to convert from wei to ether
print("getBalance =>")
print(getBalance)
```
#### `Get Random Address`

This method get random address on the current blockChain specified
```python
createRandomAccount = lazerpay.createRandomAccount()
print('createRandomAccount=>')
print(createRandomAccount)
```
#### `Get Rate`

This method get the rate of a particular crypto to a specified currency e.g NGN,USD .e.t.c
```python
getRate = lazerpay.getRate('USDT','NGN')
print("getRate =>")
print(getRate)
```
#### `Get Accepted Fiats`

This gets the list of accepted fiat on Lazerpay

```python
getFiats = lazerpay.getFiats()
print("getFiats =>")
print(getFiats)
```
#### `Creating random string`
This function creates a random string and takes a single parameter as argument.
```python
ref = lazerpay.createReferenceString(20)#Length of string
print("ref => " + str(ref))
print("__DONE__")
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## `Example`
To view a full example on how to use this sdk, click
[here](https://github.com/Coderdivine/Lazerpay-python-sdk/blob/main/Example.py)
## `License`
[MIT](https://choosealicense.com/licenses/mit/)
