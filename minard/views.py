from minard import app
from flask import render_template

@app.route('/')
def index():
    return render_template('layout.html',message='Hello World!')