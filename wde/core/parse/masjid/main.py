from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.parse.masjid.listing import ListingParser, MASJID_LISTING_HOME_URL
from wde.core.parse.masjid.profile import Parser
from wde.core.utils.io import get_content


def work(page_id):
    html = get_content(ListingParser.construct_listing_url(page_id))
    listing = ListingParser.extract(html)

    masjids = {}
    for masjid_url_id, sdm in listing.items():
        html = get_content(Parser.construct_profile_url(masjid_url_id))
        masjid = Parser.extract(html, masjid_url_id)
        if masjid:
            masjid.update_sdm(sdm)
            masjids[masjid_url_id] = masjid

    return masjids


def main():
    print(work('0'))

    html = get_content(MASJID_LISTING_HOME_URL)
    last_page_id = ListingParser.get_last_page_id(html)
    print(last_page_id)

    print(work(last_page_id))

if __name__ == '__main__':
    main()
