import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from app import app


@app.route('/AVDU_search', methods=['POST'])
def AVDU_search():
    print("AVDU_import_ok")
    dict = request.values.to_dict()
    print(dict)
    code, results = search(dict)
    # print("AVDU_import return code = %d" % (code))
    response = make_response(
        jsonify(
            {
                'code': code,
                'list': results
            }
        )
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


def search(dict):
    sql, values = genSQL(dict)
    results = None
    code = 200
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="@liudf57489sql", db="bigdata",
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        results = cursor.fetchall()
        print(results)
    except Exception as err:
        # 发生错误时回滚
        print(err)
        db.rollback()
        code = 400
    # 关闭数据库连接
    db.close()    
    return code,results




# 将输入字符串转化为int类型，如果无法转化就返回None


def toint(s):
    try:
        x = int(s)
    except:
        x = None
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


def genSQL(dict):
    system_type = tostring(dict['system_type'])
    process_type = tostring(dict['process_type'])
    density_l = tofloat(dict['density_l'])
    density_u = tofloat(dict['density_u'])
    acid_l = tofloat(dict['acid_l'])
    acid_u = tofloat(dict['acid_u'])
    s_l = tofloat(dict['s_l'])
    s_u = tofloat(dict['s_u'])

    sql = 'select `system`.`id`, `system`.`name`, `system`.`type`, `system`.`process_type`, \
        `material`.`density`, `material`.`acid`, `element`.`value` \
        from `system`, `material`,`element` where \
        `system`.`id`= `material`.`system_id`  \
        and `material`.`id` =  `element`.`material_id` \
        and `element`.`symbol` = \'S\' '
    values = []
    
    if system_type is not None:
        sql = sql + "and `system`.`type`= %s "
        values.append(system_type)

    if process_type is not None:
        sql = sql + "and `system`.`process_type`= %s "
        values.append(process_type)
    
    if density_u is not None:
        sql = sql + "and `material`.`density` <=  %s "
        values.append(density_u)

    if density_l is not None:
        sql = sql + "and `material`.`density`>= %s "
        values.append(density_l)

    if acid_u is not None:
        sql = sql + "and `material`.`acid` <=  %s "
        values.append(acid_u)

    if acid_l is not None:
        sql = sql + "and `material`.`acid`>= %s "
        values.append(acid_l)
   
    if s_u is not None:
        sql = sql + "and `element`.`value` <=  %s "
        values.append(s_u)

    if s_l is not None:
        sql = sql + "and `element`.`value`>= %s "
        values.append(s_l)

    return sql, values