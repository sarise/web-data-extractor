from setuptools import setup

setup(
    name='web-data-extractor',
    install_requires=[
        'beautifulsoup4',
        'enum;python_version<"3.4"',
        'simplejson',
        'requests',
        'repoze.lru',
    ],
    entry_points={
        'console_scripts': [
            'wde = wde.main:main',
            'populate_ids = wde.core.parse.masjid.populate_ids:main',
        ],
    },
    tests_require=["pytest"],
    author='Sari Setianingsih',
    author_email='sari.thok@gmail.com',
)