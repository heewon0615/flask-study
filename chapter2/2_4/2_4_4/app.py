# 플라스크에서느 make_response() 함수를 사용해서 상태 코드와 헤더를 지정하는 헬퍼 함수를 제공한다. 

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/response')
def response_example():
    # 응답 객체를 생성한다. "Hello with header"는 응답 바디이며, 200은 HTTP 상태 코드이다.
    resp = make_response("Hello with header", 200)
    # 'Custom-Header'라는 이름의 사용자 정의 헤더를 설정하고 'custom-value' 값을 지정
    resp.headers['Custom-Header'] = 'custer-value'
    # 설정한 헤더와 함께 응답 객체를 반환
    return resp
    