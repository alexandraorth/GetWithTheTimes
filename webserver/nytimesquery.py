#!/usr/bin/python
#!/usr/bin/env python
import requests
import json
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    # Get the json by making an API call to the Times 
    f = requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/1.json?api-key=7fffaa70d16f04f4357c4b1d0b873090:17:66946433")
    # Store Python library into 'jsonResponse' to be fed to index.html
    jsonResponse = f.text
    f.close()
    return jsonResponse

@app.route('/compare/<path:urlPath>')
def compare(urlPath):
	return render_template('compare.html', url=urlPath)

if __name__ == "__main__":
    app.run(port=8080, debug=True)    