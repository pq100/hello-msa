from datetime import datetime, timedelta
from typing import Optional

import bcrypt
import jwt
from sqlalchemy.orm import Session
from schema.user import UserLogin, Token
from models.user import User

# JWT 로그인 처리
def userlogin(login: UserLogin, db: Session):
    loginuser = db.query(User)\
        .filter(User.userid == login.userid).first()
    print(loginuser)

    if loginuser is None:   # 아이디가 일치하지 않으면
        token = None
    elif not bcrypt.checkpw(login.passwd.encode('utf-8'), loginuser.passwd):
        token = None
    else:
        # token = "{'access_token': 'hello, world',""'token_type': 'bearer'}"
        # token = Token(access_token='hello', token_type='bearer')
        access_token = generate_access_token(login.userid)
        token = Token(access_token=access_token, token_type='bearer')

    return token


# 비밀번호 함호화 함수
# bcrypt: 비밀번호 단방향 암호화에 자주 사용하는 패키지
# 암호화 방법: 사용자의 비밀번호 + bcryprt의 고유한 솔트
def hashed_password(passwd):
    SALT = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), SALT)
    print(hashed_password)

    return hashed_password


# JWT 엑세스 토큰 생성 (jwt.io)
# 엑세스 토큰 = 헤더 + 페이로드 + 시그니처
# 페이로드 : JWT의 중요한 구성요소 - 토큰에 저장한 사용자 정보 및 클레임 포함
# 등록된 클레임 : iss(발급 주체), sub(토큰 주제), aud(토큰 사용 가능 대상), exp(유효 기간), iat(발행 시간), jti(토큰 고유 식별자)
# pip install pyJWT
# expire_delta : 토큰 유지 기간
def generate_access_token(userid: str,
                          expire_delta: Optional[datetime]=None):
    # 토큰 생성 시 사용할 비밀키
    SECRETKEY = 'Hello, World!! 13579'


    # 토큰 유효기간 설정
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)


    # 토큰 발급
    to_encode = {'iss': 'http://127.0.0.1:3000', 'sub': userid, 'exp': expire, 'aud': 'http://127.0.0.1:3000'}  # jwt 페이로드
    encode_jwt = jwt.encode(to_encode, SECRETKEY, algorithm='HS256')

    return encode_jwt
