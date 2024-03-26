from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # products = ["Ürün 1", "Ürün 2", "Ürün 3"]
    products = [
            {"id":1, "name":"Ürün 1", "price":1000},
            {"id":2, "name":"Ürün 2", "price":2000},
            {"id":3, "name":"Ürün 3", "price":3000},
        ]

    return render_template("index.html", stok=1, products = products) # Koşul Durumu ve Döngü

@app.route("/about")
def about():
    return render_template("about.html")

# Dinamik URL
@app.route("/products/<string:id>")
def detail(id):
    return "Product Id: " + id

if __name__ == "__main__":
    app.run(debug=True)