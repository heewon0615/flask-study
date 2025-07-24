from flask import Flask, url_for

app = Flask(__name__)

# 뷰 함수 : 사용자 프로필 보여주기
@app.route('/user/<username>')
def show_user_profile(username):
    # 실제로는 사용자 프로필 정보를 보여주는 로직이 위치
    return f'User {username}'

# 뷰 함수 : 게시물 보여주기
@app.route('/post/<year>/<month>/<day>')
def show_post(year, month, day):
    return f'Post for {year}/{month}/{day}'

# 홈페이지에서 url_for를 이용하여 위의 뷰 함수들로 이동하는 링크 생성
@app.route('/')
def index():
    # 'show_user_profile' 뷰로 이동하는 URL 생성
    user_url = url_for('show_user_profile', username = 'chloe')
    # 'show_post' 뷰로 이동하는 URL 생성
    post_url = url_for('show_post', year = '2025', month = '07', day = '24')
    # 생성된 URL을 반환
    return f'''
        <a href="{user_url}">Go to User Profile</a><br>
        <a href="{post_url}">Go to Post</a>
    '''