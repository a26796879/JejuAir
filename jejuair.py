import requests, json, math
from datetime import timedelta, date
import datetime

url = 'https://ibsearch.jejuair.net/jejuair/com/jeju/ibe/availHybris.do'

headers = {
'accept-language': 'zh-TW',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.jejuair.net',
'referer': 'https://www.jejuair.net/jejuair/tw/com/jeju/ibe/goAvail.do',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
#
othercost = 724 + 1097

def getArrFare():
    #SegType = RET回程 DEP去程
    def params(SegType,DepStn,ArrStn):
        params = {
        'AdultPaxCnt': '1','ChildPaxCnt': '0','InfantPaxCnt': '0','RouteType': 'I','Language': 'TW','ReturnSeatAvail': 'true','PointsPayment': 'false','FFPGrade': '','TripType': 'RT',
        'DepDate': DetDate,
        'SegType': SegType,
        'DepStn': DepStn,
        'ArrStn': ArrStn,
        'SystemType': 'IBE',"MULTIFLAG":"N","COUNTRYNAME":"TAIWAN","MAXAMT":'6000',"REGIONCODE":"NEA","CURRENCY":"TWD"}
        return params

    for day in range (1,20):
        days = day * 7
        DetDate = datetime.date.today() + timedelta(days=days)
        #from TPE to PUS
        dep_res = requests.post(url , headers = headers , params = params('DEP','TPE','PUS'))
        dep_js = json.loads(dep_res.text)
        #from PUS to TPE
        ret_res = requests.post(url , headers = headers , params = params('RET','PUS','TPE'))
        ret_js = json.loads(ret_res.text)
        for i in range(7):
            try:
                #行程一（早去） 03:00 TPE-> 06:10 PUS
                DepTime = dep_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['FlightSegment']['DepTime']
                if DepTime == "03:00":
                    without_dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['Fares'][0]['Fare']
                    fithty_dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['Fares'][1]['Fare']
                else:
                    without_dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['Availability'][1]['Fares'][0]['Fare']
                    fithty_dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['Availability'][1]['Fares'][1]['Fare']
                if without_dep_price == 0:
                    without_dep_price = '完售'
                if fithty_dep_price == 0:
                    fithty_dep_price = '完售'
                dep_date = dep_js['Result']['Data']['AvailabilityDates'][i]['Date']
                print ('無行李:' + str(without_dep_price),'15kg行李:'+str(fithty_dep_price),dep_date)
            except:
                break
                print('查詢完畢')
            try:
                #行程二（晚回） 21:40 PUS-> 23:50 TPE
                DepTime = ret_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['FlightSegment']['DepTime']
                if DepTime == "21:40":
                    without_ret_price = ret_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['Fares'][0]['Fare']
                    fithty_ret_price = ret_js['Result']['Data']['AvailabilityDates'][i]['Availability'][0]['Fares'][1]['Fare']
                else:
                    without_ret_price = ret_js['Result']['Data']['AvailabilityDates'][i]['Availability'][1]['Fares'][0]['Fare']
                    fithty_ret_price = ret_js['Result']['Data']['AvailabilityDates'][i]['Availability'][1]['Fares'][1]['Fare']
                if without_ret_price == 0:
                    without_ret_price = '完售'
                if fithty_ret_price == 0:
                    fithty_ret_price = '完售'
                ret_date = ret_js['Result']['Data']['AvailabilityDates'][i]['Date']
                print ('無行李:' + str(without_ret_price),'15kg行李:'+str(fithty_ret_price),ret_date)
            except:
                break
                print('查詢完畢')
                
def getArrFare_Cheapest():
    #SegType = RET回程 DEP去程
    def params(SegType,DepStn,ArrStn):
        params = {
        'AdultPaxCnt': '1','ChildPaxCnt': '0','InfantPaxCnt': '0','RouteType': 'I','Language': 'TW','ReturnSeatAvail': 'true','PointsPayment': 'false','FFPGrade': '','TripType': 'RT','DepDate': DetDate,
        'SegType': SegType,
        'DepStn': DepStn,
        'ArrStn': ArrStn,
        'SystemType': 'IBE',"MULTIFLAG":"N","COUNTRYNAME":"TAIWAN","MAXAMT":'6000',"REGIONCODE":"NEA","CURRENCY":"TWD"}
        return params

    for day in range (1,20):
        days = day * 7
        DetDate = datetime.date.today() + timedelta(days=days)
        #去程最便宜
        dep_res = requests.post(url , headers = headers , params = params('DEP','TPE','PUS'))
        dep_js = json.loads(dep_res.text)
        for i in range(7):
            dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['CheapestFare'] 
            if dep_price == 0:
                break
            dep_date = dep_js['Result']['Data']['AvailabilityDates'][i]['Date']
            print(math.ceil(dep_price),dep_date)
        #回程最便宜
        dep_res = requests.post(url , headers = headers , params = params('RET','PUS','TPE'))
        dep_js = json.loads(dep_res.text)
        for i in range(7):
            dep_price = dep_js['Result']['Data']['AvailabilityDates'][i]['CheapestFare'] 
            if dep_price == 0:
                break
            dep_date = dep_js['Result']['Data']['AvailabilityDates'][i]['Date']
            print(math.ceil(dep_price),dep_date)

getArrFare()
#getArrFare_Cheapest()
