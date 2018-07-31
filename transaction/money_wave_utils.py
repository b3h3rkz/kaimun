"""
Set of utility methods for use with the moneywave api
"""

import requests


BASE_URL = "https://moneywave.herokuapp.com/v1/"
auth_token = ''


def get_auth_token():
    url = BASE_URL + "merchant/verify"
    payload = {'apiKey': 'ts_JIGRALK6O6YGH196OGPM', 'secret': 'ts_SHU80QZ8NAO2H2ZZPIFHYQD4WQZGMA'}
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()
    auth_token = response['token']
    return auth_token


def get_banks(country):
    url = BASE_URL + "banks"
    headers = {'content-type': 'application/json'}
    params = {'country': country}
    response = requests.post(url, params=params, headers=headers)
    banks = response.json()
    return banks


def resolve_account(account_number, bank_code, currency):
    token = get_auth_token()
    headers = {'content-type': 'application/json', 'authorization': token}
    url = BASE_URL + "resolve/account"
    payload = {'currency': currency, 'bank_code': bank_code, 'account_number': account_number}
    print(type(payload['account_number']))
    response = requests.post(url, json=payload, headers=headers)
    response = response.json()
    print(response)
    if response['status'] == "success":
        return True
    else:
        return False


def disburse(account_number):
    pass



