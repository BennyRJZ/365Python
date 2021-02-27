

import requests 
import pandas as pd


##### CONFIG

api_key = "#######LOL########"

url = "https://api.nasa.gov/neo/rest/v1/neo/browse/"

r = requests.get(url,{'api_key':api_key}) ### Request

r.status_code ### Verifiying the status of our request

response = r.json() 
response.keys() #### See the JSON Keys

data = response['near_earth_objects']

normalized = pd.json_normalize(data)

df = pd.DataFrame.from_dict(normalized)

print(df)