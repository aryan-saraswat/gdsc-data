import io, json, requests

INPUT_FILE = 'journey_ids.json'
OUTPUT_FILE = 'journey_details.json'

def clean_file(FILE):
    open(FILE, 'w').close()

def get_key():
    with io.open('config.json', 'r') as INPUT_FILE:
        config = json.load(INPUT_FILE)
        INPUT_FILE.close()
    return config['access-token']

def get_journey_ids():
    with io.open(INPUT_FILE, 'r') as input:
        journey_ids = json.load(input)
        input.close()
    return journey_ids

def get_journey_details(journey_id):
    url = "https://api.deutschebahn.com/fahrplan-plus/v1/journeyDetails/{}".format(journey_id)
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(get_key()),
    }
    response = requests.get(url=url, headers=headers)
    data = response.json()
    return data

if __name__ == "__main__":
    clean_file(OUTPUT_FILE)
    journey_ids = get_journey_ids()
    print(len(journey_ids))
    trips = []
    for i in range(len(journey_ids)):
        id = str(journey_ids[i]).replace('%', '%25') # extra step, otherwise incompatible with DB API
        print("accessing journey id {} of {}".format(i, len(journey_ids)))
        trip = get_journey_details(id)
        trips.append(trip)

    with io.open(OUTPUT_FILE, 'w') as output:
        json.dump(trips, output)
        output.close()
