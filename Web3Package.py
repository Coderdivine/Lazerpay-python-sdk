from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed4.binance.org"))
blocks = web3.eth.get_block('latest')
print(blocks)