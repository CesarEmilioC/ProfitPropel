from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    messages.append({
        'name': name,
        'email': email,
        'message': message
    })
    
    return 'Thank you for your message!'

if __name__ == '__main__':
    app.run(debug=True)
