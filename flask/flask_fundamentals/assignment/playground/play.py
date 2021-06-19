from flask import Flask, render_template
app = Flask(__name__)
@app.route("/play")
def play():
    return render_template("index.html",number=3)

@app.route("/play/<int:number>")
def play2(number):
    return render_template("index.html",number=number)

@app.route("/play/<int:number>/<string:color>")
def play3(number,color):
    return render_template("index.html",number=number,color=color)
if __name__ == "__main__":
    app.run(debug=True)

