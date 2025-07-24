# 타입 힌트를 활용한 라우팅

# 타입 힌트 : 프로그래밍 언어에서 변수, 함수 인자, 반환값 등의 데이터 타입을 명시적으로 표기하는 기법
# 코드의 가독성을 높이고, 에러를 미리 잡을 수 있게 함

# 플라스크 URL 타입 힌트는 들어오는 타입이 선언한 타입과 다르다면, 실행 시 에러를 발생시킴

from flask import Flask
app = Flask(__name__)

@app.route('/int/<int:var>')  # int: - 이 부분은 정수형으로만 허용  # var : 그 정수 값을 함수 매개변수로 전달할 변수 이름
def int_type(var:int):  # 파이썬 타입 힌트 # 변수 var이 int 타입이기를 기대(강제x)
    return f'Integer: {var}'

@app.route('/float/<float:var>')
def float_type(var:float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>') # path 타입은 /를 포함한 문자열을 받는다. 
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>') # uuid 타입은 UUID 포맷에 맞는 문자열을 받는다.
def show_uuid(some_id):            # UUID는 128bit 숫자이며 유일성이 거의 보장되는 랜덤 식별자이다. 
    return f'UUID: {some_id}'

# 플라스크의 URL 타입 힌트는 타입이 일치하지 않을 경우 자동으로 404 에러를 반환해주기 떄문에
# 이를 활용하면 매개변수 검증 작업을 훨씬 쉽게 처리할 수 있으며, 보안성도 강화할 수 있다. 