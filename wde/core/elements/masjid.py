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
