import requests                 ## Importing the Library that will allow us to make the requests
from keys import ameritrade     ## Importing our API key
url = 'https://api.tdameritrade.com/v1/instruments'

## Payload to make the request
payload = {
    'apikey':ameritrade,        ## Apikey previously imported
    'symbol':'GOOG',            ## The stock that we want to get
    'projection':'fundamental'  ## The information that we want to get about the stock
}

results = requests.get(url,params=payload)   ## config of our request


print("Your API Key",ameritrade) 
print(results.status_code)                    ## Showing the status of our request
print(results.json())                         ## Showing our request in a json format