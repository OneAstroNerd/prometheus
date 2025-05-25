from flask import Flask


messages_ = [
    """Title: This just a test.
---
Hey this is just a test.
this is a test and nithing else."""
]


app = Flask(__name__)

@app.route('/send')
def home():
    return 'Hello, World!'

@app.route('/inbox<id>' )
def home(id):
    if id == 0:
        for i in range(len(messages_)):
            print(i+1,":", messages_[i].splitlines()[0])
    global messages_
    return messages_[id-1]


@app.route('/status')
def about():
    global messages_

    return len(messages_)