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