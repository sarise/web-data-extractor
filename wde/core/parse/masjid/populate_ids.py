from __future__ import absolute_import, division, print_function, unicode_literals

from multiprocessing.pool import Pool

from bs4 import BeautifulSoup

from wde.core.utils.io import get_content, write_json_to_file

SEARCH_URL = 'http://simas.kemenag.go.id/index.php/search/'
KABUPATEN_SELECT_URL = 'http://simas.kemenag.go.id/index.php/ajax/address/kabupaten/%d/0/kabupaten_id2'  # provinsi id
KECAMATAN_SELECT_URL = 'http://simas.kemenag.go.id/index.php/ajax/address/kecamatan/%d/0'  # kecamatan id


def _parse_ids_from_select_element(content, select_id):
    soup = BeautifulSoup(content, 'html.parser')
    selection = soup.find('select', id=select_id)

    ids = {}
    for option in selection.find_all('option'):
        id_ = option.get('value')
        if id_:
            ids[option.text] = int(id_)
    return ids


def _extract_provinsi_ids():
    html = get_content(SEARCH_URL)
    return _parse_ids_from_select_element(html, 'provinsi_id2')


def _extract_kabupaten_ids(provinsi_id):
    html = get_content(KABUPATEN_SELECT_URL % provinsi_id)
    return _parse_ids_from_select_element(html, 'kabupaten_id2')


def _extract_kecamatan_ids(kabupaten_id):
    html = get_content(KECAMATAN_SELECT_URL % kabupaten_id)
    return _parse_ids_from_select_element(html, 'kecamatan_id')


def _merge_dicts(list_):
    result = {}
    for dict in list_:
        result.update(dict)
    return result


def main():
    # provinsi ids
    provinsi_dict = _extract_provinsi_ids()
    write_json_to_file('provinsi_ids.json', provinsi_dict)

    # kabupaten ids
    with Pool(10) as p:
        records = p.map(_extract_kabupaten_ids, provinsi_dict.values())
    kabupaten_dict = _merge_dicts(records)
    write_json_to_file('kabupaten_ids.json', kabupaten_dict)

    # kecamatan ids
    with Pool(10) as p:
        records = p.map(_extract_kecamatan_ids, kabupaten_dict.values())
    kecamatan_dict = _merge_dicts(records)
    write_json_to_file('kecamatan_ids.json', kecamatan_dict)


if __name__ == '__main__':
    main()
