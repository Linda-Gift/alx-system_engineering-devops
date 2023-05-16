#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "e1d7d6700d7a9d41be49ee187b6b8e9a"
api_app_key = "8ff34dd610461889b01e7b4db162b51d34385c36"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:154501-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
