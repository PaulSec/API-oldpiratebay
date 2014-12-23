"""
This is the (unofficial) Python API for Old Pirate Bay

Using this code, you can retrieve the torrents you're looking for
by specifying the category + sort criteria you want.

By default, the script is looking in all categories, and does not use
a sort order.

"""
from bs4 import BeautifulSoup
import requests

url = "https://oldpiratebay.org"
categories = {'anime': 1,
            'software': 2,
            'games': 3,
            'adult': 4,
            'movies': 5,
            'music': 6,
            'other': 7,
            'series': 8,
            'books': 9}
sort = ['created_at', 'size', 'seeders', 'leechers']


class OldPirateBayAPI(object):
    """
        OldPirateBayAPI Main Handler
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
            __new__ builtin (Singleton)
        """
        if not cls._instance:
            cls._instance = super(OldPirateBayAPI, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def search(self, term, category='all', sort_criteria=None, asc=False):
        global url, categories, sort

        resource = "%s/search.php?q=%s" % (url, term)
        if (category != 'all'):
            resource = resource + "&iht=%s" % (categories[category])

        if (sort_criteria in sort):
            resource = resource + "&Torrent_sort=%s" % (sort_criteria)
            if (not asc):
                resource = resource + ".desc"

        req = requests.get(resource, verify=False)
        soup = BeautifulSoup(req.content)
        res = []
        for torrent in soup.findAll('tr'):
            try:
                date = torrent.find('td', attrs={'class': 'date-row'}).text
                size = torrent.find('td', attrs={'class': 'size-row'}).text
                seeders = torrent.find('td', attrs={'class': 'seeders-row'}).text
                leechers = torrent.find('td', attrs={'class': 'leechers-row'}).text
                magnet_link = torrent.find('a', attrs={'title': 'MAGNET LINK'})['href']
                link = "%s%s" % (url, torrent.findAll('a')[1]['href'])
                name = date = torrent.find('span').text
                t = {'date': date, 'size': size, 'seeders': seeders, 'leechers': leechers, 'magnet_link': magnet_link, 'name': name, 'link': link}
                res.append(t)
            except:
                pass
        return res
