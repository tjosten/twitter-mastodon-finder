# twitter-mastodon-finder
Finds Mastodon links in your Twitter followers descriptions.

## Get follower information

To to [here for followers](https://oauth-playground.glitch.me/?id=usersIdFollowers&params=%28%27user.fields%21%27description%27%29_) or [here for followings](https://oauth-playground.glitch.me/?id=usersIdFollowing&params=%28%27user.fields%21%27description%27%29_) and export the JSON data to a file named `data.json` saved in the same location as the python file in this repository.

Run `python3 finder.py` and get a list of all followers/followings with a Mastodon-like URL in their Twitter profile description.
