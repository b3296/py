# -*- coding : utf-8 -*-
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST']) 
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
	return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return render_template('signin-ok.html',username=request.form['username'])
	return render_template('form.html',message='Bad username or password',username=request.form['username'])		
if __name__ == '__main__':
	app.run()			