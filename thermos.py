from flask import Flask,url_for,redirect,render_template,request,flash
from logging import DEBUG
from datetime import datetime

app = Flask(__name__)
app.logger.setLevel(DEBUG)

app.config["SECRET_KEY"]="\x99\x8bzoV\xe4S8\xc5W\x9e\x83aHq\xea\xc9\xf4\xbc\x96\xa7\xc5\xd9\x9d"

bookmarks = []

def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		name = 'erafeeque',
		datetime = datetime.utcnow() 
	))

def new_bookmarks(num):
	return sorted(bookmarks,key=lambda bm: bm['datetime'],reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',new_bookmarks=new_bookmarks(5))

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
		flash("The {} has been bookmark".format(url))
		return redirect(url_for('index'))
	return render_template('add.html')
		# app.logger.debug('Store URL : '+ url )

# run the main applcation
if __name__ == '__main__':
	app.run(debug=True)