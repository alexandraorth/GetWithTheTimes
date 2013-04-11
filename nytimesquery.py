from urllib import urlopen
import json

def searching(string):
    
    # Get a file-like object for the Python Web site's home page.
    f = urlopen("http://api.nytimes.com/svc/community/v2/comments/url/exact-match.json?url=" + string + "&api-key=3617242150835f8e3b987deb6b58d404:0:66946433")
    
    # Read from the object, storing the page's contents in 's'.
    
    jsonResponse = json.load(f)
   
    f.close()

    coordinates = "["

    i = 0

    for comments in jsonResponse['results']['comments']:

        address = comments['location']
        response = urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + address + "&sensor=true")
        jsonLocations = json.load(response)
        
        if jsonLocations['status'] == 'OK':
            locationCoor = ""

            locationCoor += "[" + str(jsonLocations['results'][0]['geometry']['location']["lat"]) + ","
            locationCoor += str(jsonLocations['results'][0]['geometry']['location']["lng"]) + "]"
            coordinates += locationCoor
            i = i + 1

    coordinates += "]"

    JSON = "{'type':'Locations','transform':{'scale':[0.032229964456445645,0.006392461796179619],'translate':[-176.6460306,7.367222]},'objects':{'coords':{'type':'MultiPoint','coordinates':"+coordinates+"}},'arcs'[]}"

    print JSON
    
    return JSON
