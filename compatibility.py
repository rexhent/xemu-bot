# https://reports.xemu.app/compatibility

import json
import requests


try:
    response = requests.get('https://reports.xemu.app/compatibility')
    response.raise_for_status()

    data = response.json()

except requests.exceptions.RequestException as e:
    print("Error making the request:", e)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)


def find_by_id(json_data, target_id):
    for item in json_data:
        if item.get('_id') == target_id:
            return item
    return None


