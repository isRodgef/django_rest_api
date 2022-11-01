from decimal import localcontext
from threading import local
import requests
import datetime

class CurrencyWrapper():

    def __init__(self) -> None:
        self.rate = None 
        pass
    
    def get_rate(self,currency):
        self.url = "".join(["https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.", currency ,".EUR.SP00.A"])
        params = {
            'format': 'jsondata',
            'detail': 'dataonly',
            'updatedAfter': datetime.datetime.now().date()
        }
        r = requests.get(self.url, params)
        if r.status_code == 200:
            self.rate = r.json()['dataSets'][0]['series']['0:0:0:0:0']['observations']['0'][0]
        else:
            self.rate = 0
        return self.rate

    def convert(self,value):
        return value * self.rate    


if __name__ == '__main__':
    c = CurrencyWrapper.get_rate('NOK')
    print(c.rate)
