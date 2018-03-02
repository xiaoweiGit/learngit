# http://mp.weixin.qq.com/s/uyBGs0krBEWLP3IiDDTDyg
import hashlib
import json
from time import time
import requests
from urllib.parse import urlparse

class Blockchain(object):
    def __init__(self):
        self.chain=[];
        self.current_transactions=[]
        # Create the genesis blcok
        self.new_block(previous_hash=1,proof=100)
        self.nodes=set()
    def new_block(self,proof,previous_hash=None):
        """
        生成新块
        :parm proof:<int> the proof given by the proof of work algorithm
        :param previous_hash:(Optional)<str>Hash of previous Block
        :return :<dict>New Block
        """
        block ={
            'index':len(self.chain)+1,
            'timestap':time(),
            'transaction':self.current_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1]),
            }
        print("Blockchain-- new_block");
        # Reset the current list of transaction
        self.current_transactions=[]
        self.chain.append(block)
        return block


    def new_transaction(self,sender,recipient,amount):
        """
        生成新的交易信息，信息会加入到下一个待挖的区块中
        :parm sender:<str> Address of the sender
        :parm recipient:<str> address of teh Recipient
        :parm amount:<int>Amount
        :Return <int>The index of hte Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount
            })
        print(self.current_transactions)
        return self.last_block['index'] + 1;
    @staticmethod
    def hash(block):
        """
        生成块的SHA-256hash 值
        :param block :<dict> Block
        :return :<str>
        """
        # We must make sure that the dictionary is Ordered,or we'll have inconsistent hashes
        block_string=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self,last_proof):
        """
        简单的工作量证明：
        -查找一个p'使的hash(pp')以4个0开头
        -p是上个快的证明，p'是当前的证明
        :parm last_proof:<int>
        :return:<int>
        """
        print("proof_of_work")
        proof=0;
        while self.value_proof(last_proof,proof) is False:
            proof +=1
        return proof
        
    @staticmethod
    def value_proof(last_proof,proof):
        """
        验证证明: 是否hash(last_proof, proof)以4个0开头?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess=f'{last_proof}{proof}'.encode()
        guess_hash=hashlib.sha256(guess).hexdigest()
        print(f"value_proof:{guess_hash}")
        return guess_hash[:4]=="0000"
    def register_node(self,address):
        """
        add a new node to the list of nodes
        :para address:<str>address of node.Eg.'http://'
        :return: None
        """
        parsed_url=urlparse(address)
        self.nodes.add(parsed_url.netloc)

   def valid_chain(self,chain):
       """
       Determine if a given blockchain is valid
       :param chain:<list> a blockchain
       :return:<bool>True if valid,False if not
       """
       last_block=chain[0]
       current_index=1
       while current_index<len(chain):
           block=chain[current_index]
           print(f"{last_block}")
           print(f"{block}")
           print(f"{\n--------\n}")
           # check that the hash of the block is corrent
           if block['previous_hash'] !=self.hash(last_block):
               return False
           # check that the proof of work is corrent
           if not self.valid_proof(last_block['proof'],block['proof']):
               return False
           last_block=block
        return True

    def resolve_conflicts(self):
        """
        共识算法解决冲突
        使用网络中最长的链.
        :return: <bool> True 如果链被取代, 否则为False
        """
        neighbours=self.nodes
        new_chain=None
        # We're only looking for chains longer than ours
        max_length=len(self.chain)
        # Grab and verify the chains from all teh nodes in our network
        for node in neighbours:
            response=requests.get(f"http://{node}/chain")

        
        
