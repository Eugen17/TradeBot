import time
import datetime
import requests
import telebot
from bs4 import BeautifulSoup
import re

send_content = "Currency -*{0}* \n" + \
               "Price - *{1}*\n" + \
               "Time - *{2}*\n"


def get_html_soup(html):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.84 Safari/537.36'}

    r = requests.get(html, headers=headers)
    data_fromhtml = r.content
    soup = BeautifulSoup(data_fromhtml, "html.parser")
    return soup


def get_currency(name):
    print('rabotaem')
    soup = get_html_soup('https://www.investing.com/currencies/'+name)
    curse = (soup.find("span", {"id": "last_last"})).text
    if name == 'gbp-usd':
        timenow = (soup.find("span", {"class": "bold pid-2-time"})).text
    if name == 'jpy-usd':
        timenow = (soup.find("span", {"class": "bold pid-1910-time"})).text
    if name == 'eur-usd':
        timenow = (soup.find("span", {"class": "bold pid-1-time"})).text
    return send_content.format(name.upper(), curse, timenow)


def get_commodities(name):
    print('rabotaem')
    soup = get_html_soup('https://www.investing.com/commodities/'+name)
    curse = (soup.find("span", {"id": "last_last"})).text
    if name == 'brent-oil':
        timenow = (soup.find("span", {"class": "bold pid-8833-time"})).text
    if name == 'gold':
        timenow = (soup.find("span", {"class": "bold pid-8830-time"})).text
    if name == 'silver':
        timenow = (soup.find("span", {"class": "bold pid-8836-time"})).text
    if name == 'platinum':
        timenow = (soup.find("span", {"class": "bold pid-8910-time"})).text
    return send_content.format(name.upper(), curse, timenow)

