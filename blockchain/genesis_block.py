import hashlib
import json
import time

def create_genesis_block():
    genesis_block = {
        'index': 0,
        'timestamp': time.time(),
        'data': 'Genesis Block - Web5-Eternal',
        'previous_hash': '0' * 64,
        'hash': ''
    }
    genesis_block['hash'] = hashlib.sha256(json.dumps(genesis_block, sort_keys=True).encode()).hexdigest()
    return genesis_block

if __name__ == "__main__":
    genesis_block = create_genesis_block()
    print("🌟 Web5-Eternal Genesis Block Created! 🌟")
    print(json.dumps(genesis_block, indent=4))
