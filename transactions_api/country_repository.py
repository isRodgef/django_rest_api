import requests

class CountryWrapper():

    def __init__(self,url) -> None:
        r = requests.get(url)
        self.country_list = r.json() 
        pass

    def fetch_info(url):
        return {}
