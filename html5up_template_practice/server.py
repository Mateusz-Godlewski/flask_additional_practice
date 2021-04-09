from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def home_page():
    return render_template("index.html")


@app.route("/generic.html")
def generic():
    return render_template("generic.html")


@app.route("/elements.html")
def elements():
    return render_template("elements.html")


if __name__ == "__main__":
    app.run(debug=True)