from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from wde.core.parse.mushalla.profile import Parser
from wde.core.utils.io import (
    get_content,
    read_file,
)


mushalla1 = {
    "activities": [
        "Menyelenggarakan kegiatan pendidikan (TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)",
        "Menyelenggarakan Kegiatan Hari Besar Islam",
        "Menyelenggarakan Ibadah Sholat Fardhu"
    ],
    "address": "Jl. As-Adiyah Uloe Kec. Dua Boccoe Kab. Bone Sulawesi Selatan",
    "capacity": "",
    "contact": "",
    "fasilities": [
        "Parkir",
        "Kamar Mandi/WC",
        "Tempat Wudhu",
        "Sarana Ibadah"
    ],
    "id_": "02.3.26.08.19.000001",
    "jumlah_pengurus": "",
    "kabupaten": "KAB. BONE",
    "kabupaten_id": "391",
    "kecamatan": "DUA BOCCOE",
    "kecamatan_id": "5374",
    "luas_bangunan": "",
    "luas_tanah": "",
    "name": "MUSHALLA MTSS. AS-ADIYAH",
    "provinsi": "SULAWESI SELATAN",
    "provinsi_id": "26",
    "status_tanah": "Wakaf",
    "tahun_berdiri": "1990",
    "tipologi": "Mushalla Pendidikan",
    "tipologi_id": "",
    "url_id": "19"
}


@pytest.mark.parametrize('file_path, expected', [
    ('wde/core/parse/mushalla/test/html/mushalla_profile.html',     mushalla1),
])
def test_profile_downloaded(file_path, expected):
    c = read_file(file_path)
    result = Parser.extract(c, url_id='19')
    assert result.__dict__ == expected


def test_compare_online_and_downloaded():
    url_id = '19'

    local = read_file('wde/core/parse/mushalla/test/html/mushalla_profile.html')
    one = Parser.extract(local, url_id=url_id)

    online = get_content(Parser.construct_profile_url(url_id))
    two = Parser.extract(online, url_id=url_id)

    assert one.__dict__ == two.__dict__


@pytest.mark.parametrize('page_id, expected', [
    ('173156',      'http://simas.kemenag.go.id/index.php/profil/mushalla/173156/'),
    ('89028',       'http://simas.kemenag.go.id/index.php/profil/mushalla/89028/'),
])
def test_listing_construct_profile_url(page_id, expected):
    assert Parser.construct_profile_url(page_id) == expected
