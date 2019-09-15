from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello world!</h1>'

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/use')
def use():
	return render_template('use.html')
	
if __name__ == '__main__':
	app.run(debug=True)

