import requests
import json
# from flask import Flask, render_template

# app = Flask(__name__)
api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"
offset = "25"
url = "http://www.nytimes.com/2013/07/14/fashion/sex-on-campus-she-can-play-that-game-too.html"
# @app.route("/")
# def index():
#     return render_template('compare.html')

# @app.route('/query')

# def query():
    # Get the json by making an API call to the Times
f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + offset + "&url=" + url + "&api-key=" + api_key)
    # Store Python library into 'jsonResponse' to be fed to compare.html
jsonResponse = f.json()
#j = json.loads(jsonResponse)

f.close()

i = 0

for comments in jsonResponse['results']['comments']:
	addresses = comments['location']
	print addresses

	for a in addresses:
		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + a + "&sensor=false")
		jsonLocations = response.json()

		coordinates = "["
		locationCoor = ""
		locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lat"]) + ","
		locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lng"]) + "]"
		coordinates += locationCoor

		print coordinates

		i = i + 1

		coordinates += "]"

	#print address

#print jsonResponse

# if __name__ == "__main__":
#     app.run(port=8080, debug=True) 