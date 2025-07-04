# app/routes/main.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', title='Home', current_year=datetime.now().year)

@main.route('/about')
def about():
    return render_template('about.html', title='About', current_year=datetime.now().year)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically send an email or store the contact message
        # For now, we'll just flash a message
        flash(f'Thanks {name}, your message has been sent!', 'success')
        return redirect(url_for('main.contact'))
        
    return render_template('contact.html', title='Contact', current_year=datetime.now().year)

# # app/routes/main.py
# from flask import Blueprint, render_template

# main = Blueprint('main', __name__)

# @main.route('/')
# def home():
#     return render_template('home.html', title='Home')

# @main.route('/about')
# def about():
#     return render_template('about.html', title='About')

# @main.route('/contact')
# def contact():
#     return render_template('contact.html', title='Contact')