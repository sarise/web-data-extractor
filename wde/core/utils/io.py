from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import simplejson as json


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def get_content(url):
    page = requests.get(url)

    if page.status_code == 200:
        return page.content.decode('UTF-8')

    return None


def pretty_print(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
