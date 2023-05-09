#!/usr/bin/python3
"""0-subs.py"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

