from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app)

@app.route('/getNames', methods = ['GET'])
def getNames():
    response = []
    for i in range(5):
        res = requests.get(f"https://swapi.dev/api/people/"+ str(i+1))
        res_json = res.json()
        response.append(res_json['name'])
    print(response)
    return response

if __name__ == '__main__':
    app.run(debug = True)


# https://api.jikan.moe/v4/anime
