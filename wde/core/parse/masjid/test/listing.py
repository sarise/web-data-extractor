from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from wde.core.elements.masjid import SDM
from wde.core.parse.masjid.listing import ListingParser
from wde.core.utils.io import (
    get_content,
    read_file,
)


def offline():
    return read_file('wde/core/parse/masjid/test/html/masjid_listing.html')


def online():
    return get_content(ListingParser.listing_home_url)


@pytest.mark.parametrize('source, expected', [
    (offline,     '250320'),
    (online,      '250510'),
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


@pytest.mark.parametrize('url', [
    'http://simas.kemenag.go.id/index.php/profil/masjid/page/33810',
    'http://simas.kemenag.go.id/index.php/profil/masjid/page/34400',
    'http://simas.kemenag.go.id/index.php/profil/masjid/page/41960',
])
def test_listing_unicode(url):
    source = get_content(url)
    result = ListingParser.extract(source)
    assert len(result) == 10
    assert all([isinstance(sdm, SDM) for sdm in result.values()])


@pytest.mark.parametrize('page_id, expected', [
    ('0',       'http://simas.kemenag.go.id/index.php/profil/masjid/page/0'),
    ('33810',   'http://simas.kemenag.go.id/index.php/profil/masjid/page/33810'),
    ('34400',   'http://simas.kemenag.go.id/index.php/profil/masjid/page/34400'),
    ('41960',   'http://simas.kemenag.go.id/index.php/profil/masjid/page/41960'),
])
def test_listing_construct_listing_url(page_id, expected):
    assert ListingParser.construct_listing_url(page_id) == expected
