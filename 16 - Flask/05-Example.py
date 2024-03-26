from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Database işlemleri
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "shopdb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

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