import os, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(coordinate):

    now = datetime.now()

    vilage_weather_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'
    service_key = os.environ.get('service_key')

    today = now.date()
    base_date = today.strftime('%Y%m%d')
    base_time = '0800'

    nx = coordinate[0]
    ny = coordinate[1]

    payload = 'serviceKey=' + service_key + '&' + 'dataType=json' + '&' + 'base_date=' + base_date + '&' + 'base_time=' + base_time + '&' + 'nx=' + nx + '&' + 'ny=' + ny

    res = requests.get(vilage_weather_url + payload)
    items = res.json().get('response').get('body').get('items')

    data = dict()
    data['date'] = base_date
    weather_data = dict()

    for item in items['item']:
        
        #기온
        if item['category'] == 'TMP':
            weather_data['tmp'] = item['fcstValue']

        #기상상태
        if item['category'] == 'PTY':
            weather_code = item['fcstValue']
            if weather_code == '1':
                weather_state = '비'
            elif weather_code == '2':
                weather_state = '비/눈'
            elif weather_code == '3':
                weather_state = '눈'
            elif weather_code == '4':
                weather_state = '소나기'
            else:
                weather_state = '없음'
            
            weather_data['code'] = "0"
            weather_data['code'] = weather_code
            weather_data['state'] = weather_state

    data['weather'] = weather_data
    return [data, service_key]