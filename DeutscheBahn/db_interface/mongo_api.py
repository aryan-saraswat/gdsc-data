from pymongo import MongoClient
from pprint import pprint

class MongoDb:

    def __init__(self, port=27017):
        self.client = MongoClient(port=port)
        self.db = self.client.gdsc_trains  #thesis_test is the name of the database where different collections are stored

    def clean_collection(self):
        result = self.db.cities.delete_many({})
        return result

    def get_all_cities(self):
        cities = self.db.cities.find({})
        result = [city for city in cities]
        return result

    def get_cities_by_name(self, city_name) -> list:
        cities = self.db.cities.find({"name":{"$regex": "^{}".format(city_name), "$options": "i"}}) # checking if an entry contains the name of a city, case-insensitive search
        result = [city for city in cities]
        return result