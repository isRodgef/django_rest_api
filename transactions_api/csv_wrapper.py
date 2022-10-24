import csv
from transactions_api.models import TransactionModel
from transactions_api.serializers import TransactionSerializer
from datetime import datetime, timedelta

def validate(date_text):
    try:
        return datetime.strptime(date_text, '%Y/%m/%d')
    except ValueError:
        return None
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")

class CsvWrapper():
    
    def __init__(self):
        pass

    def create_list(self,filename):
        list_of_entries = []
        with open(filename) as file:
            reader = csv.reader(file)
            key_list = next(reader)
            #import code; code.interact(local=dict(globals(), **locals()))
            #reader = csv.DictReader(f, delimiter=",")
            try:
                for read in reader:
                    checked_date = validate(read[key_list.index('Date')])
                    if checked_date is None:  #will remove later 
                        continue
                    new_dict = {
                        'date': checked_date.strftime("%Y-%m-%d"),
                        'transaction_type': read[ key_list.index('Purchase/Sale')],
                        'country': read[key_list.index('Country')],
                        'currency': read[key_list.index('Currency')],
                        'net': read[key_list.index('Net')],
                        'vat': read[key_list.index('VAT')]
                    }


                    tmp = TransactionModel(
                        date=new_dict['date'],
                        transact_type = new_dict['transaction_type'],
                        country = new_dict['country'],
                        currency = new_dict['currency'],
                        net = new_dict['net'],
                        vat = new_dict['vat']
                    )

                    list_of_entries.append(tmp)
            except Exception as err:
                import traceback as tb
                import code; code.interact(local=dict(globals(), **locals()))
        return list_of_entries
