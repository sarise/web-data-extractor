from __future__ import absolute_import, division, print_function, unicode_literals

import re
import traceback

from bs4 import BeautifulSoup

from wde.core.elements.masjid import Masjid
from wde.core.parse.masjid.populate_ids import extract_tipologi_ids

MASJID_PROFILE_URL = 'http://simas.kemenag.go.id/index.php/profil/masjid/%s/'   # masjid_id
MASJID_TABLE_URL = 'http://simas.kemenag.go.id/index.php/profil/masjid/%s'      # table iterator


class Parser:

    tipologi_to_id_mapping = extract_tipologi_ids()

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
            tipologi_id = cls.tipologi_to_id_mapping[tipologi]

            # Sub-heading bar
            div_alamat = soup.find('h5').find_all('a', href=True)
            provinsi, provinsi_id = div_alamat[0].text, div_alamat[0]['href'].split('=')[-1]
            kabupaten, kabupaten_id = div_alamat[1].text, div_alamat[1]['href'].split('=')[-1]
            kecamatan, kecamatan_id = div_alamat[2].text, div_alamat[2]['href'].split('=')[-1]

            # Table
            tds = soup.find('table', id='profil-table').find_all('td')
            id_ = tds[0].text.strip()
            luas_tanah = tds[1].text
            status_tanah = tds[2].text
            luas_bangunan = tds[3].text
            tahun_berdiri = tds[4].text
            capacity = tds[5].text
            contact = tds[6].text.strip()
            facilities = cls._sanitize_string_list(tds[7].text)
            activities = cls._sanitize_activities(tds[8].text)
            jumlah_pengurus = cls._sanitize_int(tds[9].text)

        except Exception:  # pylint: disable=broad-except
            print(MASJID_PROFILE_URL % url_id, traceback.format_exc())
            return None

        return Masjid(
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
            luas_tanah=cls._sanitize_luas(luas_tanah),
            status_tanah=status_tanah,
            luas_bangunan=cls._sanitize_luas(luas_bangunan),
            tahun_berdiri=tahun_berdiri,
            capacity=capacity,
            contact=contact,
            jumlah_pengurus=jumlah_pengurus,
            facilities=facilities,
            activities=activities,
        )

    @classmethod
    def _sanitize_activities(cls, text):
        # Replace commas with slashes to avoid being tokenized
        text = text.replace(
            '(TPA, Madrasah, Pusat Kegiatan Belajar Masyarakat)',
            '(TPA/Madrasah/Pusat Kegiatan Belajar Masyarakat)',
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
        return list(map(lambda x: x.strip(), text.split(',')))
