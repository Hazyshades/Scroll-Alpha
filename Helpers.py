import random

networks = {
    'Optimism': {
        'net_name': 'Scroll Alpha Testnet',
        'rpc': 'https://alpha-rpc.scroll.io/l2',
        'chain_id': 534353,
        'symbol': 'ETH',
        'explorer': 'https://blockscout.scroll.io',
    }
}

value_input = random.uniform(0.0099, 0.0109)
bridge_amount = 0.005
