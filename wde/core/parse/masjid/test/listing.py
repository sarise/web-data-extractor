from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from wde.core.elements.masjid import SDM
from wde.core.parse.masjid.listing import (
    ListingParser,
    MASJID_LISTING_HOME_URL,
)
from wde.core.utils.io import (
    get_content,
    read_file,
)


def offline():
    return read_file('wde/core/parse/masjid/test/html/masjid_listing.html')


def online():
    return get_content(MASJID_LISTING_HOME_URL)


@pytest.mark.parametrize('source, expected', [
    (offline,     '250320'),
    (online,      '250320'),
])
def test_listing_get_last_page_id(source, expected):
    last_page_id = ListingParser.get_last_page_id(source())
    assert last_page_id == expected


@pytest.mark.parametrize('source', [
    offline,
    online,
])
def test_listing_extract(source):
    result = ListingParser.extract(source())
    assert len(result) == 10
    assert all([isinstance(sdm, SDM) for sdm in result.values()])
