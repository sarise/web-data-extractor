from __future__ import absolute_import, division, print_function, unicode_literals

import re
import traceback

from bs4 import BeautifulSoup

from wde.core.elements.masjid import Masjid, Details
from wde.core.parse.masjid.populate_ids import extract_tipologi_ids


class Parser:

    tipologi_to_id_mapping = extract_tipologi_ids()
    profile_url = 'http://simas.kemenag.go.id/index.php/profil/masjid/%s/'   # masjid_id
    element_cls = Masjid

    @classmethod
    def construct_profile_url(cls, masjid_id):
        return cls.profile_url % masjid_id

    @classmethod
    def extract(cls, content, url_id=None):
        soup = BeautifulSoup(content, 'html.parser').find('div', class_='wrap')

        try:
            # Top heading bar
            div_title = soup.find('div', id='profil-title')
            div_logo = div_title.find('div', id=re.compile(r'^logo(|\-mushalla)$'))
            name = div_logo.find('h6').text
            address = div_logo.find_all('div')[-1].text.strip()
            tipologi = div_title.find('div', id='tip').find('a').text
            tipologi_id = cls.tipologi_to_id_mapping.get(tipologi, '')

            # Sub-heading bar
            div_alamat = soup.find('h5').find_all('a', href=True)
            provinsi, provinsi_id = div_alamat[0].text, div_alamat[0]['href'].split('=')[-1]
            kabupaten, kabupaten_id = div_alamat[1].text, div_alamat[1]['href'].split('=')[-1]
            kecamatan, kecamatan_id = div_alamat[2].text, div_alamat[2]['href'].split('=')[-1]

            # Table
            main_table = soup.find('table', id='profil-table')
            id_ = main_table.find('td').text.strip()  # Assume the first one is always masjid/mushalla id

            header_to_variable_mapping = {
                'Luas Tanah': 'luas_tanah',
                'Status Tanah': 'status_tanah',
                'Luas Bangunan': 'luas_bangunan',
                'Tahun Berdiri': 'tahun_berdiri',
                'Daya Tampung Jamaah': 'capacity',
                'No Telp/Faks': 'contact',
                'Fasilitas': 'facilities',
                'Kegiatan': 'activities',
                'Jumlah Pengurus': 'jumlah_pengurus',
            }

            # Initialize the dict with empty string to avoid failed creation of namedtuple Details
            data = {}
            for key in header_to_variable_mapping.values():
                data[key] = ''

            # Extract data based on the matching header
            for row in main_table.find_all('tr'):
                th = row.find('th')
                if th:
                    header = th.text
                    if header not in ['ID Masjid', 'ID Mushalla', 'IMAM', 'KHATIB', 'Dokumen']:
                        data[header_to_variable_mapping[header]] = row.find('td').text

            # Sanitized the extracted data
            data['luas_tanah'] = cls._sanitize_luas(data['luas_tanah'])
            data['luas_bangunan'] = cls._sanitize_luas(data['luas_bangunan'])
            data['contact'] = data['contact'].strip()
            data['facilities'] = cls._sanitize_string_list(data['facilities'])
            data['activities'] = cls._sanitize_activities(data['activities'])
            data['jumlah_pengurus'] = cls._sanitize_int(data['jumlah_pengurus'])
            details = Details(**data)
            
        except Exception:  # pylint: disable=broad-except
            print(cls.construct_profile_url(url_id), traceback.format_exc())
            return None

        return cls.element_cls(
            id_=id_,
            name=name,
            url_id=url_id,
            address=address,
            provinsi=provinsi,
            provinsi_id=provinsi_id,
            kabupaten=kabupaten,
            kabupaten_id=kabupaten_id,
            kecamatan=kecamatan,
            kecamatan_id=kecamatan_id,
            tipologi=tipologi,
            tipologi_id=tipologi_id,
            details=details,
        )

    @classmethod
    def _sanitize_activities(cls, text):
        # Replace commas with slashes to avoid being tokenized
        text = text.replace(
            '(TPA, Madrasah, Pusat Kegiatan Belajar Masyarakat)',
            '(TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)',
        )
        text = text.replace(
            'Pemberdayaan Zakat, Infaq, Shodaqoh dan Wakaf',
            'Pemberdayaan Zakat/Infaq/Shodaqoh dan Wakaf'
        )
        return cls._sanitize_string_list(text)

    @classmethod
    def _sanitize_luas(cls, text):
        return cls._sanitize_int(text.replace('m2', '').strip())

    @classmethod
    def _sanitize_int(cls, text):
        try:
            return int(text.strip().replace('.', ''))
        except ValueError:
            return text

    @classmethod
    def _sanitize_string_list(cls, text):
        return list(map(lambda x: x.strip(), text.split(','))) if text else []
