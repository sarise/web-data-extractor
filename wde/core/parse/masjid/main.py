from __future__ import absolute_import, division, print_function, unicode_literals

import random
import time

from datetime import datetime
from multiprocessing.pool import Pool
from tqdm import tqdm

from wde.core.parse.masjid.listing import ListingParser, MASJID_LISTING_HOME_URL
from wde.core.parse.masjid.profile import Parser
from wde.core.utils.io import (
    get_content,
    write_json_to_file,
    write_data_to_csv,
)


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
    page_ids = list(map(str, page_ids))

    records = []
    with Pool(processes=100) as p:
        with tqdm(total=len(page_ids)) as progress_bar:
            for _, result in tqdm(enumerate(p.imap_unordered(work, page_ids))):
                progress_bar.update()
                records.append(result)

    masjids = {}
    for record in records:
        masjids.update(record)

    file_name = 'masjids_%s_%d' % (
        datetime.now().strftime('%Y%m%d_%H%M%S'),
        len(masjids),
    )
    print(file_name)
    write_json_to_file('%s.json' % file_name, masjids)
    write_data_to_csv('%s.csv' % file_name, list(masjids.values()))

if __name__ == '__main__':
    main()
