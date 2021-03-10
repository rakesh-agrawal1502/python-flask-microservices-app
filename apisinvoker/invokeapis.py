import datetime
import schedule
import os
import time
import requests
from requests.exceptions import HTTPError

customer_url = os.getenv('CUSTOMER_SERVICE_URL')
invoice_url = os.getenv('INVOICE_SERVICE_URL')

if customer_url is None or invoice_url is None:
    print("Env variables are not defined")
    exit(1)


def call_apis():
    for url in [customer_url, invoice_url]:
        try:
            response = requests.get(url)
            print(response.text)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')


# call_apis()

now = datetime.datetime.now()
print("Calling APIs: %s" % now)
schedule.every(5).seconds.do(call_apis)

while 1:
    schedule.run_pending()
    time.sleep(5)
