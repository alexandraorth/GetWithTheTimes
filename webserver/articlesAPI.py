#!/usr/bin/python
#!/usr/bin/env python
import requests
import json

def query():
    # Get the json by making an API call to the Times 
    f = requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=7fffaa70d16f04f4357c4b1d0b873090:17:66946433")
    # Store Python library into 'jsonResponse' to be fed to index.html
    jsonResponse = f.text
    f.close()
    return jsonResponse

