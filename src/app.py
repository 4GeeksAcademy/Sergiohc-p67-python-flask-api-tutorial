from flask import Flask, jsonify, request
todos = [  { "label": "My first task", "done": False } ]


app = Flask(__name__)


@app.route("/home")
def home():
    return "Hola"


@app.route("/about-me")
def about():
    return "¿Qué tal?"




@app.route("/contact-me")
def contact():
    return "Adiós"



@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body =  request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request.get_json(force=True))
    return jsonify(todos)




@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
