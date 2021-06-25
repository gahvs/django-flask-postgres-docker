from flask import Flask, jsonify
from os import environ

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify(hello='world')

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)