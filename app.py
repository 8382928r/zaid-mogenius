import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://gokdelenler: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@github.com/gokdelenler/startager ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
