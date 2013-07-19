import requests
import json

offset = 0
coordinates = []
def query(url):
	global offset
	global coordinates

	api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"

	print "http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key

	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)
	jsonResponse = f.json()
	f.close()
	i = 0 

	for comments in jsonResponse['results']['comments']:
		addresses = comments['location']
		print 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false"

		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false")
		jsonLocations = response.json()

		if jsonLocations['status'] == "OK":
			locationCoor = ""
			locationCoor += "[" + str(jsonLocations['results'][0]['geometry']['location']["lng"]) + ","
			locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lat"]) + "]"
			coordinates.append(locationCoor)

		i = i + 1
		print i 

		if i > 24: # once the comments are greater than 10 (25), ask the NYTimes API for more 
			i = 0 # prepare i to be used again
			offset = offset + 25; # increments of 25, as per their API
			print "offset: " + str(offset)
			print ""
			print coordinates
			query(url) # call query() again

	return coordinates