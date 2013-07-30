from flask import jsonify, Flask, current_app
import requests
import json
import copy

offset = 0
coordinates = []
totalComments = 0

def query(url):
	global offset
	global coordinates

	api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"
	locationCoor = ""

	# remove any brackets from the url if they exist 
	if  url[0] == "<":
		url = url[1:-1]
		jsonResponse = []
		offset = 0

	print "http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key
	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)
	print f
	jsonResponse = f.json()
	f.close()

	totalComments = jsonResponse['results']['totalCommentsFound']

	for comments in jsonResponse['results']['comments']:
		addresses = comments['location']
		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses + "&sensor=false")

		jsonLocations = response.json()

		#print jsonLocations

		if jsonLocations['status'] == "OK":
			locationCoor = []
			locationCoor.append(jsonLocations['results'][0]['geometry']['location']["lng"])
			locationCoor.append(jsonLocations['results'][0]['geometry']['location']["lat"])
			coordinates.append(locationCoor)

	offset = offset + len(jsonResponse['results']['comments']); # increments of 25, as per their API
	print '\n'
	print offset

	if offset < totalComments: #if there are still comments left to be looked at
		query(url) # call query() again
	
	return jsonify(coordinates = coordinates)

body = []
def queryQuote(url):
	global body
	api_key = "3617242150835f8e3b987deb6b58d404:0:66946433"

	# remove any brackets from the url if they exist 
	if  url[0] == "<":
		url = url[1:-1]
		jsonResponse = []
		offset = 0

	print "http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key
	f = requests.get("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?offset=" + str(offset) + "&url=" + url + "&api-key=" + api_key)
	jsonResponse = f.json()
	f.close()

	totalComments = jsonResponse['results']['totalCommentsFound']

	for comments in jsonResponse['results']['comments']:
		print "whale"
		body.append(comments['commentBody'])


	print body

	return jsonify(comments = body)



