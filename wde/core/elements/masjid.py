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


class Masjid:
    def __init__(self, id_, name, url_id, address, provinsi, provinsi_id, kabupaten, kabupaten_id, kecamatan,
                 kecamatan_id, tipologi, tipologi_id, luas_tanah, status_tanah, luas_bangunan, tahun_berdiri, capacity,
                 contact, jumlah_pengurus, facilities, activities):
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
        self.luas_tanah = luas_tanah
        self.status_tanah = status_tanah
        self.luas_bangunan = luas_bangunan
        self.tahun_berdiri = tahun_berdiri
        self.capacity = capacity
        self.contact = contact
        self.jumlah_pengurus = jumlah_pengurus
        self.fasilities = facilities
        self.activities = activities

    def update_sdm(self, sdm):
        assert isinstance(sdm, SDM)
        self.jamaah = sdm.jamaah
        self.imam = sdm.imam
        self.khatib = sdm.khatib
        self.muazin = sdm.muazin
        self.remaja = sdm.remaja
