from data.menu_choose import menu_choose
from data.weather import weather
from data.dust_weather import dust_weather
from service.kakao_send import send
from service.naver_search import search_res
import requests

def serve_code(location, token, coordinate):
    get = weather(coordinate)
    service_key = get[1]
    data = get[0]
    data = dust_weather(data, service_key)
    foods_list = menu_choose(data)
    restaurant = search_res(location, foods_list)
    send(token, location, restaurant, data)

def get_token(code, client_id, redirect_uri):
    params = {'grant_type': 'authorization_code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'code': code}
    response_token = requests.post('https://kauth.kakao.com/oauth/token', data = params)
    tokens = response_token.json()
    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token')
    print('access_token :', access_token)
    print('refresh_token :', refresh_token) 
    return [access_token, refresh_token]