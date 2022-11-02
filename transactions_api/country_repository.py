from collections import defaultdict
from itertools import count    

from app.cache import function_cache

import requests

@function_cache.cache(ttl=10000)
def get_country_keys():
    url = "https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json"
    r = requests.get(url)
    return r.json()

class CountryWrapper():

    def __init__(self) -> None:
        

        country_list = get_country_keys()
        self.country_list = defaultdict(lambda : False)
        for json_data in country_list:
            self.country_list[json_data['Name'].lower()] = json_data['Code'].lower()


    def fetch_info(self, country):
        return self.country_list[country.lower()]
