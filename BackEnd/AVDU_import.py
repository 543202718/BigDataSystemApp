import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from app import app


@app.route('/AVDU_import', methods=['POST'])
def AVDU_import():
    print("AVDU_import_ok")
    dict = request.values.to_dict()
    # print(dict)
    code = insert(dict)
    response = make_response(
        jsonify(
            {
                'code': code
            }
        )
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


def insert(dict):
    code = 200
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="bigdata",
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 将数据插入project表
        sql, values = project(dict)
        cursor.execute(sql, values)
        # 将数据插入system表
        sql, values = system(dict)
        cursor.execute(sql, values)
        # 提交sql更新
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        code = 400
    # 关闭数据库连接
    db.close()
    return code


# Tips:
# 1. 在编写SQL语句时，对所有的表名和字段名都用``包裹（注意是英文模式下键盘左上角的符号，不是引号）。
# 2. 为了防止注入，不要自行拼接SQL语句，而是使用参数化语句，将%s作为占位符。
# 3. 注意字符串类型和数值类型的区别，在SQL语句中字符串需要加上引号（即'%s'）而数值不需要（即%s）。
# 4. 为了避免同一行的字符串过长，使用 \ 主动折行


# 生成将数据插入project表的SQL语句
def project(dict):
    sql = "insert into `project` (`id`, `name`, `description`, `place`, `owner`, \
        `owner_doc_no`) \
        values ('%s', '%s', '%s', '%s', '%s', \
        '%s')"
    values = [dict['deviceInfo[id]'], dict['deviceInfo[name]'], dict['deviceInfo[description]'],
              dict['deviceInfo[place]'], dict['deviceInfo[owner]'], dict['deviceInfo[owner_doc_no]']]
    return sql, values


# 生成将数据插入system表的SQL语句
def system(dict):
    sql = "insert into `system` (`project_id`, `system_id`, `type`, `designer`, `design_time`, \
        `name`, `property`, `design_stage`, `scale`, `set`, \
        `work_hour`, `flexibility`, `process_type`, `patentee`, `field`, \
        `technical_route`, `area`, `population`, `energy`) \
        values ('%s', '%s', '%s', '%s', '%s', \
        '%s', '%s', '%s', %s, %s, \
        %s, %s, '%s', '%s', '%s', \
        '%s', %s, %s, %s)"
    values = [dict['deviceInfo[project_id]'], dict['deviceInfo[system_id]'], dict['deviceInfo[type]'],
              dict['deviceInfo[designer]'], dict['deviceInfo[design_time]'],  # 第一行
              dict['deviceInfo[name]'], dict['deviceInfo[property]'], dict['deviceInfo[design_stage]'],
              dict['deviceInfo[scale]'], dict['deviceInfo[set]'],  # 第二行
              dict['deviceInfo[work_hour]'], dict['deviceInfo[flexibility]'], dict['deviceInfo[process_type]'],
              dict['deviceInfo[patentee]'], dict['deviceInfo[field]'],  # 第三行
              dict['deviceInfo[technical_route]'], dict['deviceInfo[area]'], dict['deviceInfo[population]'],
              dict['deviceInfo[energy]']]  # 第四行
    return sql, values
