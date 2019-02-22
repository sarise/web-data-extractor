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


daftar_kegiatan = {
    'Pemberdayaan Zakat/Infaq/Shodaqoh dan Wakaf': 'k0',
    'Menyelenggarakan kegiatan pendidikan (TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)': 'k1',
    'Menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)': 'k2',
    'Menyelenggarakan Pengajian Rutin': 'k3',
    'Menyelenggarakan Dakwah Islam/Tabliq Akbar': 'k4',
    'Menyelenggarakan Kegiatan Hari Besar Islam': 'k5',
    'Menyelenggarakan Sholat Jumat': 'k6',
    'Menyelenggarakan Ibadah Sholat Fardhu': 'k7',
    '-': 'k8',
    'BAIK': 'k9',
    'Rusak Ringan': 'k10',
    'PENYEMBELIHAN HEWAN QURBAN': 'k11',
    'shedekah jumat': 'k12',
}

daftar_fasilitas = {
    'Internet Akses': 'f0',
    'Parkir': 'f1',
    'Taman': 'f2',
    'Gudang': 'f3',
    'Tempat Penitipan Sepatu/Sandal': 'f4',
    'Ruang Belajar (TPA/Madrasah)': 'f5',
    'Aula Serba Guna': 'f6',
    'Poliklinik': 'f7',
    'Koperasi': 'f8',
    'Perpustakaan': 'f9',
    'Kantor Sekretariat': 'f10',
    'Penyejuk Udara/AC': 'f11',
    'Sound System dan Multimedia': 'f11',
    'Pembangkit Listrik/Genset': 'f12',
    'Kamar Mandi/WC': 'f13',
    'Tempat Wudhu': 'f14',
    'Sarana Ibadah': 'f15',
    'Sarana Olah Raga': 'f16',
    'Lift bagi penyandang cacat': 'f17',
    'Perlengkapan Pengurusan Jenazah': 'f18',
    'Toko': 'f19',
    'Mobil Ambulance': 'f20',
    'CCTV': 'f21',
    '-': 'f22',
    'BAIK': 'f23',
}

class Masjid:
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
        flatten = self._flatten_list(daftar_fasilitas, result['fasilities'], 'f')
        result.update(flatten)
        del(result['fasilities'])

        # Kegiatan
        flatten = self._flatten_list(daftar_kegiatan, result['activities'], 'k')
        result.update(flatten)
        del(result['activities'])

        return result

    @staticmethod
    def _flatten_list(mapping, list_, leftover_key):
        flatten = {}
        for text, field in mapping.items():
            try:
                list_.remove(text)
                flatten[field] = 1
            except ValueError:
                flatten[field] = 0
        flatten[leftover_key] = list_
        return flatten
