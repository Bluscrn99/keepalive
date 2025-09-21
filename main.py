import time
import requests
import os

URL_TO_PING = os.environ.get('pingurl')

while True:
    try:
        requests.get(URL_TO_PING, timeout=5)
        print("Ping!")
    except Exception as e:
        print("Bonk. ", e)
    time.sleep(60)  # ping every minute
