from mongo_api import MongoDb
from pprint import pprint

db_instance = LsfInterface()

cities = db_instance.get_cities_by_name("aachen")
print(cities[0]['id'])

cities = db_instance.get_all_cities()
pprint(cities)