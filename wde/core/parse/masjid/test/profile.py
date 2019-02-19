from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.parse.masjid.profile import (
    MASJID_PROFILE_URL,
    Parser,
)
from wde.core.utils.io import (
    get_content,
    read_file,
)


def test_from_file1():
    expected = {
        "activities": [
            "Pemberdayaan Zakat",
            "Infaq",
            "Shodaqoh dan Wakaf",
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
        "jumlah_imam": 10,
        "jumlah_khatib": 10,
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
        "url_id": '275733',
    }

    c = read_file('wde/core/parse/masjid/test/html/masjid_profile.html')
    result = Parser.extract(c, url_id='275733')
    assert result.__dict__ == expected


def test_from_file2():
    expected = {
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
        "jumlah_imam": 3,
        "jumlah_khatib": 2,
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
        "url_id": None,
    }

    c = read_file('wde/core/parse/masjid/test/html/masjid_profile2.htm')
    result = Parser.extract(c, url_id=None)
    assert result.__dict__ == expected


def test_compare_online_and_downloaded():
    url_id = '19'

    local = read_file('wde/core/parse/masjid/test/html/masjid_profile.html')
    masjid1 = Parser.extract(local, url_id=url_id)

    online = get_content(MASJID_PROFILE_URL % url_id)
    masjid2 = Parser.extract(online, url_id=url_id)

    assert masjid1.__dict__ == masjid2.__dict__
