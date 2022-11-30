#!/usr/bin/python

import json
import re
import os
import sys

# Get data.json from Twitter for 
# Followers: https://oauth-playground.glitch.me/?id=usersIdFollowers&params=%28%27user.fields%21%27description%27%29_
# Followings: https://oauth-playground.glitch.me/?id=usersIdFollowing&params=%28%27user.fields%21%27description%27%29_

with open(os.path.join(sys.path[0], "data.json"), "r") as fileData:
    jsonData = json.load(fileData)

    mastodonUrlRegex = re.compile(r'@\w*@\w*\.\w*')
    webUrlRegex = re.compile(r'http(s?)://.*/@\w*')

    for follower in jsonData['data']:
        name = follower['name']
        username = follower['username']
        description = follower['description']

        match1 = mastodonUrlRegex.search(description)
        if match1:
            print("%s (@%s) - %s" % (name, username, match1.group()))

        match2 = webUrlRegex.search(description)
        if match2:
            print("%s (@%s) - %s" % (name, username, match2.group()))
