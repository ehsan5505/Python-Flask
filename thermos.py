from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html')

@app.route('/add')
def add():
	return render_template('add.html')

# run the main applcation
if __name__ == '__main__':
	app.run(debug=True)