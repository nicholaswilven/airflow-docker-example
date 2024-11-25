import logging
logger = logging.getLogger("Main")
from dotenv import load_dotenv
load_dotenv(".env")
import os
api_username = os.getenv("API_USERNAME")
api_password = os.getenv("API_PASSWORD")
import requests
from requests.auth import HTTPBasicAuth
TEST_URL = f"http://10.8.0.19:6001"

TELEGRAM_AUTHTOKEN = os.getenv('TELEGRAM_AUTHTOKEN')
TELEGRAM_ENDPOINT = os.getenv('TELEGRAM_ENDPOINT')
TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')

# Define header
headers = {"Authorization": f"Basic {TELEGRAM_AUTHTOKEN}"}

import time
import json
import pandas as pd
def test_apis(output_path):
    df = pd.read_csv(output_path).columns
    data = requests.get(TEST_URL, auth = HTTPBasicAuth(api_username, api_password))
    assert data.status_code == 200
    
    # Define request body
    request_body = {
        "chat_id": TELEGRAM_CHATID,
        "text": f"Testing Airflow Pipeline:\n{df}\n{json.dumps(data.json())}"
    }
    # Set maximum tolerance to 5 trial
    max_tolerance = 5
    success = False
    while not success:
        if max_tolerance > 0:
            try:
                resp = requests.post(
                    url = TELEGRAM_ENDPOINT,
                    headers = headers,
                    json = request_body
                )
                assert resp.status_code == 200
                logger.info(f'Successfully hit telegram notifier using POST method with status code {resp.status_code}')
                success = True
            except Exception as e:
                logger.error(f'Failed to hit telegram notifier using POST method with status code {resp.status_code}')
                max_tolerance -= 1
                time.sleep(5)
        else:
            break