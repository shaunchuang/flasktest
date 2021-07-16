# Home page route
from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    course = {'id':'BDSE'}
    lessons = [{'code':'J001','name':'Java Programming'},
                {'code':'D002','name':'Data Analysis using Python'}]
    return render_template('index.html',title='Group2',course=course, lessons=lessons)

