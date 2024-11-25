from flask import Flask, render_template, request, flash
import os
from config import PersonalInfo

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"

# Only set SERVER_NAME in production
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SERVER_NAME'] = 'johncosenzo.com'

personal_info = PersonalInfo()

@app.route('/')
def index():
    return render_template('index.html', data=personal_info.get_data())

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    flash('Thank you for your message! I will get back to you soon.', 'success')
    return render_template('index.html', data=personal_info.get_data())
