#!/usr/bin/python3
"""A function that queries Reddit API and returns num. of subs"""

import requests
import sys

def number_of_subscribers(subreddit):
    """This func. takes one parameter"""
    subreddit = sys.argv[1];

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirs=False)
    if response.status_code == 200:
        data = response.json()['data']['subscribers']
