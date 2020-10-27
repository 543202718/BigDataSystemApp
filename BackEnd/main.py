import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
app = Flask(__name__)

@app.route('/changjianya',methods = ['POST'])
def changjianya():
    return

@app.route('/author', methods=['POST'])
def author():
    results = getAuthor()
    response = make_response(
        jsonify(
            {
                'code': 200,
                'list':results
            }
        )
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


def getAuthor():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                        password="123456", db="bigdata",
                        charset='utf8', cursorclass = pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from st")
    # 使用 fetchall() 方法获取所有数据.
    results = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0')
