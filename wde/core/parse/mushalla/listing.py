from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.parse.masjid.listing import ListingParser as MasjidListingParser


MUSHALLA_LISTING_HOME_URL = 'http://simas.kemenag.go.id/index.php/profil/mushalla/page/'


class ListingParser(MasjidListingParser):

    listing_home_url = 'http://simas.kemenag.go.id/index.php/profil/mushalla/page/'
    listing_url = 'http://simas.kemenag.go.id/index.php/profil/mushalla/page/%s'
