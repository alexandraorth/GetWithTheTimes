import requests
import json
# from flask import Flask, render_template

# app = Flask(__name__)
api_key = "7fffaa70d16f04f4357c4b1d0b873090:17:66946433"
offset = "20"

# @app.route("/")
# def index():
#     return render_template('compare.html')

# @app.route('/query')

# def query():
    # Get the json by making an API call to the Times
f = requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?offset=" + offset + "&api-key=" + api_key)
    # Store Python library into 'jsonResponse' to be fed to compare.html
jsonResponse = f.json()

f.close()

for comments in jsonResponse:
	print comments
	

# if __name__ == "__main__":
#     app.run(port=8080, debug=True) 