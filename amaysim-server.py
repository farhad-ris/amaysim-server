from flask import Flask, Response, jsonify
import os, json, sys
from pprint import pprint


app = Flask(__name__)


@app.route('/json', methods=["GET"])
def server():


    with open('data.json') as data_file:

        data = json.load(data_file)
        resp = jsonify(data)
        resp.status_code = 200

    return resp


if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)

