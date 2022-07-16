from web3 import Web3
w3 = Web3()
w3.isConnected('https://bsc-dataseed4.binance.org')
blocks = w3.eth.get_block('latest')
print(blocks)