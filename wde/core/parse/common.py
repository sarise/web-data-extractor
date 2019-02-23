from __future__ import absolute_import, division, print_function, unicode_literals

import random
import time

from datetime import datetime
from multiprocessing.pool import Pool
from tqdm import tqdm

from wde.core.utils.io import (
    get_content,
    write_json_to_file,
    write_data_to_csv,
)


def work(page_id, listing_parser_cls, parser_cls):
    html = get_content(listing_parser_cls.construct_listing_url(page_id))
    if html is None:
        return {}

    listing = listing_parser_cls.extract(html)

    masjids = {}
    for masjid_url_id, sdm in listing.items():
        time.sleep(random.random())
        html = get_content(parser_cls.construct_profile_url(masjid_url_id))
        masjid = parser_cls.extract(html, masjid_url_id)
        if masjid:
            masjid.update_sdm(sdm)
            masjids[masjid_url_id] = masjid.to_dict()

    return masjids


def main(listing_parser_cls, element_cls, work_function):
    html = get_content(listing_parser_cls.listing_home_url)
    last_page_id = listing_parser_cls.get_last_page_id(html)
    print(last_page_id)

    last_page_id = 5000
    print(last_page_id)

    page_ids = range(0, int(last_page_id), 10)
    page_ids = list(map(str, page_ids))

    records = []
    with Pool(processes=200) as p:
        with tqdm(total=len(page_ids)) as progress_bar:
            for _, result in tqdm(enumerate(p.imap_unordered(work_function, page_ids))):
                progress_bar.update()
                records.append(result)

    output_dict = {}
    for record in records:
        output_dict.update(record)

    file_name = '%s_%s_%d' % (
        element_cls.__name__.lower(),
        datetime.now().strftime('%Y%m%d_%H%M%S'),
        len(output_dict),
    )
    print(file_name)
    write_json_to_file('%s.json' % file_name, output_dict)
    write_data_to_csv('%s.csv' % file_name, list(output_dict.values()))
    write_data_to_csv('%s_kegiatan.csv' % file_name, [element_cls.daftar_kegiatan])
    write_data_to_csv('%s_fasilitas.csv' % file_name, [element_cls.daftar_fasilitas])

    leftover_kegiatan = set()
    for masjid in output_dict.values():
        leftover_kegiatan.update(masjid['k'])
    print('k', leftover_kegiatan)

    leftover_fasilitas = set()
    for masjid in output_dict.values():
        leftover_fasilitas.update(masjid['f'])
    print('f', leftover_fasilitas)