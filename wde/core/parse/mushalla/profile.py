from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.elements.mushalla import Mushalla
from wde.core.parse.masjid.profile import Parser as MasjidParser


class Parser(MasjidParser):

    profile_url = 'http://simas.kemenag.go.id/index.php/profil/mushalla/%s/'   # mushalla_id
    element_cls = Mushalla
