from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []

@app.route('/')
def entry_point():
    return 'SIC Technical Assignment #1'

@app.route('/data', methods=['POST'])
def post():
    data = request.get_json()
    if data:
        data_store.append(data)
        print(f"Received data: {data}")
        return jsonify({"message": "Data received successfully"}), 200
    else:
        return jsonify({"message": "No data received"}), 400

@app.route('/data', methods=['GET'])
def get():
    return jsonify(data_store), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)