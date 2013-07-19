import requests
import json

api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"
offset = 25
url = "http://www.nytimes.com/2013/07/14/fashion/sex-on-campus-she-can-play-that-game-too.html"

@app.route('/commentsQuery')

def commentsQuery():
	global offset
	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)
	jsonResponse = f.json()
	f.close()
	i = 0 
	for comments in jsonResponse['results']['comments']:
		addresses = comments['location']
		print addresses

		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false")
		jsonLocations = response.json()

		coordinates = ""
		locationCoor = ""
		locationCoor += "[" + str(jsonLocations['results'][0]['geometry']['location']["lng"]) + ","
		locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lat"]) + "]"
		coordinates += locationCoor

		i = i + 1
		print i 

		if i > 5: # once the comments are greater than 10 (25), ask the NYTimes API for more 
			i = 0 # prepare i to be used again
			offset = offset + 25; # increments of 25, as per their API
			query() # call query() again
	return coordinates