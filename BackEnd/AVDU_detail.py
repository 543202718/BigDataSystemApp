import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from app import app
import json

system_id = -1


@app.route('/AVDU_detail', methods=['POST'])
def AVDU_detail():
    print("AVDU_detail_ok")
    dict = request.get_json()
    global system_id
    system_id = dict['id']
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="bigdata",
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        response = make_response(
            jsonify(
                {
                    'code': 200,
                    'systemInfo': systemInfo(cursor),
                }
            )
        )
    except Exception as ex:
        # 查询过程中出现异常，只返回错误码400
        print(ex)
        response = make_response(
            jsonify(
                {
                    'code': 400
                }
            )
        )
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


def systemInfo(cursor):
    dict = {}
    # 从system表中获取指定system_id的记录
    sql = "select `project_id`, `system_no`, `type` as `system_type`, `designer`, `design_time`, \
        `name` as `system_name`, `property`, `design_stage`, `scale`, `set`, \
        `work_hour`, `flexibility`, `process_type`, `patentee`, `field`, \
        `technical_route`, `area`, `population`, `energy` from `system` \
        where `id` = %s "
    cursor.execute(sql, [system_id])
    dict.update(cursor.fetchone())
    # 从project表中获取指定project_id的记录，project_id来自system表的外键
    sql = "select `id`, `name` as `project_name`, `description`, `place`, `owner`, `owner_doc_no` \
        from `project` where `id` = %s "
    cursor.execute(sql, [dict['project_id']])
    dict.update(cursor.fetchone())
    # 删除重复的字段
    del dict['project_id']
    return dict


# 测试代码
if __name__ == '__main__':
    system_id = 8
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="bigdata",
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    print(systemInfo(cursor))
