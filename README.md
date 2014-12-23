API-oldpiratebay
================

(Unofficial) Python API for Old Pirate Bay that I developed in few mins. 
There might be some bugs, report them, and I'll fix them as soon as possible. 

Feel free to clone/fork the repo, do Pull Requests..

Looking for a specific feature? Ping me or do it and integrate it as a PR.

Installation
================

Easy. Install *pip*, then run: 

```pip install -r requirements.txt```

Then:

```python APIexample.py```

How to use it?
================

Feel free to check *APIexample.py* file, but otherwise, here is the source code:

```python
from oldpiratebayAPI import OldPirateBayAPI


def print_torrents(torrents):
    for torrent in torrents:
        print "%s %s/%s" % (torrent['name'], torrent['seeders'], torrent['leechers'])

# Looking for the term 'pirate'
torrents = OldPirateBayAPI().search('pirate')
print_torrents(torrents)

# Looking in 'movies' and sorting by 'seeders'
torrents = OldPirateBayAPI().search('pirate', 'movies', 'seeders')
print_torrents(torrents)

# Same search but sorting descending
torrents = OldPirateBayAPI().search('pirate', 'movies', 'seeders', True)
print_torrents(torrents)
```

