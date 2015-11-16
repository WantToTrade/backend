from flask import Flask, jsonify, Response, request
from datetime import datetime
import json

app = Flask(__name__)

offers = [{"currency-from": "CZK",
           "currency-to": "EUR",
           "user-id": 1,
           "range": (250, 500),
           "date_until": (2015, 12, 15, 14, 6, 40, 155462)}, 
          {"currency-from": "FOO",
           "currency-to": "BAR",
           "user-id": 2,
           "range": (1000, 1e6),
           "date_until": (2016, 11, 15, 14, 6, 40, 155462)}, 
           ]

users = [{"user-id": 1,
          "name": "Foo Bar"},
         {"user-id": 2,
          "name": "Miro Stuchlik"}]

@app.route('/api/v1/offers', methods=['GET'])
def get_offers():
    return Response(json.dumps(offers))

@app.route('/api/v1/offers', methods=['POST'])
def create_offer():
    offers.append({"foo": "bar"})
    return Response("OK")

@app.route('/api/v1/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    return jsonify(offers[offer_id])

@app.route('/api/v1/offers/<int:offer_id>', methods=['PUT'])
def update_offer(offer_id):
    offer = offers[offer_id]
    offer["currency-from"] = request.form["currency-from"]
    return Response("OK")

@app.route('/api/v1/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    del offers[offer_id]
    return Response("OK")

@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(users[user_id])

@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    user = users[request.form["user-id"]]
    user["name"] = request.forma["name"]
    return Response("OK")

@app.route('/api/v1/user/<int:user_id>', methods=['POST'])
def create_user(user_id):
    users.append({"name": "foo"})
    return Response("OK")

if __name__ == '__main__':
    app.run(debug=True)
