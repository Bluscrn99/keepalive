import time
import requests
import os

URL_TO_PING = os.environ.get('pingurl')

while True:
    try:
        requests.get(URL_TO_PING, timeout=5)
        print("Pinged Service A successfully")
    except Exception as e:
        print("Ping failed:", e)
    time.sleep(60)  # ping every minute
