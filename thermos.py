from flask import Flask,url_for,render_template,request
from logging import DEBUG
from datetime import datetime

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		name = 'erafeeque',
		datetime = datetime.utcnow() 
	))

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

@app.route('/add',methods=['GET','POST'])
def add():
	if request.method == 'POST':
		url = request.form['url']
		store_bookmark(url)
		app.logger.debug('Store URL: '+url)
	return render_template('add.html')
		# app.logger.debug('Store URL : '+ url )

# run the main applcation
if __name__ == '__main__':
	app.run(debug=True)