from django.conf import settings
# from balance import Web3
from web3 import Web3


def get_balances(address, network):
    """
    Get balances from balance.
    Return: Balance of the wallet.
    """
    try:
        endpoint = settings.ENDPOINTS[network]
        w3 = Web3(Web3.HTTPProvider(endpoint))
        balance = w3.eth.get_balance(address)
        return balance
    except:
        return False


def check_input_network(network):
    """
    Check if the network is supported
    """
    networks = [
        "ETH",
        "ArbitrumETH",
        "Optimism",
        "Gnosis xDa",
    ]
    if network in networks:
        return network
    return False


def check_input_address(address):
    """
    Check if the address is valid
    """
    if Web3.isAddress(address):
        return address
    return False
