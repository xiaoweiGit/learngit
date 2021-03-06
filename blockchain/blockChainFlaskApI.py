import hashlib
import json
from textwrap import dedent
from uuid import uuid4
from flask import Flask,jsonify,request
import blockchain


# Instantiate our node
app=Flask(blockchain.__name__)
# Generate a globally unique address for the node
node_identifier=str(uuid4()).replace('-','')
# Instantiate the Blockchain
bkchain=blockchain.Blockchain()

@app.route('/mine',methods=['GET'])
def mine():
    print("mine")
    # We run the proof of work algorithm to get hte next proof
    last_block=bkchain.last_block
    last_proof=last_block['proof']
    print(f"last_block:{last_block},last_proof:{last_proof}");
    proof =bkchain.proof_of_work(last_proof)
    # 给工作量证明的节点提供奖励
    # 发送者为"0"表明是新挖出的币
    bkchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
            )
    print('/mine-new_block...');
    # Forge the new Block by adding it to the chain
    block=bkchain.new_block(proof)
    response={
            'Message':"new Block Forged",
            'index':block['index'],
            'transaction':block['transaction'],
            'proof':block['proof'],
            'previous_hash':block['previous_hash'],
            }
    return jsonify(response),200

@app.route('/transaction/new',methods=['POST'])
def new_transaction():
    print("new_transaction")
    values=request.get_json()
    required=['sender','recipient','amount']
    if not all(k in values for k in required):
       return "Missing values",400

    # Create a new Transaction
    index=bkchain.new_transaction(values['sender'],values['recipient'],values['amount'])
    response = {'message': f'Transaction will be added to Block{index}'}
    return jsonify(response),201

@app.route('/full_chain',methods=['GET'])
def full_chain():
    response={
            'chain':bkchain.chain,
            'length':len(bkchain.chain),
            }
    return jsonify(response),200

@app.route('/nodes/register',methods=['POST'])
def register_nodes():
    values=request.get_json()
    nodes=values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes",400
    for node in nodes:
        blockchain.register_node(node)
    response={
            'message':"new nodes have have been added",
            'total_nodes':list(blockchain.nodes)
            }
    return jsonify(response),201
@app.route('/nodes/resolve',methods=['GET'])
def consensus():
    replaced=blockchain.resolve_conflicts()
    if replaced:
        response={
                'message':'OUr chain was replaced',
                'new+chain':blockchain.chain
                }
    else:
        response={
                'message':'our chain is authoritativ',
                'chain':blockchain.chain
                }
    return jsonify(response),200
if __name__=='__main__':
        app.run(host='0.0.0.0',port=5000)
        app.run(host='0.0.0.0',port=5001)
