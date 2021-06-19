from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}"

@app.route("/repeat/<int:number>/<name>")
def repeat_name(number, name):
    
    return f"{name} "* number

@app.errorhandler(404)
def error_msg(e):
    
    return "Sorry! No response. Try again."



if __name__ == "__main__":
    app.run(debug=True)