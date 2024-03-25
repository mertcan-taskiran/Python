from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route("/")
def index():
    
    article = dict()
    article["title"] = "Deneme Title"
    article["body"] = "Deneme Body"
    article["author"] = "Mertcan"

    return render_template("index.html", article = article)

if __name__ == "__main__":
    app.run(debug=True)