from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField
from passlib.hash import sha256_crypt 
from functools import wraps

# Kullanıcı Giriş Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Lütfen giriş yapın.","danger")
            return redirect(url_for("login"))
    return decorated_function

# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("Fullname", validators=[validators.Length(min=3, max=30)])
    username = StringField("Username", validators=[validators.Length(min=3, max=30)])
    email = StringField("Email")
    password = PasswordField("Password", validators=[
        validators.DataRequired(message="Lütfen bir parola giriniz!"),
        validators.EqualTo(fieldname="confirm", message="Parolanız uyuşmuyor!")
    ])
    confirm = PasswordField("Confirm Password")

# Kullanıcı Girişi
class LoginForm(Form):
    username = StringField("Username")
    password = StringField("Parola")

app = Flask(__name__)

app.secret_key="shopdb" # for flash message

# Database işlemleri
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "shopdb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

# About
@app.route("/about")
def about():
    return render_template("about.html")

# Dashboard
@app.route("/dashboard")
@login_required # decorator
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From products where author = %s"
    result = cursor.execute(sorgu,(session["username"],))
    if result > 0:
        products = cursor.fetchall()
        return render_template("dashboard.html", products = products)
    else:
        return render_template("dashboard.html")

# Register
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

        flash("Başarıyla kayıt olundu.", "success") #flash message

        return redirect(url_for("login"))
    else:
        return render_template("register.html", form=form)

# Login
@app.route("/login",methods =["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()
        sorgu = "Select * From users where username = %s"
        result = cursor.execute(sorgu, (username,))

        if result > 0:
            data = cursor.fetchone() # Kullanıcının tüm bilgisini alır.
            real_password = data["password"]
            
            if sha256_crypt.verify(password_entered, real_password):
                flash("Başarıyla giriş yaptınız.", "success")

                session["logged_in"] = True
                session["username"] = username

                return redirect(url_for("index"))
            else:
                flash("Parola yanlış.", "danger")
                return redirect(url_for("login"))
        else:
            flash("Kullanıcı bulunamadı.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# Products
@app.route("/products")
def products():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From products"
    result = cursor.execute(sorgu)

    if result > 0:
        products = cursor.fetchall()
        return render_template("products.html", products = products)
    else:
        return render_template("products.html")

# Add Product
@app.route("/addproduct",methods =["GET","POST"])
def addproduct():
    form = ProductForm(request.form)

    if request.method == "POST" and form.validate():
        title = form.title.data
        price = form.price.data
        content = form.content.data

        cursor = mysql.connection.cursor()
        sorgu = "Insert into products(title,author,price,content) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],price,content))
        mysql.connection.commit()
        cursor.close()

        flash("Ürün eklendi.", "success")
        return redirect(url_for("dashboard"))

    return render_template("addproduct.html", form = form)

# Product Form
class ProductForm(Form):
    title = StringField("Ürün Adı")
    price = IntegerField("Ürün Fiyatı")
    content = TextAreaField("Ürün Özellikleri")
    
# Detail 
@app.route("/product/<string:id>")
def product(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * From products where id = %s"
    result = cursor.execute(sorgu, (id,))

    if result > 0:
        product = cursor.fetchone()
        return render_template("product.html", product = product)
    else:
        return render_template("product.html")
    

if __name__ == "__main__":
    app.run(debug=True)