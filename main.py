import requests
from pprint import pprint
import time

def get_request(tag):
    todate = int(time.time())
    fromdate = todate - 172800
    url = f"https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow"
    resp = requests.get(url)
    return resp.json()


if __name__ == '__main__':
    pprint(get_request('python'))


