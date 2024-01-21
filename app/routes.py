from flask import render_template, request, redirect, url_for
from app import app
from .detectors import detect_url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect():
    url = request.form.get('url')
    detect_url(url)
    return redirect(url)
