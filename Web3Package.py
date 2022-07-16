from web3 import Web3
w3 = Web3()
w3.isConnected()
blocks = w3.eth.get_block('latest')
print(blocks)