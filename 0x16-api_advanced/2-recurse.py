#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests
import sys
after = None

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        if len(posts) == 0:
            return hot_list
        
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        new_after = data['data']['after']
        return recurse(subreddit, hot_list, new_after)
    else:
        return None

# Example usage
subreddit = "python"
result = recurse(subreddit)

if result is not None:
    for title in result:
        print(title)
else:
    print("None")
