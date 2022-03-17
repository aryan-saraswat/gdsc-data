import json, io, requests
from cities import cities
import datetime
from db_interface.mongo_api import MongoDb

OUTPUT_FILE = 'journey_ids.json'
mongo = MongoDb()

def clean_file(FILE):
    open(FILE, 'w').close()

def get_key():
    with io.open('config.json', 'r') as INPUT_FILE:
        config = json.load(INPUT_FILE)
        INPUT_FILE.close()
    return config['access-token']

def get_journey_id_on_date(id, date):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(get_key()),
    }
    params = {
        "date": date
    }
    url = "https://api.deutschebahn.com/fahrplan-plus/v1/arrivalBoard/{}".format(id)

    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    clean_file(OUTPUT_FILE)
    date = datetime.date(2022,3,14)
    cities = mongo.get_all_cities()
    city_ids = [city['id'] for city in cities]
    journey_ids = set()
    error_journey_ids = set()

    for id in city_ids:
        arrivals = get_journey_id_on_date(id=id, date=date)
        print("getting journeys for id {}".format(id))

        for arrival in arrivals:
            # print(details)
            try:
                journey_ids.add(arrival['detailsId'])
            except:
                error_journey_ids.add(arrival)

    print(journey_ids)

    with io.open(OUTPUT_FILE, 'w') as output_file:
        json.dump(list(journey_ids), output_file)
        output_file.close()