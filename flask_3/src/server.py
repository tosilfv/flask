import requests
import random, datetime
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
QUOTE_URL = 'https://zenquotes.io/api/random'
app.secret_key = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 123
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
mail = Mail(app)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', rand_num = random_number, \
                           cur_y=current_year)

@app.route('/quotes')
def home():
    current_year = datetime.now().year
    res = requests.get(QUOTE_URL)
    res_json = res.json()
    return render_template('index.html', cur_y=current_year, \
                            quote_q=res_json[0]['q'], \
                            quote_a=res_json[0]['a'])

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = Message('New Message from Contact Form',
                  sender='your_email@gmail.com',
                  recipients=['recipient@example.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    mail.send(msg)
    
    flash('Email sent successfully!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
