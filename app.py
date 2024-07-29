from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota raiz
@app.route('/')
def home():
    return "Hello, Flask!"

# Rota GET
@app.route('/api/resource', methods=['GET'])
def get_resource():
    data = {
        "message": "This is a GET request",
        "data": [1, 2, 3, 4, 5]
    }
    return jsonify(data)

# Rota POST
@app.route('/api/resource', methods=['POST'])
def post_resource():
    content = request.json
    response = {
        "message": "This is a POST request",
        "received_data": content
    }
    return jsonify(response), 201

# Rota PUT
@app.route('/api/resource/<int:id>', methods=['PUT'])
def put_resource(id):
    content = request.json
    response = {
        "message": f"Resource {id} updated",
        "updated_data": content
    }
    return jsonify(response)

# Rota DELETE
@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    response = {
        "message": f"Resource {id} deleted"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
