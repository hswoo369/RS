import requests
import json

from datetime import datetime, timedelta
from dateutil.parser import parse

API_URL = 'https://api.gopax.co.kr'

#자산 목록 조회하기
def get_asset_list():
    result = requests.get(API_URL + '/assets')
    return json.loads(result.text)

#거래쌍 목록 조회하기
def get_trading_pairs():
    result = requests.get(API_URL + '/trading-pairs')
    return json.loads(result.text)

#Ticker 조회하기
def get_ticker(trading_pair):
    result = requests.get(API_URL + '/trading-pairs/%s/ticker' % trading_pair)
    return json.loads(result.text)

#
def get_books(trading_pair):
    result = requests.get(API_URL + '/trading-pairs/%s/book' % trading_pair)
    return json.loads(result.text)

def get_recent_deals(trading_pair, limit, after, before):
    req = API_URL + '/trading-pairs/%s/trades' % trading_pair
    parameter = {'limit': limit, 'after': after, 'before': before}
    result = requests.get(req, params = parameter)
    return json.loads(result.text)

#시간을 내맘대로 적으면 알아서 잘라주는 함수 (parse)
def get_timestamp(date_string):
    return parse(date_string).timestamp()

def get_past_data(trading_pair, start, end, interval = 1):
    req = API_URL + '/trading-pairs/%s/candles' % trading_pair
    parameter = {'start': start * 1000, 'end': end * 1000, 'interval': interval}
    result = requests.get(req, params = parameter)
    return json.loads(result.text)