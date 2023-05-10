#!/usr/bin/python3
"""A function that queries Reddit API and returns num. of subs"""

import requests

def number_of_subscribers(subreddit):
    """This func. takes one parameter"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Custom User Agent"
    }

    response = requests.get(url, headers = headers, allow_redirections=False)
    if response.status_code == 200:
        return 0
    data = response.json()['data']['subscribers']
    return data.get('subscribers')
