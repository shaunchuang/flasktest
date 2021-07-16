# Home page route
from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    course = {'id':'BDSE'}
    return render_template('index.html',title='Group2',course=course)

