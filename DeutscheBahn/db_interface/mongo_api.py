from pymongo import MongoClient
from pprint import pprint

class LsfInterface:

    def __init__(self, port=27017):
        self.client = MongoClient(port=port)
        self.db = self.client.gdsc_trains  #thesis_test is the name of the database where different collections are stored

    def clean_collection(self):
        result = self.db.cities.delete_many({})
        return result

    def find_cities_by_name(self, city_name) -> list:
        cities = self.db.cities.find({"name":{"$regex": "^{}".format(city_name), "$options": "i"}}) # checking if an entry contains the name of a city, case-insensitive search
        result = []
        for city in cities:
            result.append(city)
        return result