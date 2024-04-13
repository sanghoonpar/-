# -*- coding: utf-8 -*-
import urllib, json, requests

def send(token, location, restaurant, data):
    token = token
    kcreds = {'access_token' : token}

    kheaders = {'Authorization': 'Bearer ' + kcreds.get('access_token'), 'scope':'talk_message'}

    #카카오톡 URL 주소
    kakaotalk_template_url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    #날씨 상세 정보 URL
    weather_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
    #날씨 정보 만들기 
    text = f'''\
    위치 정보 : {location}
    날씨 정보 ({data['date']})
    기온 : {data['weather']['tmp']}
    기우  : {data['weather']['state']}
    미세먼지 : {data['dust']['pm10']['value']} {data['dust']['pm10']['state']}
    '''

    #텍스트 템플릿 형식 만들기
    template = {'object_type': 'text', 'text': text, 'link': {'web_url': weather_url, 'mobile_web_url': weather_url}, 'button_title': '날씨 상세보기'}

    #JSON 형식 -> 문자열 변환
    payload = {'template_object' : json.dumps(template)}

    #카카오톡 보내기
    res = requests.post(url=kakaotalk_template_url, data=payload, headers=kheaders)

    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))

    #리스트 템플릿 형식 만들기
    contents = []
    template = {'object_type' : 'list', 'header_title' : '현재 날씨에 따른 음식 추천', 'header_link' : {'web_url': weather_url, 'mobile_web_url' : weather_url}, 'contents' : contents, 'buttons' : [{'title' : '날씨 정보 상세보기', 'link' : {'web_url': weather_url, 'mobile_web_url' : weather_url}}]}
    
    #contents 만들기
    for place in restaurant:
        title = place.get('title')#장소 이름
        #title : 태극쿵푸<b>마라탕</b>
        #html 태그 제거
        title = title.replace('<b>','').replace('</b>','')

        category = place.get('category')#장소 카테고리
        telephone = place.get('telephone')#장소 전화번호
        address = place.get('address')#장소 지번 주소

        #각 장소를 클릭할 때 네이버 검색으로 연결해주기 위해 작성된 코드
        enc_address = urllib.parse.quote(address + '' + title)
        query = 'query=' + enc_address

    #장소 카테고리가 카페이면 카페 이미지
    #이외에는 음식 이미지
        if '카페' in category:
            image_url = 'https://freesvg.org/img/pitr_Coffee_cup_icon.png'
        else:
            image_url = 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill'

    #전화번호가 있다면 제목과 함께 넣어줍니다.
        if telephone:
            title = title, '\ntel) ', telephone

    #카카오톡 리스트 템플릿 형식에 맞춰줍니다.
        content = {'title': '[' + category + '] ' + title, 'description': ''.join(address.split()[1:]), 'image_url': image_url, 'image_width': 50, 'image_height': 50, 'link': {'web_url': 'https://search.naver.com/search.naver?' + query, 'mobile_web_url': 'https://search.naver.com/search.naver?' + query}}
        contents.append(content)
    #JSON 형식 -> 문자열 변환
    payload = {'template_object' : json.dumps(template)}

    # 카카오톡 보내기

    res = requests.post(url=kakaotalk_template_url, data=payload,
                        headers=kheaders)

    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))