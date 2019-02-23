from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from wde.core.parse.masjid.profile import Parser
from wde.core.utils.io import (
    get_content,
    read_file,
)


masjid_istiqlal = {
    "activities": [
        "Pemberdayaan Zakat/Infaq/Shodaqoh dan Wakaf",
        "Menyelenggarakan kegiatan pendidikan (TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)",
        "Menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)",
        "Menyelenggarakan Pengajian Rutin",
        "Menyelenggarakan Dakwah Islam/Tabliq Akbar",
        "Menyelenggarakan Kegiatan Hari Besar Islam",
        "Menyelenggarakan Sholat Jumat",
        "Menyelenggarakan Ibadah Sholat Fardhu"
    ],
    "address": "Jl. Taman Wijaya Kusuma Rt.08/02, Kel. Pasar Baru, Kec. Sawah Besar, Jakarta Pusat",
    "capacity": "200.000",
    "contact": "021 3811708 / 021 3508903",
    "fasilities": [
        "Internet Akses",
        "Parkir",
        "Taman",
        "Gudang",
        "Tempat Penitipan Sepatu/Sandal",
        "Ruang Belajar (TPA/Madrasah)",
        "Aula Serba Guna",
        "Poliklinik",
        "Koperasi",
        "Perpustakaan",
        "Kantor Sekretariat",
        "Penyejuk Udara/AC",
        "Sound System dan Multimedia",
        "Pembangkit Listrik/Genset",
        "Kamar Mandi/WC",
        "Tempat Wudhu",
        "Sarana Ibadah",
        "Sarana Olah Raga",
        "Lift bagi penyandang cacat"
    ],
    "id_": "01.0.11.03.02.000001",
    "jumlah_pengurus": 20,
    "kabupaten": "KOTA ADM. JAKARTA PUSAT",
    "kabupaten_id": "152",
    "kecamatan": "SAWAH BESAR",
    "kecamatan_id": "1823",
    "luas_bangunan": 24200,
    "luas_tanah": 93200,
    "name": "MASJID ISTIQLAL",
    "provinsi": "DKI JAKARTA",
    "provinsi_id": "11",
    "status_tanah": "SHM",
    "tahun_berdiri": "1978",
    "tipologi": "Masjid Negara",
    "tipologi_id": "1",
    "url_id": None,
}

langgar = {
    "activities": [
        "Menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)",
        "Menyelenggarakan Pengajian Rutin",
        "Menyelenggarakan Dakwah Islam/Tabliq Akbar",
        "Menyelenggarakan Kegiatan Hari Besar Islam",
        "Menyelenggarakan Sholat Jumat",
        "Menyelenggarakan Ibadah Sholat Fardhu"
    ],
    "address": "DSN. SUKAMULYA DESA HUJUNGTIWU",
    "capacity": "150",
    "contact": "- / -",
    "fasilities": [
        "Parkir",
        "Taman",
        "Gudang",
        "Kamar Mandi/WC",
        "Tempat Wudhu",
        "Sarana Ibadah"
    ],
    "id_": "01.4.13.07.08.000106",
    "jumlah_pengurus": 10,
    "kabupaten": "KAB. CIAMIS",
    "kabupaten_id": "170",
    "kecamatan": "PANJALU",
    "kecamatan_id": "2250",
    "luas_bangunan": 120,
    "luas_tanah": 320,
    "name": "MASJID AL-HASANAH",
    "provinsi": "JAWA BARAT",
    "provinsi_id": "13",
    "status_tanah": "Wakaf",
    "tahun_berdiri": "1980",
    "tipologi": "Masjid Jami",
    "tipologi_id": "5",
    "url_id": None,
}


@pytest.mark.parametrize('file_path, expected', [
    ('wde/core/parse/masjid/test/html/masjid_profile.html',     masjid_istiqlal),
    ('wde/core/parse/masjid/test/html/masjid_profile2.htm',     langgar),
])
def test_profile_downloaded(file_path, expected):
    c = read_file(file_path)
    result = Parser.extract(c)
    assert result.__dict__ == expected


def test_compare_online_and_downloaded():
    url_id = '19'

    local = read_file('wde/core/parse/masjid/test/html/masjid_profile.html')
    masjid1 = Parser.extract(local, url_id=url_id)

    online = get_content(Parser.construct_profile_url(url_id))
    masjid2 = Parser.extract(online, url_id=url_id)

    assert masjid1.__dict__ == masjid2.__dict__


@pytest.mark.parametrize('page_id, expected', [
    ('173156',      'http://simas.kemenag.go.id/index.php/profil/masjid/173156/'),
    ('89028',       'http://simas.kemenag.go.id/index.php/profil/masjid/89028/'),
])
def test_listing_construct_profile_url(page_id, expected):
    assert Parser.construct_profile_url(page_id) == expected


# @pytest.mark.parametrize('url', [
#     'http://simas.kemenag.go.id/index.php/profil/masjid/173156/',
#     'http://simas.kemenag.go.id/index.php/profil/masjid/89028/',
# ])
# def test_profile_unknown(url):
#     online = get_content(url)
#     with pytest.raises(AttributeError):
#         Parser.extract(online, None)
