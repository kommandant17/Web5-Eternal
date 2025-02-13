import json
import time
import hashlib
import flask
from flask import request, jsonify

# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data="Genesis Block - Web5-Eternal", previous_hash='0')

    def create_block(self, data, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

# Initialize Blockchain
blockchain = Blockchain()

# Flask API
app = flask.Flask(__name__)

@app.route('/mine', methods=['GET'])
def mine_block():
    prev_block = blockchain.get_previous_block()
    new_block = blockchain.create_block(data="New Block Mined", previous_hash=prev_block['hash'])
    return jsonify(new_block), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.chain), 200

# Start Node
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
