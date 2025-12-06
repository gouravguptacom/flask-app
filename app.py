from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/greet')
def hello():
    return "Hello, World"

@app.route('/greet/<name>', methods=["GET", "POST"])
def greet(name):
    if request.method == "GET":
        return "You made a GET request\n", 200
    elif request.method == "POST":
        response = make_response("You made a POST reques\n")
        response.status_code = 201
        response.headers["content-type"] = "text/plain" # "application/octet-stream"
        return response
    else:
        return "You will never see this message\n"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/handle_url_params')
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args.get("greeting")
        name = request.args.get("name")
        return f"{greeting}, {name}"
    else:
        return "Some parameters are missing"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)