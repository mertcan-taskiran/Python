from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt 

# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("Full Name", validators=[validators.Length(min=3, max=30)])
    username = StringField("UserName", validators=[validators.Length(min=3, max=30)])
    email = StringField("Email")
    password = PasswordField("Password", validators=[
        validators.DataRequired(message="Lütfen bir parola giriniz!"),
        validators.EqualTo(fieldname="confirm", message="Parolanız uyuşmuyor!")
    ])
    confirm = PasswordField("Confirm Password")


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

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():

        # Kullanıcıyı veri tabanına kayıt etme
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "Insert into users(name,email,username,password) VALUES(%s, %s, %s, %s)"
        cursor.execute(sorgu, (name,email,username,password))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("index"))
    else:
        return render_template("register.html", form=form)

# Dinamik URL
@app.route("/products/<string:id>")
def detail(id):
    return "Product Id: " + id

if __name__ == "__main__":
    app.run(debug=True)