from decimal import localcontext
from threading import local
import requests
import datetime

class CurrencyWrapper():

    def __init__(self,currency) -> None:
        url = "".join(["https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.", currency ,".EUR.SP00.A"])
        params = {
            'format': 'jsondata',
            'detail': 'dataonly',
            'updatedAfter': datetime.datetime.now().date()
        }
        r = requests.get(url, params)
        if r.status_code == 200:
            self.rate = r.json()['dataSets'][0]['series']['0:0:0:0:0']['observations']['0'][0]
        else:
            self.rate = 0

    def convert(self,value):
        return value * self.rate    


    def fetch_info(self, country):
        return self.country_list[country]


if __name__ == '__main__':
    c = CurrencyWrapper('NOK')
    print(c.rate)
