from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # You can change this path to your preferred location

db = SQLAlchemy(app)

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Message('{self.name}', '{self.email}')"

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
        
        message = Message(name=name, email=email, message=message_text)
        db.session.add(message)
        db.session.commit()
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
