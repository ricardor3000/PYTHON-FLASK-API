from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "id":1, "label": "Sample todo 1", "done": True },
    { "id":2, "label": "Sample todo 2", "done": True },
    { "id":3, "label": "Sample todo 3", "done": True },
]

@app.route('/', methods=['GET'])
def users():
    json_text = jsonify(todos)
    return json_text

@app.route('/', methods=['POST'])
def post_user():
    user = request.json
    todos.append(user)
    return jsonify({"mensaje": "estatus perfecto de datos POST"}), 201

@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for users in todos:
        if users.get( 'id' ) == user_id:
            print("rutal que ha sido borrada")
    print(users)        
    return "ruta para delete habilitada"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
