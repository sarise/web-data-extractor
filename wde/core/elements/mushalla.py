from __future__ import absolute_import, division, print_function, unicode_literals

from wde.core.elements.masjid import Masjid


class Mushalla(Masjid):

    daftar_fasilitas = {
        'Alat-alat Bolo Pecah': 'f0',  # 44
        'Alat-alat pecah belah': 'f1',  # 34
        'Aula Serba Guna': '2',  # 1576
        'Gudang': 'f3',  # 31732
        'HALAMAN': 'f4',  # 24
        'Internet Akses': 'f5',  # 531
        'KIPAS ANGIN': 'f6',  # 20
        'Kamar Mandi/WC': 'f7',  # 155050
        'Kantor Sekretariat': 'f8',  # 4717
        'Kegiatan Sosial :': 'f9',  # 44
        'Kipas Angin': 'f10',  # 93
        'Koperasi': 'f11',  # 583
        'Mimbar': 'f12',  # 19
        'Mobil Ambulance': 'f13',  # 217
        'Parkir': 'f14',  # 58379
        'Pembangkit Listrik/Genset': 'f15',  # 106679
        'Pengumpulan Zakat Fitrah': 'f16',  # 41
        'Penyaluran Qurban': 'f17',  # 37
        'Penyejuk Udara/AC': 'f18',  # 61640
        'Perlengkapan Pengurusan Jenazah': 'f19',  # 19544
        'Perpustakaan': 'f20',  # 3182
        'Poliklinik': 'f21',  # 225
        'Ruang Belajar (TPA/Madrasah)': 'f22',  # 29129
        'SERAMBI': 'f23',  # 32
        'Sarana Ibadah': 'f24',  # 232206
        'Sholat Jenazah': 'f25',  # 29
        'Sound System dan Multimedia': 'f26',  # 163184
        'Soundsystem': 'f27',  # 23
        'Taman': 'f28',  # 13122
        'Tempat Penitipan Sepatu/Sandal': 'f29',  # 11081
        'Tempat Wudhu': 'f30',  # 234922
        'Toko': 'f31',  # 357
        'Upacara Perkawinan': 'f32',  # 16
        'karpet': 'f33',  # 11
        'sound system': 'f34',  # 15
        'speaker': 'f35',  # 12
    }

    daftar_kegiatan = {  # Filtered based on occurrence > 10
        'Diba\'iyah': 'k0',  # 17
        'Menyelenggarakan Dakwah Islam/Tabliq Akbar': 'k1',  # 42133
        'Menyelenggarakan Ibadah Sholat Fardhu': 'k2',  # 237979
        'Menyelenggarakan Kegiatan Hari Besar Islam': 'k3',  # 105732
        'Menyelenggarakan Pengajian Rutin': 'k4',  # 106332
        'Menyelenggarakan Sholat Jumat': 'k5',  # 9687
        'Menyelenggarakan Sholat Malam': 'k6',  # 14
        'Menyelenggarakan kegiatan pendidikan (TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)': 'k7',  # 67859
        'Menyelenggarakan kegiatan sosial ekonomi (koperasi masjid)': 'k8',  # 3826
        'Papan nama Musholla': 'k9',  # 24
        'Pemberdayaan Zakat/Infaq/Shodaqoh dan Wakaf': 'k10',  # 67734
        'Stempel Musholla': 'k11',  # 13
        'TPQ': 'k12',  # 110
        'Upload foto mushala': 'k13',  # 18
        'pengajian': 'k14',  # 21
    }
