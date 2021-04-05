import requests, json
from decouple import config
from urllib.parse import urlencode, quote_plus

k = config('foodKey')
url = 'https://tradifood.net/api/service/TradFoodInfoService/getFoodCateogryList'
url = 'http://apis.data.go.kr/B551553/TradFoodInfoService/getFoodCateogryList'
url = 'http://apis.data.go.kr/B551553/TradFoodInfoService/getFoodCateogryList?'

# url = 'http://apis.data.go.kr/B551553/TradFoodInfoService'
param = {
    'serviceKey':k,
    'pageNo': 1,
    'numOfRows': 10,
    'type':'JSON',
}
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : k, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('type') : 'JSON' })
# url = url+queryParams
# http = urllib3.poolmanager()
# res = http.request('GET', url)
res = requests.get(url, params=param)
print(res.text)
# print(res.headers)
print(res.url)