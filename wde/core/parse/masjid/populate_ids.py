from __future__ import absolute_import, division, print_function, unicode_literals

import csv
from collections import namedtuple
from multiprocessing.pool import Pool
from repoze.lru import lru_cache

from bs4 import BeautifulSoup

from wde.core.utils.io import get_content, write_json_to_file

SEARCH_URL = 'http://simas.kemenag.go.id/index.php/search/'
KABUPATEN_SELECT_URL = 'http://simas.kemenag.go.id/index.php/ajax/address/kabupaten/%s/0/kabupaten_id2'  # provinsi id
KECAMATAN_SELECT_URL = 'http://simas.kemenag.go.id/index.php/ajax/address/kecamatan/%s/0'  # kecamatan id

NameId = namedtuple('NameId', ['id', 'name'])


def _parse_ids_from_select_element(content, select_id):
    soup = BeautifulSoup(content, 'html.parser')
    selection = soup.find('select', attrs={'name': select_id})

    ids = {}
    for option in selection.find_all('option'):
        id_ = option.get('value')
        if id_:
            ids[id_] = option.text
    return ids


@lru_cache(maxsize=1)
def extract_tipologi_ids():
    html = get_content(SEARCH_URL)
    mapping = _parse_ids_from_select_element(html, 'tipologi_id')
    # Invert the mapping as it's used to translate from name to id
    return {v: k for k, v in mapping.items()}


def _extract_provinsi_ids():
    html = get_content(SEARCH_URL)
    return _parse_ids_from_select_element(html, 'provinsi_id')


def _extract_kabupaten_ids(provinsi):
    name_id = NameId(*provinsi)
    html = get_content(KABUPATEN_SELECT_URL % name_id.id)
    return _parse_ids_from_select_element(html, 'kabupaten_id'), name_id


def _extract_kecamatan_ids(kabupaten):
    name_id = NameId(*kabupaten)
    html = get_content(KECAMATAN_SELECT_URL % name_id.id)
    return _parse_ids_from_select_element(html, 'kecamatan_id'), name_id


def _merge_outputs(outputs):
    name_to_id_mapping = {}
    parent_child_relation = {}
    for dict_, name_id in outputs:
        name_to_id_mapping.update(dict_)
        parent_child_relation[name_id] = [NameId(*item) for item in dict_.items()]

    return name_to_id_mapping, parent_child_relation


def _write_relations_to_csv(prov_to_kab, kab_to_kec):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['provinsi_name', 'provinsi_id', 'kabupaten_name', 'kabupaten_id', 'kecamatan_name', 'kecamatan_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for provinsi, kabupatens in prov_to_kab.items():
            for kabupaten in kabupatens:
                for kecamatan in kab_to_kec[kabupaten]:
                    writer.writerow({
                        'provinsi_name': provinsi.name,
                        'provinsi_id': provinsi.id,
                        'kabupaten_name': kabupaten.name,
                        'kabupaten_id': kabupaten.id,
                        'kecamatan_name': kecamatan.name,
                        'kecamatan_id': kecamatan.id,
                    })


def main():
    # tipologi ids
    tipologi_dict = extract_tipologi_ids()
    write_json_to_file('tipologi_ids.json', tipologi_dict)

    # provinsi ids
    provinsi_dict = _extract_provinsi_ids()
    write_json_to_file('provinsi_ids.json', provinsi_dict)

    # kabupaten ids
    with Pool(10) as p:
        records = p.map(_extract_kabupaten_ids, provinsi_dict.items())
    kabupaten_dict, provinsi_to_kabupaten_name_ids = _merge_outputs(records)
    write_json_to_file('kabupaten_ids.json', kabupaten_dict)

    # kecamatan ids
    with Pool(10) as p:
        records = p.map(_extract_kecamatan_ids, kabupaten_dict.items())
    kecamatan_dict, kabupaten_to_kecamatan_name_ids = _merge_outputs(records)
    write_json_to_file('kecamatan_ids.json', kecamatan_dict)

    _write_relations_to_csv(provinsi_to_kabupaten_name_ids, kabupaten_to_kecamatan_name_ids)

    assert len(kecamatan_dict) == 6947

if __name__ == '__main__':
    main()
