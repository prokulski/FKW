from .api_key import api_key
import requests
from urllib.parse import urlencode


rejestr_url = 'https://rejestr.io/api/v1'


def api_search(name):
    query_url = rejestr_url + '/krs?' + urlencode({'name': name,
                                                   'w_likwidacji': 0,
                                                   'w_upadlosci': 0,
                                                   'w_zawieszeniu': 0})
    res = requests.get(query_url, headers={'Authorization': api_key})
    return res
