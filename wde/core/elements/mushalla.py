from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.elements.masjid import Masjid


class Mushalla(Masjid):

    daftar_fasilitas = {
        'alat-alat bolo pecah': 'f0',  # 44
        'alat-alat pecah belah': 'f1',  # 34
        'aula serba guna': '2',  # 1576
        'gudang': 'f3',  # 31732
        'halaman': 'f4',  # 24
        'internet akses': 'f5',  # 531
        'kipas angin': 'f6',  # 20
        'kamar mandi/wc': 'f7',  # 155050
        'kantor sekretariat': 'f8',  # 4717
        'kegiatan sosial :': 'f9',  # 44
        'kipas angin': 'f10',  # 93
        'koperasi': 'f11',  # 583
        'mimbar': 'f12',  # 19
        'mobil ambulance': 'f13',  # 217
        'parkir': 'f14',  # 58379
        'pembangkit listrik/genset': 'f15',  # 106679
        'pengumpulan zakat fitrah': 'f16',  # 41
        'penyaluran qurban': 'f17',  # 37
        'penyejuk udara/ac': 'f18',  # 61640
        'perlengkapan pengurusan jenazah': 'f19',  # 19544
        'perpustakaan': 'f20',  # 3182
        'poliklinik': 'f21',  # 225
        'ruang belajar (tpa/madrasah)': 'f22',  # 29129
        'sErambi': 'f23',  # 32
        'sarana ibadah': 'f24',  # 232206
        'sholat jenazah': 'f25',  # 29
        'sound system dan multimedia': 'f26',  # 163184
        'soundsystem': 'f27',  # 23
        'taman': 'f28',  # 13122
        'tempat penitipan sepatu/sandal': 'f29',  # 11081
        'tempat wudhu': 'f30',  # 234922
        'toko': 'f31',  # 357
        'upacara perkawinan': 'f32',  # 16
        'karpet': 'f33',  # 11
        'sound system': 'f34',  # 15
        'speaker': 'f35',  # 12
    }

    daftar_kegiatan = {  # filtered based on occurrence > 10
        'diba\'iyah': 'k0',  # 17
        'menyelenggarakan dakwah islam/tabliq akbar': 'k1',  # 42133
        'menyelenggarakan ibadah sholat fardhu': 'k2',  # 237979
        'menyelenggarakan kegiatan hari besar islam': 'k3',  # 105732
        'menyelenggarakan pengajian rutin': 'k4',  # 106332
        'menyelenggarakan sholat jumat': 'k5',  # 9687
        'menyelenggarakan sholat malam': 'k6',  # 14
        'menyelenggarakan kegiatan pendidikan (tpa/madrasah/pusat kegiatan belajar masyarakat)': 'k7',  # 67859
        'menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)': 'k8',  # 3826
        'papan nama musholla': 'k9',  # 24
        'pemberdayaan zakat/infaq/shodaqoh dan wakaf': 'k10',  # 67734
        'stempel musholla': 'k11',  # 13
        'tpq': 'k12',  # 110
        'upload foto mushala': 'k13',  # 18
        'pengajian': 'k14',  # 21
    }
