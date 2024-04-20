import webbrowser, os, run_service
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

refresh_token, access_token, crd, address, allergy = None, None, None, None, None

#Flask 인스턴스 생성 및 템플릿 폴더 설정
app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['GET', 'POST'])
def inintial():
    return render_template('home.html')

@app.route('/test', methods = ['GET', 'POST'])
def test():
    return 'test'

@app.route('/main', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        webbrowser.open(os.environ.get('call_back_url'))

    return render_template('main.html', call_back_url = os.environ.get('call_back_url'))

@app.route('/kakaocallback')
def kakaocallback():
    global access_token, refresh_token

    #URL에서 'code' 파라미터 추출
    code = request.args.get('code')
    token = run_service.get_token(code, os.environ.get('k_client_id'), os.environ.get('k_redirect_uri'))
    access_token = token[0]
    refresh_token = token[1]

    #액세스 토큰 요청
    return render_template('main.html')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    global crd, address
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        crd = request.form.get('좌표')
        print('crd :', crd)
        address = run_service.geocoding_reverse(crd)
        address = str(address).split(', ')
        address = address[1]
        print('address :', address)
    return render_template('map.html', java_key = os.environ.get('k_java_key'))

@app.route('/allergy', methods=['GET', 'POST'])
def allergy():
    global allergy
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        allergy = request.form.getlist('allergy')
        print('allergy :', allergy)

    return render_template('allergy.html')

@app.route('/dust_weather')
def dust():
    return render_template('dust_weather.html')

@app.route('/service')
def service():
    run_service.serve_code(address, access_token, crd)
    #함수호출 
    return render_template('main.html')

#서버 실행
if __name__ == '__main__':
    app.run(port = 5051, ssl_context = ('ssl/self_signed_certificate.pem', 'ssl/private_key.pem'))