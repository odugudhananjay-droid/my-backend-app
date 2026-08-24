from fastapi import FastAPI
import requests
import time

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Website Health Checker is running"
    }


@app.get("/check")
def check_website(url: str):

    start_time = time.time()

    try:
        response = requests.get(
            url,
            timeout=10
        )

        end_time = time.time()

        response_time = round(
            end_time - start_time,
            2
        )

        return {
            "url": url,
            "status": "UP",
            "status_code": response.status_code,
            "response_time": response_time
        }

    except requests.RequestException:

        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "response_time": None
        }