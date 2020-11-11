import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from app import app
import json

system_id = -1


@app.route('/AVDU_import', methods=['POST'])
def AVDU_import():
    print("AVDU_import_ok")
    dict = request.get_json()
    code = insert(dict)
    print("AVDU_import return code = %d" % (code))
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
        sql, values = project(dict['systemInfo'])
        cursor.execute(sql, values)
        # 将数据插入system表
        sql, values = system(dict['systemInfo'])
        cursor.execute(sql, values)
        # 获取system_id并保存在全局变量中
        cursor.execute("select last_insert_id()")
        result = cursor.fetchone()
        global system_id
        system_id = result['last_insert_id()']
        print(system_id)
        # 将数据插入device表
        for item in dict['deviceInfo']['tableDatas']:
            sql, values = device(item)
            cursor.execute(sql, values)
        # 将数据插入investment表
        # sql, values = investment(dict)
        # cursor.execute(sql, values)
        # 提交sql更新
        db.commit()
    except Exception as err:
        # 发生错误时回滚
        print(err)
        db.rollback()
        code = 400
    # 关闭数据库连接
    db.close()
    return code


# 将输入字符串转化为int类型，如果无法转化就返回None
def toint(s):
    try:
        x = int(s)
    except:
        x = None
    return x


# 将输入字符串转化为int类型，如果无法转化就返回0
def tointNotNone(s):
    try:
        x = int(s)
    except:
        x = 0
    return x


# 将输入字符串转化为float类型，如果无法转化就返回None
def tofloat(s):
    try:
        x = float(s)
    except:
        x = None
    return x


# 如果输入字符串是空串，就返回None
def tostring(s):
    if s == "":
        return None
    else:
        return s


# Tips:
# 1. 在编写SQL语句时，对所有的表名和字段名都用``包裹（注意是英文模式下键盘左上角的符号，不是引号）。
# 2. 为了防止注入，不要自行拼接SQL语句，而是使用参数化语句，将%s作为占位符。
# 3. 为了处理输入为空字符串和非法字符串（例如在数值类型的输入框中输入非数值字符串）的情况，所有的输入都需要根据类型采用
#   toint(), tofloat(), tostring() 方法进行处理，将它们都转化为None（即MySQL中的null）
# 4. 为了避免同一行的字符串过长，使用 \ 主动折行


# 生成将数据插入project表的SQL语句
def project(dict):
    sql = "insert into `project` (`id`, `name`, `description`, `place`, `owner`, `owner_doc_no`) \
        values (%s, %s, %s, %s, %s, %s)"
    values = [tostring(dict['id']),
              tostring(dict['project_name']),
              tostring(dict['description']),
              tostring(dict['place']),
              tostring(dict['owner']),
              tostring(dict['owner_doc_no'])]
    return sql, values


# 生成将数据插入system表的SQL语句
def system(dict):
    sql = "insert into `system` (`project_id`, `system_id`, `type`, `designer`, `design_time`, \
        `name`, `property`, `design_stage`, `scale`, `set`, \
        `work_hour`, `flexibility`, `process_type`, `patentee`, `field`, \
        `technical_route`, `area`, `population`, `energy`) \
        values (%s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, \
        %s, %s, %s, %s)"
    values = [tostring(dict['id']),
              tostring(dict['system_id']),
              tostring(dict['system_type']),
              tostring(dict['designer']),
              tostring(dict['design_time']),  # 第一行
              tostring(dict['system_name']),
              tostring(dict['property']),
              tostring(dict['design_stage']),
              toint(dict['scale']),
              toint(dict['set']),  # 第二行
              toint(dict['work_hour']),
              tostring(dict['flexibility']),
              tostring(dict['process_type']),
              tostring(dict['patentee']),
              tostring(dict['field']),  # 第三行
              tostring(dict['technical_route']),
              toint(dict['area']),
              toint(dict['population']),
              tofloat(dict['energy'])]
    return sql, values


# 生成将数据插入investment表的SQL语句
def investment(dict):
    # ToDO: 仿照project表完成即可
    pass


# 生成将数据插入device表的SQL语句
def device(dict):
    sql = "insert into `device` (`type`, `system_id`, `internal`, `overseas`, `note`)  \
        values (%s, %s, %s, %s, %s)"
    values = [tostring(dict['type']['content']),
              system_id,
              tointNotNone(dict['internal']['content']),
              tointNotNone(dict['overseas']['content']),
              tostring(dict['note']['content'])]
    return sql, values
