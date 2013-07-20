#!/usr/bin/python
#!/usr/bin/env python

#import scripts
from flask import Flask, render_template
import requests
import json

#import local scripts
import articlesAPI
import commentsAPI


app = Flask(__name__)

# main route, on localhost renders index
@app.route("/")
def index():
    return render_template('index.html')

#returns about NYTimes most popular articles
@app.route('/queryArticles')
def queryArticles():
	return articlesAPI.query()

#returns info from NYTimes articles' comments
@app.route('/queryComments/<path:urlPath>')
def queryComments(urlPath):
	return commentsAPI.query(urlPath)

#routes to compare page
@app.route('/compare/<path:urlPath>')
def compare(urlPath):
	return render_template('compare.html', url=urlPath)

if __name__ == "__main__":
    app.run(port=8080, debug=True)    