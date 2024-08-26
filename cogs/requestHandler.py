import json
import requests
import os
import dotenv
from dotenv import load_dotenv

dotenv.load_dotenv()

def getVersion() -> str:
    """Get the current bot version"""
    return os.getenv("VERSION")

HEADERS = {
    "User-Agent": "CombineBot/{version} (https://github.com/CombineSoldier14/CombineBot +combineemails14@gmail.com); python-requests/{requests}; curl/8.4.0".format(
        version=getVersion(),
        requests=requests.__version__
    ),
    "Accept": "application/json,text/plain,application/xml",
    "Upgrade-Insecure-Requests": "1",
    "Accept-Encoding": "gzip",
    "Connection": "close"
}

def get(url) -> requests.models.Response:
    return requests.get(url, headers=HEADERS)

def post(url, data) -> requests.models.Response:
    return requests.post(url, data, headers=HEADERS)
