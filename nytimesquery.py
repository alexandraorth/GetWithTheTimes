import urllib2
import json
def query():	
    # Get the json by making an API call to the Times 
    f = urllib2.urlopen();
    # Store Python library into 'jsonResponse' to be fed to index.html
    jsonResponse = json.load(f)
    f.close()

    #print jsonResponse #for debugging purposes
    return jsonResponse
