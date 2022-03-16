import requests
import io
import json

url = "https://airhob-api.p.rapidapi.com/sandboxapi/flights/v1.1/search"
KEY_FILE = 'config.json'

payload = '''{\r
    \"TripType\": \"O\",\r
    \"NoOfAdults\": 1,\r
    \"NoOfChilds\": 0,\r
    \"NoOfInfants\": 0,\r
    \"ClassType\": \"Economy\",\r
    \"OriginDestination\": [\r
        {\r
            \"Origin\": \"JFK\",\r
            \"Destination\": \"SFO\",\r
            \"TravelDate\": \"07/14/2017\"\r
        }\r
    ]\r
}'''

payloadjson = {
    "TripType": "0",
    "NoOfAdults": 1,
    "NoOfChilds": 0,
    "NoOfInfants": 0,
    "ClassType": "Economy",
    "OriginDestination": [
        {
            "Origin": "JFK",
            "Destination": "SFO",
            "TravelDate": "07/14/2017"
        }
    ]
}

def get_api_key():
    with io.open(KEY_FILE, 'r') as key_file:
        keys_json = json.load(key_file)
        key_file.close()
        return keys_json['x-rapidapi-key']

headers = {
    'content-type': "application/json",
    'mode': "sandbox",
    'apikey': "<REQUIRED>",
    'accept-encoding': "gzip, deflate",
    'x-rapidapi-host': "airhob-api.p.rapidapi.com",
    'x-rapidapi-key': get_api_key()
    }

if __name__ == "__main__":
    response = requests.request("POST", url, data=payloadjson, headers=headers)
    print(response.text)