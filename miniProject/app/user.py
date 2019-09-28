from flask import Flask, render_template
import pymysql
import json



app = Flask(__name__)


def create_table():
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='1111',db='zimssa',charset='utf8')
    sql = '''
            CREATE TABLE USERS 
                (
                      USER_ID     VARCHAR(50)    NOT NULL PRIMARY KEY,
                      USER_NM     VARCHAR(200)    NOT NULL COMMENT '사용자명',
                      TEL_NO     VARCHAR(50)   COMMENT '전화번호',
                      EMAIL     VARCHAR(100)   COMMENT '이메일',
                      COMPNY_NM     VARCHAR(200)  COMMENT '회사명',
                      DEPT_NM     VARCHAR(200)   COMMENT '부서명',
                      JDEG_NM     VARCHAR(200)    COMMENT '직급명',
                      WORKING_SITE_NM   VARCHAR(200)  COMMENT '근무지역명',
                      REG_TM     TIMESTAMP   COMMENT '등록일시',
                      CHG_TM     TIMESTAMP   COMMENT '변경일시'
                 )ENGINE=InnoDB DEFAULT CHARSET=utf8
          ''' 
    try:
        with db.cursor() as cursor:
            cursor.execute(sql)
        db.commit()
    finally:
        db.close()

def drop_table():

    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='1111',db='zimssa',charset='utf8')
    
    try:
        with db.cursor() as cursor:
            sql = 'DROP TABLE USERS'
            cursor.execute(sql)
        db.commit()
#     print(cursor.rowcount) # 1 (affected rows)
    finally:
        db.close()


@app.route('/')
def hello():
	return render_template('test.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/use')
def use():
	return render_template('use.html')
	
if __name__ == '__main__':
	app.run(debug=True)

