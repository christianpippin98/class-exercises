import datetime

class City:
    def __init__(self, city_name, mayor_name):
        self.city_name = city_name
        self.mayor_name = mayor_name
        self.date_established = ""
        self.buildings = list()

    def add_building(self, Building):
        self.buildings.append(Building)
        