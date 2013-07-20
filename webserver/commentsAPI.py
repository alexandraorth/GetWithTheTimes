import requests
import json

offset = 0
coordinates = []
def query(url):
	global offset
	global coordinates

	api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"

	print url + '\n'

	print "this is the first character in the url " + url[0]

	print str(offset) + "\n"

	# remove any brackets from the url if they exist 
	if  url[0] == "<":
		url = url[1:-1]

	print url + '\n'

	print "http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key + '\n\n'

	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)

	print "it is fucking cold"

	jsonResponse = f.json()
	f.close()
	print "THIS IS THE TOTAL NUMBER OF COMMENTS" + str(jsonResponse['results']['totalCommentsFound']) + '\n\n'
	totalComments = jsonResponse['results']['totalCommentsFound']
	i = 0 

	print "test OCTOPUS \n\n"

	for comments in jsonResponse['results']['comments']:
		print "test WHALE \n\n"
		addresses = comments['location']

		print 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false" + '\n\n'

		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(addresses).strip('[]') + "&sensor=false")

		print "test PORPOISE \n\n"

		jsonLocations = response.json()

		print "test STARFISH \n\n"

		if jsonLocations['status'] == "OK":
			locationCoor = ""
			locationCoor += "[" + str(jsonLocations['results'][0]['geometry']['location']["lng"]) + ","
			locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lat"]) + "]"
			coordinates.append(locationCoor)

		i = i + 1
		print i 
		print len(jsonResponse['results']['comments'])

		if i >= len(jsonResponse['results']['comments']): # once the comments are greater than 10 (25), ask the NYTimes API for more 
			i = 0 # prepare i to be used again
			print "made it into this IF STATEMEN"
			offset = offset + len(jsonResponse['results']['comments']); # increments of 25, as per their API
			print "offset: " + str(offset)
			print ""
			print coordinates
			if offset < totalComments: #if there are still comments left to be looked at
				print "this is the offset greater than totalCOmments if\n\n\n\n"
				query(url) # call query() again
			else:
				print "this is the else\n\n\n\n"
				return coordinates
				print "does this ever happen, will python allow it to happen"

	return coordinates