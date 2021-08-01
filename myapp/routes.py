# Home page route
from flask import render_template, request
from myapp import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    course = {'id': 'BDSE'}
    lessons = [{'code': 'J001', 'name': 'Java Programming'},
               {'code': 'D002', 'name': 'Data Analysis using Python'}]
    if request.method == 'POST':
        if request.form['submit_button'] == 'do':
            return render_template('button2.html')
        elif request.form['submit_button'] == 'nomore':
            return render_template('button1.html')
    return render_template('index.html', title='Group2', course=course, lessons=lessons)
