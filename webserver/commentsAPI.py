import requests
import json

offset = 0
coordinates = "["
totalComments = 0
def query(url):
	global offset
	global coordinates

	api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"
	locationCoor = ""

	# remove any brackets from the url if they exist 
	if  url[0] == "<":
		url = url[1:-1]

	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)
	jsonResponse = f.json()
	f.close()

	totalComments = jsonResponse['results']['totalCommentsFound']

	for comments in jsonResponse['results']['comments']:
		addresses = comments['location']
		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false")
		jsonLocations = response.json()

		if jsonLocations['status'] == "OK":
			locationCoor = ""
			locationCoor += "[" + str(jsonLocations['results'][0]['geometry']['location']["lng"]) + ","
			locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lat"]) + "]"
			coordinates += locationCoor + ","

	offset = offset + len(jsonResponse['results']['comments']); # increments of 25, as per their API
	print offset
	print coordinates
	print "\n"

	if offset < totalComments: #if there are still comments left to be looked at
		query(url) # call query() again
	
	coordinates = coordinates[:-1] #removes last comma
	coordinates += ']' #adds a bracket
	
	return coordinates