from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically integrate with an email service
    # For now, we'll just flash a success message
    flash('Thank you for your message! I will get back to you soon.', 'success')
    return render_template('index.html')
