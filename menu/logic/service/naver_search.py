import os, requests
from dotenv import load_dotenv
load_dotenv()

#검색 request에 필요한 header(= 앱 소유자의 정보) 확보 -> 검색 request 로직 실행 

#로그인 로직
nheaders = {'X-Naver-Client-Id' : os.environ.get('n_client_id'),
            'X-Naver-Client-Secret' : os.environ.get('n_client_secret')}
naver_local_url = 'https://openapi.naver.com/v1/search/local.json?'

#검색 로직
restaurant = []
def search_res(location, foods_list):

    for food in foods_list:
        #검색어 지정
        query = location + ' ' + food + ' 맛집'
        
        #지역검색 요청 파라메터 설정
        params = 'sort=comment' + '&query='+ query + '&display=' + '5'
        
        #검색
        res = requests.get(naver_local_url,
                           params=params,
                           headers=nheaders)
        
        result_list = res.json().get('items')
        if not result_list:
            print('검색 실패')
        #경우 1,2 처리
        #해당 음식 검색 결과에서 가장 상위를 가져옴
        if result_list:
            restaurant.append(result_list[0])
        #3개를 찾았다면 검색 중단
            if len(restaurant) > 3:
                break
        #경우 1,2 처리
        #해당 음식 검색 결과에서 가장 상위를 가져옴
            if result_list:
                restaurant.append(result_list[0])
            #3개를 찾았다면 검색 중단
                if len(restaurant) > 3:
                    break
    return restaurant