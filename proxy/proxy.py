import requests


class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        countries = []
        if object_instance.number % 2 == 0:
            response = requests.get("https://restcountries.eu/rest/v2/region/asia?fields=name")
        else:
            response = requests.get("https://restcountries.eu/rest/v2/region/europa?fields=name")
        return response.content
