from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message_text = db.Column(db.Text, nullable=False)

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message_text = form.message.data
        
        new_message = Message(name=name, email=email, message_text=message_text)
        db.session.add(new_message)
        db.session.commit()

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('index'))
        
    flash("There was an error sending your message. Please check your inputs.", "error")
    return render_template('index.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
