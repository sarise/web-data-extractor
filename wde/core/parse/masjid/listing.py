from __future__ import absolute_import, division, print_function, unicode_literals

from bs4 import BeautifulSoup

from wde.core.elements.masjid import SDM

MASJID_LISTING_HOME_URL = 'http://simas.kemenag.go.id/index.php/profil/masjid/page/'
MASJID_LISTING_URL = 'http://simas.kemenag.go.id/index.php/profil/masjid/page/%d'   # page id (multiple of 10)



class ListingParser:

    @classmethod
    def get_last_page_id(cls, content):
        soup = BeautifulSoup(content, 'html.parser')
        last_url = soup.find('div', class_='paging').findAll('a', href=True)[-1]['href']
        return cls._parse_paging_id_from_url(last_url)

    @classmethod
    def extract(cls, content):
        soup = BeautifulSoup(content, 'html.parser').find('div', class_='wrap')
        main_table = soup.find('table', class_='widefat border').find('tbody')
        results = {}
        for tr in main_table.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                masjid_url = tds[3].find('a', href=True)['href']
                masjid_id = cls._parse_masjid_id_from_url(masjid_url)
                jamaah = tds[11].text
                imam = tds[12].text
                khatib = tds[13].text
                muazin = tds[14].text
                remaja = tds[15].text
                results[masjid_id] = SDM(jamaah, imam, khatib, muazin, remaja)
        return results

    @classmethod
    def construct_listing_url(cls, page_id):
        return 'http://simas.kemenag.go.id/index.php/profil/masjid/page/%s' % page_id

    @classmethod
    def _parse_paging_id_from_url(cls, url):
        # Example: http://simas.kemenag.go.id/index.php/profil/masjid/page/250250
        return url.split('/')[-1]

    @classmethod
    def _parse_masjid_id_from_url(cls, url):
        # Example: http://simas.kemenag.go.id/index.php/profil/masjid/276353/
        return url.split('/')[-2]
