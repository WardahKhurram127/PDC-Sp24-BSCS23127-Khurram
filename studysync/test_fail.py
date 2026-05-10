import requests
import time

URL = "http://127.0.0.1:8000/generate?prompt=hello"

for i in range(15):
    try:
        r = requests.get(URL)
        print(f"Request {i+1}: ", r.json(), "Header:", r.headers.get("X-Student-ID"))
        time.sleep(0.5)
    except Exception as e:
        print("Request failed:", e)