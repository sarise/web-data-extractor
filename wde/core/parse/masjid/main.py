from __future__ import absolute_import, division, print_function, unicode_literals

import random
import time

from datetime import datetime
from multiprocessing.pool import Pool

from wde.core.parse.masjid.listing import ListingParser, MASJID_LISTING_HOME_URL
from wde.core.parse.masjid.profile import Parser
from wde.core.utils.io import get_content, write_json_to_file


def work(page_id):
    html = get_content(ListingParser.construct_listing_url(page_id))
    listing = ListingParser.extract(html)

    masjids = {}
    for masjid_url_id, sdm in listing.items():
        time.sleep(random.random())
        html = get_content(Parser.construct_profile_url(masjid_url_id))
        masjid = Parser.extract(html, masjid_url_id)
        if masjid:
            masjid.update_sdm(sdm)
            masjids[masjid_url_id] = masjid.__dict__

    return masjids


def main():
    html = get_content(MASJID_LISTING_HOME_URL)
    last_page_id = ListingParser.get_last_page_id(html)
    print(last_page_id)

    last_page_id = 5000
    print(last_page_id)

    page_ids = range(0, int(last_page_id), 10)
    page_ids = map(str, page_ids)

    with Pool(100) as p:
        records = p.map(work, page_ids)

    masjids = {}
    for record in records:
        masjids.update(record)

    file_name = 'masjids_%s_%d.json' % (
        datetime.now().strftime('%Y%m%d_%H%M%S'),
        len(masjids),
    )
    print(file_name)
    write_json_to_file(file_name, masjids)

if __name__ == '__main__':
    main()
