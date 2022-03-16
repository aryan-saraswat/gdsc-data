import requests, io, json

url = "https://flixbus.p.rapidapi.com/v1/cities"
KEY_FILE = 'config.json'

def get_api_key():
    with io.open(KEY_FILE, 'r') as key_file:
        keys_json = json.load(key_file)
        key_file.close()
        return keys_json['x-rapidapi-key']

headers = {
    'x-rapidapi-host': "flixbus.p.rapidapi.com",
    'x-rapidapi-key': get_api_key()
    }

if __name__ == "__main__":
    response = requests.request("GET", url, headers=headers)

    with io.open('output.json', 'w') as output_file:
        output_file.write(response.text)
        output_file.close()