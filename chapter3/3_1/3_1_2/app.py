from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://chloe:sewon0812@localhost/db_name'
db=SQLAlchemy(app)

# 여기서 모델 클래스를 정의
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
# Flask-Migrate 초기 설정
migrate = Migrate(app.db)