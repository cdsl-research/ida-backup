import requests
import json
from pprint import pprint
from datetime import datetime
import logging

def get_rps_current():
    url = "http://ida-loc:8089/stats/requests"
    res = requests.get(url)

    d = json.loads(res.text)
    return d["total_rps"]

def judge(rps):
    logging.basicConfig(filename='rps_copy_suspend.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    ths = 20.2
    if ths > rps:
        logging.info(f"under {ths} False")
        return False
    else:
        logging.info(f"over {ths} True")
        return True