import xml.etree.ElementTree as elemTree, requests

def dust_weather(data, service_key):

    dust_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0"%(service_key)
    item_code_pm10 = "PM10"

    data_gubun = "HOUR"
    search_condition = "WEEK"

    payload = "serviceKey=" + service_key + "&" + "dataType=json" + "&" + "dataGubun=" + data_gubun + "&" + "searchCondition=" + search_condition + "&" + "itemCode="

    #미세먼지 수치 가져오기
    pm10_res = requests.get(dust_url + payload + item_code_pm10)

    #xml 파싱하기
    pm10_tree = elemTree.fromstring(pm10_res.text)
    dust_data = dict()

    pm_per_tree = ['pm10']
    pm_tree = [pm10_tree]

    for i in range(len(pm_per_tree)):
        item = pm_tree[i].find("body").find("items").find("item")
        code = pm_per_tree[i]
        value = float(item.findtext(pm_per_tree[i]+"Value"))
        dust_data[code] = {'value' : value}

    pm10_value = dust_data.get('pm10').get('value')
    if pm10_value <= 30:
        pm10_state = "좋음"
    elif pm10_value <= 80:
        pm10_state = "보통"
    elif pm10_value <= 150:
        pm10_state = "나쁨"
    else:
        pm10_state = "매우나쁨"

    #미세먼지가 나쁜 상태인지(1)/아닌지(0)
    if pm10_value > 60:
        dust_code = "1"
    else:
        dust_code = "0"

    dust_data.get('pm10')['state'] = pm10_state
    dust_data['code'] = dust_code
    data['dust'] = dust_data
    print("dust_weather :", data)
    return data