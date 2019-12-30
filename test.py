'''
import requests, json, math
from datetime import timedelta, date
import datetime

url = 'https://ibsearch.jejuair.net/jejuair/com/jeju/ibe/searchFareTaxHybris.do'

headers = {
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'accept-language': 'zh-TW',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.jejuair.net',
'referer': 'https://www.jejuair.net/jejuair/tw/com/jeju/ibe/goAvail.do',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

params = {
    'Itinerary': {"DEP":[{"DepStn":"TPE","DepDate":"2020-01-16","DepTime":"03:00","ArrStn":"PUS","ArrDate":"2020-01-16","ArrTime":"06:10","FlightNumber":"2654","BundleType":"B","FareBasis":"OB3ETW","RBD":"O"}],"RET":[{"DepStn":"PUS","DepDate":"2020-01-23","DepTime":"11:00","ArrStn":"TPE","ArrDate":"2020-01-23","ArrTime":"12:45","FlightNumber":"2651","BundleType":"B","FareBasis":"MB3ETW","RBD":"M"}]},
    'RouteType': 'I',
    'TripType': 'RT',
    'Language': 'TW',
    'CachingFlag': 'T',
    'SystemType': 'IBE'}
    
res = requests.post(url , headers = headers , params = params)

#js = json.loads(res.text)
print (res.text)
'''

def test():
    test = 'test11'
    print (test)

test()
