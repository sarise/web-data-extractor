from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.elements.masjid import Masjid
from wde.core.parse.common import (
    main as common_main,
    work as common_work,
)
from wde.core.parse.masjid.listing import ListingParser
from wde.core.parse.masjid.profile import Parser


def work(page_id):
    return common_work(page_id, listing_parser_cls=ListingParser, parser_cls=Parser)


def main():
    common_main(listing_parser_cls=ListingParser, element_cls=Masjid, work_function=work)
