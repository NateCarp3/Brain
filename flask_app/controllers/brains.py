from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.brain import Brain
from flask_app.models.user import User
from flask_app.models.cart import Cart



@app.route('/add_brain', methods=['POST'])
def show():
    if not Brain.validate_brain(request.form):
        return redirect('/buyModel')
    brain = Brain.add_brain(request.form)
    return redirect('/cart')

@app.route('/cart')
def cart():
    if "user_id" not in session:
        return redirect('/createaccount')
    data = {
        'user_id': session['user_id'],
}
    cart = Cart.get_cart_info(data)
    print(cart)
    return render_template('cart.html', cart = cart)

@app.route('/delete/<int:brain_model_id>')
def delete_brain(brain_model_id):
    if "cart_id" not in session:
        return redirect('/buymodel')
    data = {
        'user_id': session['user_id'],
        'brain_model_id': brain_model_id
    }
    delete_brain = Cart.delete_brain(data)
    return redirect('/cart')
