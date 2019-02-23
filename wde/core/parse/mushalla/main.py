from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.elements.mushalla import Mushalla
from wde.core.parse.common import (
    main as common_main,
    work as common_work,
)
from wde.core.parse.mushalla.listing import ListingParser
from wde.core.parse.mushalla.profile import Parser


def work(page_id):
    return common_work(page_id, listing_parser_cls=ListingParser, parser_cls=Parser)


def main():
    common_main(listing_parser_cls=ListingParser, element_cls=Mushalla, work_function=work)


if __name__ == '__main__':
    main()
