"""Login command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from getpass import getpass
from gefcli.configuration import SETTINGS

from gefcli import config

import re
import requests

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid(email):
    """Check if the email is valid"""
    return bool(email)

def run():
    """Login command"""

    email = None
    while email is None or not is_valid(email) or not EMAIL_REGEX.match(email):
        email = input("Please enter your email: ")

    password = None
    while email is None or not is_valid(password):
        password = getpass(prompt='Please enter your password:')


    response = requests.post(url=SETTINGS.get('url_api')+'/auth', json={'username': email, 'password': password})

    if response.status_code != 200:
        print('Error login.')
        return False

    body = response.json()

    config.set('JWT', body['access_token'])

    return True
