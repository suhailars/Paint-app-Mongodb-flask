from flask import *
from flask.ext.pymongo import PyMongo 
import json

app = Flask(__name__)
mongo = PyMongo(app)

from pymongo import Connection  
connection = Connection() 
db = connection.test_database
collection = db.test_collection

@app.route('/')
def home():
	return render_template('paintnew.html')

@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	posts = [db.posts.find_one({"title": filename})]
        print posts
	return render_template('picload.html',posts=posts)


@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	post = { "title": request.form['name'], "imagedata":request.form['data'] }
        posts = db.posts
        posts.insert(post)
	return render_template('paintnew.html')

@app.route('/gallery')

def gallery():
	posts = db.posts.find().sort("_id")	
	return render_template('gallery.html',posts=posts)

app.run(debug = True)

