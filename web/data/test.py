import requests, json
from decouple import config
from urllib.parse import urlencode, quote_plus

k = config('foodKey')
# k='cUrXjCod9NLhb2dpkxgVyG0Yc0KPGFKFDGyfN5StAQ2qJQVBDM7g0e64CxRoYXW5hYfKu5muWtCVSxeY0p3kCg%3D%3D'
url = 'https://tradifood.net/api/service/TradFoodInfoService/getFoodCateogryList'
url = 'http://apis.data.go.kr/B551553/TradFoodInfoService/getFoodCateogryList'
url = 'http://apis.data.go.kr/B551553/TradFoodInfoService/getFoodCateogryList?'

# url = 'http://apis.data.go.kr/B551553/TradFoodInfoService'
param = {
    'serviceKey':k,
    # 'pageNo': 1,
    # 'numOfRows': 10,
    # 'type':'JSON',
}
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : k, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('type') : 'JSON' })
# url = url+queryParams
# http = urllib3.poolmanager()
# res = http.request('GET', url)
res = requests.get(url, params=param, verify=False)
print(res.text)
# print(res.headers)
print(res.url)