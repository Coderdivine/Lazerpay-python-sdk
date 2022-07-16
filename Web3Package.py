from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed4.binance.org"))
print(web3.isConnected())
#blocks = web3.eth.get_block('latest')
#print(blocks)
class WebProvider():
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
