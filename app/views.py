from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user ={'name':'Amir','age':'26','class':'RTU'}
	return render_template('index.html',
	user=user)