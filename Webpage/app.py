from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key'  # This key is essential for form protection in Flask-WTF. In production, use a more secure key and store it safely.

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
        message = form.message.data
        
        # You can now use these variables to store in the database, send an email, etc.
        
        return redirect('/')  # Redirecting the user back to the homepage or perhaps a 'thank you' page

    return render_template('index.html', form=form)  # Return the form with errors (if any)

if __name__ == '__main__':
    app.run(debug=True)
