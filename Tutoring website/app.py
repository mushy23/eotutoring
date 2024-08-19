# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask import request, session, redirect, flash
from werkzeug import security
import random

#Mail imports
import flask_mail
from flask_mail import Mail, Message

# create the Flask app
from flask import Flask, render_template
app = Flask(__name__)

#Mail configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'giginator0271@gmail.com'
app.config['MAIL_PASSWORD'] = 'lrwkdblqtzkyqcoy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key= 'aimun'

mail = Mail(app)
app.run(debug=True)

@app.route('/')
def dashboard():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")
    
@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/message', methods = ['POST'])
def message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        msg = Message('New Client Inquiry for EO Tutoring', sender = 'EO Tutoring', recipients = ['mustafaarshad237@gmail.com'])
        msg.body = f'You have a new client inquiry:\nName: {name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}'
        mail.send(msg)
        flash("We will get back to you within the next 1-2 business days!", 'success')
        return redirect('/')