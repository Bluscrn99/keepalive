import time
import requests
import os
import threading

URL_TO_PING = os.environ.get('pingurl')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Dummy web server"

@app.route("/ping")
def ping():
    print("Pong!")
    return "Pong!", 200

def ping():
    print("Ping init")
    while True:
        try:
            requests.get(URL_TO_PING, timeout=5)
            print("Ping!")
        except Exception as e:
            print("Bonk. ", e)
        time.sleep(60)  # ping every minute
# run em
if __name__ == "__main__":
    print("Threading init")
    threading.Thread(target=ping, daemon=True).start()
    # Run Flask web server on the port Render expects
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
