from flask import Flask, render_template, request, flash
import os
from config import PersonalInfo

app = Flask(__name__)
app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME', 'johncosenzo.com')
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
personal_info = PersonalInfo()

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/')
def index():
    return render_template('index.html', data=personal_info.get_data())

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically integrate with an email service
    # For now, we'll just flash a success message
    flash('Thank you for your message! I will get back to you soon.', 'success')
    return render_template('index.html', data=personal_info.get_data())
