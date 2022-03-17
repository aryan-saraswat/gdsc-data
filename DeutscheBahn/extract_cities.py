import json, io, requests
from cities import cities

def clean_file(FILE):
    open(FILE, 'w').close()

def get_key():
    with io.open('config.json', 'r') as INPUT_FILE:
        config = json.load(INPUT_FILE)
        INPUT_FILE.close()
    return config['access-token']

def get_location(name: str) -> dict:
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(get_key()),
    }

    url = 'https://api.deutschebahn.com/fahrplan-plus/v1/location/{}'.format(name)

    response = requests.get(url=url, headers=headers)
    data = response.json()
    print('getting data for {}'.format(name))
    return data[0]

# get_location("Frankfurt")
def get_most_populous_cities():
    populous = [city for city in cities if city['einwohner'] > 79750]
    print(populous)

    ok_stations = []
    error_stations = []
    for city in populous:
        try:
            result = get_location(city['stadt'])
        except:
            error_stations.append(city)
            continue
        finally:
            ok_stations.append(result)

    return ok_stations

if __name__ == "__main__":
    OUTPUT_FILE = "db_cities.json"
    stations = get_most_populous_cities()
    clean_file(OUTPUT_FILE)

    with io.open(OUTPUT_FILE, 'w') as output:
        json.dump(stations, output)
        output.close()