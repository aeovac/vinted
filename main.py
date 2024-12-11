import random
import string
import threading
import asyncio
from time import sleep
import httpx
import requests.exceptions
import pathlib as path
import colorama
import orjson as json
from bs4 import BeautifulSoup

from typing import Union, Optional, List
from decimal import Decimal
from dataclasses import dataclass
from enum import Enum

from config import *

def default_headers():
    headers = ({ 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
        'Referer': 'https://www.vinted.fr/'
    })

    return headers

class ArticleConditions(Enum):
    NewWithTags = 0
    NewWithoutTags = 1
    VeryGood = 2
    Good = 3
    Satisfactory = 4

@dataclass
class Article:
    title: str
    brand: str
    description: str
    # Status
    condition: Optional[ArticleConditions]
    images: List
    price: Union[str, Decimal]
    price_with_tax: Union[str, Decimal]
    price_without_tax: Union[str, Decimal]


def search():
    url = VINTED_URL + '..'
    res = requests.get(url)

    parser = BeautifulSoup(res.text, 'lxml')

def get_post_info(url: str):
    headers = default_headers()
    res = httpx.get(url, headers=headers)
    parser = BeautifulSoup(res.text, 'lxml')

    article = Article(
        title='',
        brand='',
        description='',
        condition=None,
        images=[],
        price='',
        price_with_tax='',
        price_without_tax=''
    )

    tags = parser.find_all('meta')

    images = parser.find_all('img')
    for image in images:
        if 'src' in image.attrs:
            src: str = image.attrs['src'] 
            if src.startswith('https://images1.vinted.net/'):
                article.images.append(src)

    property_map = {
        'og:description': 'description',
        'og:brand': 'brand',
        'og:title': 'title',
        'og:price:amount': 'price'
    }

    for meta in tags:
        if ('property' in meta.attrs and 'content' in meta.attrs):
            property = meta.attrs['property']
            content = meta.attrs['content'] or ''
            print(property)
            print(content)
            if property in property_map:
                article.__setattr__(property_map[property], meta.attrs['content'] or '')
            
    print(article)

if __name__ == '__main__':
    while True:
        search()
        asyncio.sleep(5_000)
        break

    article = get_post_info("https://www.vinted.com/items/5431856535-brown-knitted-sweater?referrer=catalog")
