#!/usr/bin/python3
"""A function that queries Reddit API and returns top ten hot post"""

import json
import requests
import sys

def top_ten(subreddit):
    """This func. takes one parameter"""
    subreddit = argv[1]

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
        else:
            print(None)