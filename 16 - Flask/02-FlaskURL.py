# pip install flask

from flask import Flask

app = Flask(__name__)

# Home
@app.route("/")
def index():
    return "Home"

# About
@app.route("/about")
def about():
    return "Hakkımda"

if __name__ == "__main__":
    app.run(debug=True)