from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from wde.core.parse.mushalla.listing import ListingParser
from wde.core.utils.io import (
    get_content,
    read_file,
)


def offline():
    return read_file('wde/core/parse/mushalla/test/html/mushalla_listing.html')


def online():
    return get_content(ListingParser.listing_home_url)


@pytest.mark.parametrize('source, expected', [
    (offline,     '279470'),
    (online,      '279470'),
])
def test_listing_get_last_page_id(source, expected):
    last_page_id = ListingParser.get_last_page_id(source())
    assert last_page_id == expected


@pytest.mark.parametrize('page_id, expected', [
    ('0',       'http://simas.kemenag.go.id/index.php/profil/mushalla/page/0'),
    ('33810',   'http://simas.kemenag.go.id/index.php/profil/mushalla/page/33810'),
    ('34400',   'http://simas.kemenag.go.id/index.php/profil/mushalla/page/34400'),
    ('41960',   'http://simas.kemenag.go.id/index.php/profil/mushalla/page/41960'),
])
def test_listing_construct_listing_url(page_id, expected):
    assert ListingParser.construct_listing_url(page_id) == expected
