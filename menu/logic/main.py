import webbrowser, os, run_service
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

refresh_token, access_token, crd, location, call_back_url = None, None, None, None, os.environ.get('call_back_url')

#Flask 인스턴스 생성 및 템플릿 폴더 설정
app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['GET', 'POST'])
def inintial():
    return render_template('home.html')

@app.route('/test', methods = ['GET', 'POST'])
def test():
    return 'test'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        webbrowser.open(call_back_url)

    #login.html을 렌더링
    # return 'hkgm;ldrkjmtkiesnriawk'
    return render_template('login.html', call_back_url = call_back_url)

@app.route('/kakaocallback')
def kakaocallback():
    global access_token, refresh_token

    #URL에서 'code' 파라미터 추출
    code = request.args.get('code')
    token = run_service.get_token(code, os.environ.get('k_client_id'), os.environ.get('k_redirect_uri'))
    access_token = token[0]
    refresh_token = token[1]

    #액세스 토큰 요청
    return render_template('login.html')

@app.route('/zone', methods = ['GET', 'POST'])
def zone():
    global location

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        location = request.form.get('위치')
    
    print('location :', location)
    
    #zone.html을 렌더링
    return render_template('zone.html')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    global crd
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        crd = request.form.get('좌표')
        print('crd :', crd)
    return render_template('map.html', java_key = os.environ.get('k_java_key'))

@app.route('/service')
def service():
    run_service.serve_code(location, access_token, crd)
    #함수호출 
    return render_template('login.html')

#서버 실행
if __name__ == '__main__':
    app.run(port = 5051, ssl_context=('ssl/self_signed_certificate.pem', 'ssl/private_key.pem'))