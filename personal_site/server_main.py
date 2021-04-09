from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(r"C:\Users\godle\Desktop\100\flask_personal_site\personal_site\templates\index.html")


if __name__ == "__main__":
    app.run(debug=True)