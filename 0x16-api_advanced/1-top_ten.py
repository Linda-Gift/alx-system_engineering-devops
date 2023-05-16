#!/usr/bin/python3
"""A func. that queries Reddit API & returns top ten hot post"""
import requests


def top_ten(subreddit):
    """This func. prints 10 hottest posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
        else:
            print(None)
            return
