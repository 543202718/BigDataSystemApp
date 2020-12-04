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
    dict = request.values.to_dict()
    print(dict)
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
                    'materialInfo': materialInfo(cursor)
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


def materialInfo(cursor):
    dict = {}
    # 从material表中获取指定system_id的记录
    sql = "select `id`, `name` as `material_name`,  `density`,  `solidifying` as `freezing_point`, `acid` as `acid_value`, \
        `flash_open` as `flash_point_open`, `flash_close` as `flash_point_close`, `ash`, `carbon`, `wax`, \
        `salt`, `sulfur`, `water`, `precipitate`, `calorific`, \
        `type`, `gum`, `asphaltene` from `material` where `system_id`= %s"
    cursor.execute(sql, [system_id])
    dict['mainInfo'] = cursor.fetchone()
    material_id = dict['mainInfo']['id']
    del dict['mainInfo']['id']
    # 从element表中获取指定material_id的记录
    sql = "select `symbol`, `value` from `element` where `material_id`=%s"
    cursor.execute(sql, [material_id])
    temp = cursor.fetchall()
    for item in temp:
        dict['mainInfo'][item['symbol']] = item['value']
    # 从hydrocarbon表中获取指定material_id的记录
    sql = "select `name`, `value` from `hydrocarbon` where `material_id` = %s"
    cursor.execute(sql, [material_id])
    temp = cursor.fetchall()
    map = {"methane": "甲烷", "ethane": "乙烷", "propane": "丙烷",
           "n_butane": "正丁烷", "isobutane": "异丁烷", "n_pentane": "正戊烷",
           "isopentane": "异戊烷", "cyclopentane": "环戊烷"}
    map = {v: k for k, v in map.items()}
    for item in temp:
        dict['mainInfo'][map[item['name']]] = item['value']
    # 从viscosity_material表中获取指定material_id的记录
    sql = "select `tempature`, `value` from `viscosity_material` where `material_id` = %s"
    cursor.execute(sql, [material_id])
    dict['viscosity']=cursor.fetchall()
    # 从material_detail表中获取指定material_id的记录
    sql = "select `boiling_range`, `yield_fraction`, `yield_total`, `density`,\
        `solidifying`, `acidity`, `acid`, \
        `characteristic`, `related`, `api` \
        from `material_detail` where `material_id` = %s "
    cursor.execute(sql, [material_id])
    dict['tableDatas'] = cursor.fetchall()
    # 从viscosity_detail表中获取指定material_id的记录
    sql = "select `boiling_range`, `tempature`, `value` from `viscosity_detail` \
        where `material_id` = %s"
    cursor.execute(sql, [material_id])
    temp = cursor.fetchall()
    s = set()
    for item in temp:
        s.add(item['tempature'])
        for row in dict['tableDatas']:
            if row['boiling_range']==item['boiling_range']:
                row['vis%d' %item['tempature']]=item['value']
                break
    dict['viscosity_t']=list(s)
    dict['viscosity_t'].sort()
    # 从refraction_detail表中获取指定material_id的记录
    sql = "select `boiling_range`, `tempature`, `value` from `refraction_detail` \
        where `material_id` = %s"
    cursor.execute(sql, [material_id])
    temp = cursor.fetchall()
    s = set()
    for item in temp:
        s.add(item['tempature'])
        for row in dict['tableDatas']:
            if row['boiling_range']==item['boiling_range']:
                row['re%d' %item['tempature']]=item['value']
                break
    dict['refract_t']=list(s)
    dict['refract_t'].sort()
    return dict


# 测试代码
if __name__ == '__main__':
    system_id = 2
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="bigdata",
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    print(materialInfo(cursor))
