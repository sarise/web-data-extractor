from __future__ import absolute_import, division, print_function, unicode_literals

import requests


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def get_content(url):
    page = requests.get(url)

    if page.status_code == 200:
        return page.content.decode('UTF-8')

    return None
