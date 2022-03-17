from mongo_api import LsfInterface

db_instance = LsfInterface()

cities = db_instance.find_cities_by_name("aachen")
print(cities[0]['id'])