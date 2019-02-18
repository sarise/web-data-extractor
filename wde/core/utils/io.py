from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import simplejson as json


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def get_content(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'}
    page = requests.get(url, headers=headers, timeout=10)

    if page.status_code == 200:
        return page.content.decode('UTF-8')

    return None


def pretty_print(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


def write_json_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(pretty_print(data))
