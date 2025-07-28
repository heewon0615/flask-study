from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://chloe:sewon0812^^@host/db_name'
db=SQLAlchemy(app)

# User 모델 생성
class User(db.Model):
    # 테이블 이름 직접 지정 (이 부분을 생략하면 기본적으로 클래스 이름을 소문자화한 'user'가 된다.)
    __tablename__ = 'users'
    # 컬럼 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # __repr__ : 객체의 문자열 표현을 정의, 콘솔에 객체를 출력할 때 이 메서드가 반환하는 형식대로 출력됨
    def __repr__(self):
        return '<User &r>' % self.username
    
    # 애플리케이션 컨텍스트 안에서 DB 테이블을 생성
    with app.app_context():
        # db.create_all() 메서드는 모델에 정의된 모든 테이블을 데이터베이스에 생성
        db.create_all()
        