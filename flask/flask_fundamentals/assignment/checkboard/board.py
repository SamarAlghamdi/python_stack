from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def play():
    return render_template("index.html",column=8,row=8)

@app.route("/<int:row>")
def play2(row):
    return render_template("index.html",column=8,row=row)

@app.route("/<int:column>/<int:row>")
def play3(column,row):
    return render_template("index.html",column=column,row=row)

if __name__ == "__main__":
    app.run(debug=True)