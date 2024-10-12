import random
import string
import threading
import asyncio
from time import sleep
import requests
import requests.exceptions
import pathlib as path
import colorama
from bs4 import BeautifulSoup

from typing import Union, Literal, str
from dataclasses import dataclass
from enum import Enum

__vinted_url__ = ""

__conditions__ = [
    "new_with_tags",
    "new_without_tags",
    "very_good",
    "good", 
    "satisfactory"
]

with requests.Session() as session:
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0' })

    with session.post(
        url='https://vinted.ca/en/login',
        data={
            'username': '',
            'password': ''
        },
        headers=headers
    ) as response:
        print(response.ok)



class ArticleConditions(Enum):
    NewWithTags = 0
    NewWithoutTags = 1
    VeryGood = 2
    Good = 3
    Satisfactory = 4

@dataclass
class Article:
    brand: str
    # Status
    condition: Union[ArticleConditions]
    price: str
    price_with_tax: str
    price_without_tax: str
    
def get_post_info():
    pass