from os import access
from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed4.binance.org"))
print(web3.isConnected())
#no params
class WebProvider:
    def __init__(self):
        pass
    def BlockNumber(self):
       block =  web3.eth.blockNumber()
       return block
    def getBalance(self,address,type): 
        balance  = web3.eth.getBalance(address)
        if type == 'from':
            return web3.fromWei(balance, 'ether')
        elif type == 'to':
            return web3.toWei(balance,'ether')
        else:
            return balance
    def LatestBlock(self):
        block = web3.eth.get_block('latest')
        return block
    def getGasPrice(self):
        price = web3.eth.gas_price
        return price
    def getAccounts(self):
        acc = web3.eth.accounts
        return acc
    def getChainId(self):
        chain =  web3.eth.chain_id
        return chain
    def createAccount():
        acc = web3.eth.accounts.create()
        return acc
