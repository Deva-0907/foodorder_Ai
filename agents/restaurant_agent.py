import json


class RestaurantAgent:

    def check_menu(self):

        with open("database/menu.json", "r") as file:
            return json.load(file)