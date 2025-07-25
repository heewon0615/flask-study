from flask import Blueprint, Flask

# Blueprint 객체 생성
# 첫 번째 인자는 블루프린트의 이름
# 두 번째 인자는 블루프린트가 정의되는 모듈의 이름으로, 일반적으로 '__name__'을 사용한다. 
auth_blueprint = Blueprint('auth', __name__)

# 블루프린트를 사용하여 라우트 정의
@auth_blueprint.route('/login')
def login():
    return '로그인 페이지입니다.'

@auth_blueprint.route('/logout')
def logout():
    return '로그아웃 되었습니다.'

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(auth_blueprint, url_prefix='/auth')