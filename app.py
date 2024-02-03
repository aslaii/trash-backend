from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/route-optimize', methods=['POST'])
def route_optimize():
    # Extracting data from the request
    data = request.json
    a = data.get('a', 0)
    b = data.get('b', 0)
    c = data.get('c', 0)
    print("Received values:", a, b, c)

    # Performing the calculation
    result = a + b + c

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=3001)
