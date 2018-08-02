"""
Set of utility methods for use with the moneywave api
"""

import requests
from random import randint
import os
from config.settings.keys import *

BASE_URL = "https://moneywave.herokuapp.com/v1/"
auth_token = ''


def get_auth_token():
    url = BASE_URL + "merchant/verify"
    payload = {'apiKey': MONEY_RAVE_API_KEY, 'secret': MONEY_RAVE_API_SECRET}
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, json=payload, headers=headers).json()
    print(response)
    auth_token = response['token']
    return auth_token


def get_banks(country):
    url = BASE_URL + "banks"
    headers = {'content-type': 'application/json'}
    params = {'country': country}
    response = requests.post(url, params=params, headers=headers).json()
    return response


def resolve_account(account_number, bank_code, currency):
    token = get_auth_token()
    headers = {'content-type': 'application/json', 'authorization': token}
    url = BASE_URL + "resolve/account"
    payload = {
        'currency': currency,
        'bank_code': bank_code,
        'account_number': account_number
    }
    # print(type(payload['account_number']))
    response = requests.post(url, json=payload, headers=headers).json()
    if response['status'] == "success":
        return response
    else:
        return False


def disburse(account_number, bankcode, amount, narration, currency, sender):
    token = get_auth_token()
    headers = {'content-type': 'application/json', 'authorization': token}
    url = BASE_URL + "disburse"
    payload = {
        "accountNumber": account_number,
        "bankcode": bankcode,
        "amount": amount,
        "narration": narration,
        "ref": get_ref(),
        "currency": currency,
        "senderName": sender,
        "lock": NAIRA_WALLET_LOCK
    }
    response = requests.post(url, json=payload, headers=headers).json()
    print(response)
    if response['status'] == "success":
        print(response, "paid")
        return response
    else:
        return False


def get_ref():
    return "Kaimun" + str(randint(00000, 99999))
