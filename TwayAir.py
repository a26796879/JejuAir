import requests, json, math
from datetime import timedelta, date
import datetime
#criteriaDate = datetime.date.today()
dep = 'TPE'
#釜山PUS 大邱TAE 濟州CJU
arr = 'TAE'

headers = {
'Host': 'www.twayair.com',
'Referer': 'https://www.twayair.com/app/booking/chooseItinerary',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
#當天+2天的票，不會賣，所以要查2天+7天後，會一次顯示一週的票
for day in range (1,20):
    days = (day * 8)+1
    criteriaDate = (datetime.date.today() + timedelta(days=days)).strftime('%Y%m%d')

    url = 'https://www.twayair.com/ajax/booking/lowestFare?groupBookingYN=N&criteriaDate='+ criteriaDate +'&period=PN&deptAirportCode='+ dep +'&arriAirportCode='+ arr +'&baseDeptAirportCode='+ dep +'&currency=TWD'

    res = requests.get(url, headers = headers)
    js = json.loads(res.text)
    #系統會一次顯示一週的票，所以可以直接查找7次
    for i in range(8):
        flydate = js['data']['lowestFareMstList'][i]['flightDate']
        soldout = js['data']['lowestFareMstList'][i]['soldoutYn']
        flightOperate = js['data']['lowestFareMstList'][i]['flightOperateYn']
        if soldout == 'Y' or flightOperate == 'N':
            soldout = '完售'
            flightOperate = '未販售'
        else:
            soldout = js['data']['lowestFareDtlMap'][flydate]['totalAmt']
        
        print (flydate,soldout,flightOperate)
    #print (js['data']['lowestFareDtlMap'][0])
