#import modules
import requests
import json 

#fetch the data with get request
data = requests.get("https://www.affirmations.dev/")
status_code = data.status_code

#check the status code to ensure request was successful
if(status_code == 200):
    #parse the data and display the data
    result = data.json()
    print(json.dumps(result["affirmation"]))
