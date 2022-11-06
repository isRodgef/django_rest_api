import csv
from transactions_api.models import TransactionModel
from transactions_api.serializers import TransactionSerializer
from datetime import datetime, timedelta

def validate(date_text):
    try:
        return datetime.strptime(date_text, '%Y/%m/%d')
    except ValueError:
        return None

class CsvWrapper():
    
    def __init__(self,serializer_class):
        self.serializer_class = serializer_class
        pass

    def create_list(self,filename):
        list_of_entries = []
        failed_entries = []
        with open(filename) as file:
            reader = csv.reader(file)
            key_list = next(reader)
            try:
                for read in reader:
                    checked_date = validate(read[key_list.index('Date')])
                    if checked_date is None:  #will remove later 
                        continue
                    str_date = checked_date.strftime("%Y-%m-%d")
                    tmp = {
                        'date': str_date ,
                        'transact_type': read[ key_list.index('Purchase/Sale')],
                        'country': read[key_list.index('Country')],
                        'currency': read[key_list.index('Currency')],
                        'net': read[key_list.index('Net')],
                        'vat': read[key_list.index('VAT')]
                    }
                    _serializer = self.serializer_class(data=tmp)
                    if _serializer.is_valid():
                        list_of_entries.append(_serializer.save(tmp))
                    else:
                        failed_entries.append(tmp)

            except Exception as err:
                failed_entries.append(tmp)
        return {"Successful" :list_of_entries, "Failed": failed_entries}
