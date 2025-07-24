# URL 빌더
# url_for() 함수를 사용하면 라우팅 함수의 이름을 기반으로 URL을 생성할 수 있다. 
# 이 기능은 URL을 하드코딩하지 않아도 되므로 나중에 URL 구조가 변경되더라도 쉽게 대응할 수 있다.
# 코드의 유지보수를 쉽게 하고, 라우트 변경이 발생해도 자동으로 반영되어 링크가 깨지는 것을 방지하는 효과가 있다. 

from flask import Flask, url_for, redirect
app = Flask(__name__)

# 홈페이지
@app.route('/')
def index():
    # 여기서는 url_for('index')를 호출
    return f'홈페이지 : {url_for("index")}'

# 사용자 프로필 페이지
@app.route('/user/<username>')
def user_profile(username):
        # 여기서는 url_for("user_profile", username = username)를 호출
    return f'{username}의 프로필 페이지 : {url_for("user_profile", username = username)}'

# 정적 파일 테스트를 위한 경로
@app.route('/static-example')
def static_example():
    return f'정적 파일 URL: {url_for("static", filename="style.css")}'

# 절대 URL 테스트
@app.route('/absolute')
def absolute():
    return f'외부 절대 URL: {url_for("index", _external=True)}'

# HTTPS와 절대 URL 테스트
@app.route('/https')
def https():
    return f'HTTPS 절대 URL : {url_for("index", _scheme="https", _external=True)}'

if __name__ == "__main__":
    app.run(debug=True)