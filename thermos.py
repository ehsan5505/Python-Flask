from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/add')
def add():
	return render_template('add.html')

# run the main applcation
if __name__ == '__main__':
	app.run(debug=True)