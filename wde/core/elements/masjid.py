from __future__ import absolute_import, division, print_function, unicode_literals

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


class Masjid:
    def __init__(self, id_, name, url_id, address, provinsi, kabupaten, kecamatan, tipologi,
                 luas_tanah, status_tanah, luas_bangunan, tahun_berdiri, capacity, contact,
                 jumlah_pengurus, jumlah_imam, jumlah_khatib, facilities, activities):
        self.id_ = id_
        self.name = name
        self.url_id = url_id
        self.address = address
        self.provinsi = provinsi
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.tipologi = tipologi
        self.luas_tanah = luas_tanah
        self.status_tanah = status_tanah
        self.luas_bangunan = luas_bangunan
        self.tahun_berdiri = tahun_berdiri
        self.capacity = capacity
        self.contact = contact
        self.jumlah_pengurus = jumlah_pengurus
        self.jumlah_imam = jumlah_imam
        self.jumlah_khatib = jumlah_khatib
        self.fasilities = facilities
        self.activities = activities
