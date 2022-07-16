from web3 import Web3, EthereumTesterProvider
w3 = Web3(EthereumTesterProvider())
w3.isConnected()
blocks = w3.eth.get_block('latest')
print(blocks)