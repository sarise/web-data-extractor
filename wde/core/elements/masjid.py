from __future__ import absolute_import, division, print_function, unicode_literals

from collections import namedtuple
from enum import Enum


class Tipologi(Enum):
    NEGARA = 1
    RAYA = 2
    AGUNG = 3
    BESAR = 4
    JAMI = 5
    BERSEJARAH = 6
    PUBLIK = 7
    NASIONAL = 8

SDM = namedtuple('SDM', ['jamaah', 'imam', 'khatib', 'muazin', 'remaja'])

Details = namedtuple('Details', [
    'luas_tanah',
    'status_tanah',
    'luas_bangunan',
    'tahun_berdiri',
    'capacity',
    'contact',
    'facilities',
    'activities',
    'jumlah_pengurus',
])


class Masjid:

    daftar_kegiatan = {  # filtered >50
        'menyelenggarakan dakwah islam/tabliq akbar': 'k0',  # 119518
        'menyelenggarakan ibadah sholat fardhu': 'k1',  # 227615
        'menyelenggarakan kegiatan hari besar islam': 'k2',  # 194191
        'menyelenggarakan pengajian rutin': 'k3',  # 159177
        'menyelenggarakan sholat jumat': 'k4',  # 218927
        'menyelenggarakan kegiatan pendidikan (tpa/madrasah/pusat kegiatan belajar masyarakat)': 'k5',  # 115616
        'menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)': 'k6',  # 15482
        'penyembelihan hewan qurban': 'k7',  # 55
        'pemberdayaan zakat/infaq/shodaqoh dan wakaf': 'k8',  # 151421
    }

    daftar_fasilitas = {
        'aula serba guna': 'f0',  # 9866
        'gudang': 'f1',  # 91620
        'internet akses': 'f2',  # 1924
        'kipas angin': 'f3',  # 69
        'kamar mandi/wc': 'f4',  # 209492
        'kantor sekretariat': 'f5',  # 31636
        'kegiatan sosial': 'f6',  # 205
        'kegiatan sosial :': 'f7',  # 474
        'khitanan massal': 'f8',  # 174
        'koperasi': 'f9',  # 2366
        'lemari': 'f10',  # 65
        'mtq': 'f11',  # 146
        'mobil ambulance': 'f12',  # 1724
        'phbi': 'f13',  # 559
        'parkir': 'f14',  # 123424
        'pembangkit listrik/genset': 'f15',  # 133556
        'pengumpulan zakat fitrah': 'f16',  # 666
        'penyaluran qurban': 'f17',  # 655
        'penyejuk udara/ac': 'f18',  # 88045
        'perlengkapan pengurusan jenazah': 'f19',  # 89121
        'perpustakaan': 'f20',  # 18076
        'poliklinik': 'f21',  # 814
        'ruang belajar (tpa/madrasah)': 'f22',  # 69948
        'serambi': 'f23',  # 65
        'sarana ibadah': 'f24',  # 220940
        'sembahyang jenazah': 'f25',  # 490
        'sholat jenazah': 'f26',  # 79
        'sound system dan multimedia': 'f27',  # 189580
        'taman': 'f28',  # 43059
        'tempat penitipan sepatu/sandal': 'f29',  # 46264
        'tempat wudhu': 'f30',  # 229291
        'toko': 'f31',  # 1626
        'upacara perkawinan': 'f32',  # 445
    }

    def __init__(self, id_, name, url_id, address, provinsi, provinsi_id, kabupaten, kabupaten_id, kecamatan,
                 kecamatan_id, tipologi, tipologi_id, details):
        self.id_ = id_
        self.name = name
        self.url_id = url_id
        self.address = address
        self.provinsi = provinsi
        self.provinsi_id = provinsi_id
        self.kabupaten = kabupaten
        self.kabupaten_id = kabupaten_id
        self.kecamatan = kecamatan
        self.kecamatan_id = kecamatan_id
        self.tipologi = tipologi
        self.tipologi_id = tipologi_id

        assert isinstance(details, Details)
        self.luas_tanah = details.luas_tanah
        self.status_tanah = details.status_tanah
        self.luas_bangunan = details.luas_bangunan
        self.tahun_berdiri = details.tahun_berdiri
        self.capacity = details.capacity
        self.contact = details.contact
        self.jumlah_pengurus = details.jumlah_pengurus
        self.fasilities = details.facilities
        self.activities = details.activities

    def update_sdm(self, sdm):
        assert isinstance(sdm, SDM)
        self.jamaah = sdm.jamaah
        self.imam = sdm.imam
        self.khatib = sdm.khatib
        self.muazin = sdm.muazin
        self.remaja = sdm.remaja

    def to_dict(self):
        result = self.__dict__

        # Fasilitas
        flatten = self._flatten_list(self.daftar_fasilitas, result['fasilities'], 'f')
        result.update(flatten)
        del(result['fasilities'])

        # Kegiatan
        flatten = self._flatten_list(self.daftar_kegiatan, result['activities'], 'k')
        result.update(flatten)
        del(result['activities'])

        return result

    @staticmethod
    def _flatten_list(mapping, list_, leftover_key):
        list_ = list(map(str.lower, list_))
        flatten = {}
        for text, field in mapping.items():
            try:
                list_.remove(text)
                flatten[field] = 1
            except ValueError:
                flatten[field] = 0
        flatten[leftover_key] = list_
        return flatten
