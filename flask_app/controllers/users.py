from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.brain import Brain
from flask_app.models.cart import Cart
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

@app.route("/")
def brain():
    if 'user_id' not in session:
        return redirect('/createaccount')
    print(session)
    data = {
        'user_id':session['user_id']
    }
    user = User.get_user_info(data)
    print(user)
    return render_template("index.html", user=user)

@app.route("/buyModel")
def buymodel():
    brain = Brain.get_all()
    return render_template("buyModel.html", brain = brain)

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/aboutus")
def abus():
    return render_template("aboutus.html")

@app.route("/createaccount")
def createaccount():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
    #directs user to register page

@app.route('/create_user', methods = ['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],

            'password': pw_hash
    }
    session['first_name']= request.form['first_name']
    user_info = User.create_user(data)
    session['user_id'] = user_info
    return redirect('/')

@app.route('/login_user', methods=["POST"])
def login():
    user_in_db = User.get_user_info_login(request.form)
    if not user_in_db:
        return redirect('/createaccount')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/add_cart', methods= ["POST"])
def cart_route():
    data = {
            'user_id': session['user_id'],
            'brain_model_id': request.form['brain_model_id'],
            'quantity': request.form['quantity']
    }
    session['cart_id'] = data['brain_model_id']
    print(data['brain_model_id'])
    Cart.add_to_cart(data)
    return redirect('/cart')

@app.route('/show_user/<int:user_id>')
def user_info(user_id):
    data = {
        'user_id': user_id
    }
    user = User.get_user_info(data)
    print(user)
    return render_template('show_user.html', user = user)

@app.route('/edit_user/<int:user_id>')
def edit_page(user_id):
    data = {
        'user_id':user_id
    }
    edit_user = User.get_user_info(data)
    return render_template('edit_user.html', edit_user = edit_user) 

@app.route('/edit_user_info', methods= ['POST'])
def edit_user_info():
    edit_user_info = User.update_user_info()(request.form)
    return redirect('/')

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    data = {
        'user_id':user_id
    }
    dele = User.delete_user_info(data)
    session.clear()
    return redirect('/createaccount')

