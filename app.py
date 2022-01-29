import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, usd

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.jinja_env.filters["usd"] = usd

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configuring sql
db = SQL("sqlite:///ecom.db")


@app.route("/")
@login_required
def index():
    """represents the main page where books are shown"""

    # check of any filters are passed in query string
    author = request.args.get("author")     
    genre = request.args.get("genre")
    age = request.args.get("age")

    # query books based on filters or get all books
    books = []
    if author:
        books = db.execute("SELECT * from books WHERE author = ?", author)
    elif genre:
        books = db.execute("SELECT * from books WHERE genres = ?", genre)
    elif age:
        books = db.execute("SELECT * from books WHERE minAge <= ?", age)
    else:
        books = db.execute("SELECT * FROM books")
    
    # populate side bar for filters
    authors = db.execute("SELECT DISTINCT author from books")
    genres = db.execute("SELECT DISTINCT genres from books")
    age = db.execute("SELECT DISTINCT minAge from books")

    return render_template("index.html", books=books, authors=authors, genres=genres, age=age)


@app.route("/login", methods=["GET", "POST"])
def login():                    
    """manages the login page"""

    session.clear()  # clear previous session if any

    if request.method == "POST":
        # ensuring that the username and password are not empty
        if not request.form.get("username"):
            return ("must provide username", 403) 
        elif not request.form.get("password"):
            return ("must provide password", 403)

        # checking if the username is already in use 
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return ("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]  # adding user to session
        session["cart"] = []            # set cart empty
        
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """ logs out the user """
    session.clear()

    return redirect("/")


@app.route("/about")
def about():
    """ display details about the project """
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Registering the user"""
    if request.method == "POST":

        # validate all reqired fields are entered
        username = request.form.get("username")
        if not username:
            return("must provide username", 400)
        elif not request.form.get("password"):
            return("must provide password", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return("password must be equal")

        # checking if username is already in use
        currentUsers = db.execute("SELECT * from users where username=?", username)
        if len(currentUsers) > 0:
            return("username already in use try another")

        hash = generate_password_hash(request.form.get("password"))  # generate hash value for password
        # get fields and insert into database
        country = request.form.get("country")
        city = request.form.get("city")
        state = request.form.get("state")
        address = request.form.get("address")
        user_db = db.execute("INSERT INTO users (username, hash ,country,state,city,address) VALUES (:username, :hash ,:country,:state,:city,:address)",
                             username=username, hash=hash, country=country, city=city, address=address, state=state)
        if not user_db:
            return("username already in use try another")

        session["user_id"] = user_db
        session["cart"] = []            # Set cart empty
        return redirect('/')

    else:
        return render_template("register.html")


@app.route("/details/<book_id>")
@login_required
def details(book_id=0):
    """ showing the details of the book """
    books = db.execute("SELECT * FROM books WHERE id = ?", book_id)
    series = []
    # checking if the selected book is a part of series
    if books[0]["series"]:
        series = db.execute("SELECT * FROM books WHERE series = ? AND id <> ?", books[0]["series"], books[0]["id"])
    return render_template("details.html", book=books[0], series=series)


@app.route("/yourAcc")
@login_required
def yourAcc(): 
    """ displaying the details of the user """
    id = session["user_id"]
    users = db.execute("SELECT * FROM users WHERE id = ?", id)
    print(users)
    return render_template("yourAcc.html", user=users[0])


@app.route("/cart", methods=["GET", "POST"])
@login_required
def viewCart():
    """ manages cart"""
    if request.method == "POST":
        cart = session.get("cart")
        if not cart:
            cart = []
            session["cart"] = cart
        
        bookid = request.form.get("bookid")
        books = db.execute("SELECT * FROM books WHERE id = ?", bookid)

        cart.append({'bookid': bookid, 'qty': 1, 'book': books[0]})

        session["cart"] = cart
        return redirect("/cart")
    else:
        return render_template("cart.html", items=session["cart"])


@app.route("/history")                      
@login_required
def history():
    """ shows the users order history """
    user_id = session["user_id"]
    items = db.execute("SELECT `time`, qty, order_items.price, `name`, `image` , order_id FROM order1 INNER JOIN order_items ON order1.id  = order_items.order_id INNER JOIN books ON books.id = order_items.book_id WHERE user_id = ?; ", user_id)
    return render_template("history.html", items=items)


@app.route("/checkout", methods=["POST"])
@login_required
def checkout():
    """ checking out the items which user added to cart """
    user_id = session["user_id"]
    
    totalAmount = 0
    cartItem = session["cart"]
    for item in cartItem:
        totalAmount += item["qty"] * item["book"]["price"]
    
    newOrderNum = 1     
    order_id = db.execute("INSERT INTO order1 (user_id, order_num, `time`, total_amt) VALUES (?,?,datetime(), ?)",
                          user_id, newOrderNum, totalAmount)

    for item in cartItem:
        book = item["book"]
        id2 = db.execute("INSERT INTO order_items (order_id, book_id, qty, price)  VALUES(?,?,?,?)",
                         order_id, book["id"], item["qty"], book["price"])
    
    session["cart"] = []

    return render_template("checkout.html", order_id=order_id) 