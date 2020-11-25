import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from app import app
import json

system_id = -1
material_id = -1


@app.route('/AVDU_import', methods=['POST'])
def AVDU_import():
    print("AVDU_import_ok")
    dict = request.get_json()
    # print(dict)
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
    print("open the database!!!")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 处理装置概况的输入
        handle_system(dict['systemInfo'], cursor)
        print("SystemInfo Done")
        # 处理原料性质的输入
        handle_material(dict['materialInfo'], cursor)
        print("MaterialInfo Done")
        # 处理产品性质的输入
        handle_product(dict['productInfo'], cursor)
        print("ProductInfo Done")
        # 处理物料平衡的输入
        handle_balance(dict['balanceInfo'], cursor)
        print("BalanceInfo Done")
        # 处理操作条件的输入
        handle_operation_condition(dict['operation_conditionInfo'], cursor)
        print("Operation_ConditionInfo Done")
        # 处理公用工程的输入
        handle_publicwork(dict['publicworkInfo'], cursor)
        print("PublicworkInfo Done")
        # 处理装置投资的输入
        handle_investment(dict['investmentInfo'], cursor)
        print("InvestmentInfo Done")
        # 处理主要设备的输入
        handle_device(dict['deviceInfo'], cursor)
        print("DeviceInfo Done")
        # 处理三废排放的输入
        handle_waste(dict['wasteInfo'], cursor)
        print("WasteInfo Done")
        # 处理化学药剂的输入
        handle_chemical(dict['chemicalInfo'], cursor)
        print("ChemicalInfo Done")
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


# 处理装置概况的输入
def handle_system(dict, cursor):
    # 将数据插入project表
    sql, values = project(dict)
    cursor.execute(sql, values)
    # 将数据插入system表
    sql, values = system(dict)
    cursor.execute(sql, values)
    # 获取system_id并保存在全局变量中
    cursor.execute("select last_insert_id()")
    result = cursor.fetchone()
    global system_id
    system_id = result['last_insert_id()']
    # print(system_id)
    return


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
    # print(dict)
    sql = "insert into `system` (`project_id`, `system_no`, `type`, `designer`, `design_time`, \
        `name`, `property`, `design_stage`, `scale`, `set`, \
        `work_hour`, `flexibility`, `process_type`, `patentee`, `field`, \
        `technical_route`, `area`, `population`, `energy`) \
        values (%s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, \
        %s, %s, %s, %s)"
    values = [tostring(dict['id']),
              tostring(dict['system_no']),
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


# 处理原料性质的输入
def handle_material(dict, cursor):
    # print(dict)
    # 将数据插入material表
    sql, values = material(dict['mainInfo'])
    cursor.execute(sql, values)
    # 获取material_id并写入全局变量
    cursor.execute("select last_insert_id()")
    result = cursor.fetchone()
    global material_id
    material_id = result['last_insert_id()']
    # print(material_id)
    # 将数据插入element表
    handle_element(dict['mainInfo'], cursor)
    # 将数据插入hydrocarbon表
    handle_hydrocarbon(dict['mainInfo'], cursor)
    # 将数据插入viscosity_material表
    handle_viscosity(dict['viscosity'], cursor)
    # 处理原料窄馏分性质的输入
    handle_material_detail(dict, cursor)
    # 处理原料窄馏分性质中的折射率
    handle_refraction_detail(dict, cursor)
    # 处理原料窄馏分性质中的粘度
    handle_viscosity_detail(dict, cursor)
    return


# 生成将数据插入material表的SQL语句
def material(dict):
    sql = "insert into `material` (`system_id`, `name`,  `density`,  `solidifying`, `acid`, \
        `flash_open`, `flash_close`, `ash`, `carbon`, `wax`, \
        `salt`, `sulfur`, `water`, `precipitate`, `calorific`, \
        `type`, `gum`, `asphaltene` ) \
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, %s, %s, %s, %s )"
    values = [system_id,
              tostring(dict['material_name']),
              tofloat(dict['density']),
              tofloat(dict['freezing_point']),
              tofloat(dict['acid_value']),  # 第一行
              tofloat(dict['flash_point_open']),
              tofloat(dict['flash_point_close']),
              tofloat(dict['ash']),
              tofloat(dict['carbon_residual']),
              tofloat(dict['wax_content']),  # 第二行
              tofloat(dict['salt_content']),
              tofloat(dict['mercaptan_sulfur']),
              tofloat(dict['water']),
              tofloat(dict['precipitate']),
              tofloat(dict['heat_value']),  # 第三行
              tostring(dict['type']),
              tofloat(dict['colloid']),
              tofloat(dict['asphalt'])]  # 第四行
    return sql, values


# 处理轻烃组成
def handle_hydrocarbon(dict, cursor):
    map = {"methane": "甲烷", "ethane": "乙烷", "propane": "丙烷",
           "n_butane": "正丁烷", "isobutane": "异丁烷", "n_pentane": "正戊烷",
           "isopentane": "异戊烷", "cyclopentane": "环戊烷"}
    sql = "insert into `hydrocarbon` (`material_id`, `name`, `unit`, `value`) values "
    values = []
    for k, v in map.items():
        value = tofloat(dict[k])
        if value != None:
            sql = sql + "(%s, %s, %s, %s),"
            values = values + [material_id, v, "v%", value]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理元素组成
def handle_element(dict, cursor):
    map = {"H": "w%", "C": "w%", "S": "w%", "N": "w%", "Ni": "μg/g",
           "V": "μg/g", "Ca": "μg/g", "Fe": "μg/g", "Cu": "μg/g",
           "Pb": "μg/g", "Mg": "μg/g", "Na": "μg/g"}
    sql = "insert into `element` (`material_id`, `symbol`, `unit`, `value`) values "
    values = []
    for k, v in map.items():
        value = tofloat(dict[k])
        if value != None:
            sql = sql + "(%s, %s, %s, %s),"
            values = values + [material_id, k, v, value]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理原料粘度
def handle_viscosity(dict, cursor):
    sql = "insert into `viscosity_material` (`material_id`, `tempature`, `value`) values "
    values = []
    for item in dict:
        temp = tofloat(item['temp'])
        value = tofloat(item['value'])
        if temp != None and value != None:
            sql = sql + "(%s, %s, %s),"
            values = values + [material_id, temp, value]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理原料窄馏分性质的输入
def handle_material_detail(dict, cursor):
    # material_detail表的SQL和数据
    sql = "insert into `material_detail` (`material_id`, `boiling_range`, \
            `yield_fraction`, `yield_total`, `density`, `solidifying`, `acidity`, `acid`, \
            `characteristic`, `related`, `api`) values "
    values = []
    # 处理表格中的数据
    for item in dict['tableDatas']:
        pk = tostring(item['boiling_point']['content'])
        if pk != None:
            # 将数据插入material_detail表
            sql = sql + "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s),"
            values = values + [
                material_id,
                pk,  # 第一行
                tofloat(item['yield']['content']),
                tofloat(item['yield_total']['content']),
                tofloat(item['density']['content']),
                tofloat(item['freezing_point']['content']),
                tofloat(item['acidity']['content']),
                tofloat(item['acid_value']['content']),  # 第二行
                tofloat(item['characteristic_index']['content']),
                tofloat(item['correlation_index']['content']),
                tofloat(item['API']['content'])
            ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理原料窄馏分性质中的粘度
def handle_viscosity_detail(dict, cursor):
    # 处理列名
    vis = processCol("vis", dict['viscosity_t'])
    # viscosity_detail表的SQL和数据
    sql = "insert into `viscosity_detail` (`material_id`, `boiling_range`, `tempature`, `value`) values "
    values = []
    for item in dict['tableDatas']:
        pk = tostring(item['boiling_point']['content'])
        if pk != None:
            for k, v in vis.items():
                value = tofloat(item[k]['content'])
                if value != None:
                    sql = sql + "(%s, %s, %s, %s),"
                    values = values + [material_id, pk, v, value]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理原料窄馏分性质中的折射率
def handle_refraction_detail(dict, cursor):
    # 处理列名
    re = processCol("re", dict['refract_t'])
    # refraction_detail表的SQL和数据
    sql = "insert into `refraction_detail` (`material_id`, `boiling_range`, `tempature`, `value`) values "
    values = []
    for item in dict['tableDatas']:
        pk = tostring(item['boiling_point']['content'])
        if pk != None:
            for k, v in re.items():
                value = tofloat(item[k]['content'])
                if value != None:
                    sql = sql + "(%s, %s, %s, %s),"
                    values = values + [material_id, pk, v, value]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 对列名进行预处理
def processCol(s, dict):
    map = {}
    for item in dict:
        map[s+item] = tofloat(item)
    return map


# 处理产品性质的输入
def handle_product(dict, cursor):
    for item in dict['tableDatas']:  # tableDatas中的item就是对应的每一行
        sql = " insert into `product` (`system_id`, `name`, `density`, \
            `api`, `m_weight`, `characteristic`, `acid`, `sulfur_content`, `note`) values \
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = [system_id,
                  tostring(item['product_name']['content']),
                  tofloat(item['density']['content']),
                  tofloat(item['API']['content']),
                  tofloat(item['molecular_weight']['content']),
                  tofloat(item['characteristic_factor']['content']),
                  tofloat(item['acid_value']['content']),
                  tofloat(item['sulfur_content']['content']),
                  tostring(item['remarks']['content'])
                  ]
        cursor.execute(sql, values)
        # 下面需要设置下product_id
        cursor.execute("select last_insert_id()")
        result = cursor.fetchone()
        product_id = result['last_insert_id()']
        visc = dict['viscosity_t']
        # print("visc:",visc)
        for i in range(len(visc)):
            value = tostring(item['vis' + visc[i]]['content'])
            if value != None:
                sql = "insert into `viscosity_product`(`product_id`, `temperature`, `value`) values\
                    (%s, %s, %s)"
                values = [product_id, visc[i], value]
                cursor.execute(sql, values)
    return


# 处理物料平衡的输入
def handle_balance(dict, cursor):
    # print(dict)
    sql = "insert into `balance` (`inout`, `name`, `system_id`, `cutting_range`, `yield`, \
        `flow1`, `flow2`, `flow3`, `note` ) values  "
    values = []
    for t in ['in', 'out']:
        for item in dict[t+'Datas']:
            sql = sql + "(%s, %s, %s, %s, %s, %s, %s, %s, %s),"
            values = values + [
                t,
                tostring(item['inward_or_outward_name']['content']),
                system_id,
                tostring(item['boiling_point_cutting_range']['content']),
                tofloat(item['yield']['content']),
                tofloat(item['flow_rate1']['content']),
                tofloat(item['flow_rate2']['content']),
                tofloat(item['flow_rate3']['content']),
                tostring(item['note']['content'])
            ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)


# 处理操作条件的输入
def handle_operation_condition(dict, cursor):
    map = {}
    for item in dict['tableCols']:
        if item['col'] == 'name' or item['col'] == 'unit':
            continue
        map[item['col']] = item['txt']
    # print(map)
    # 处理原油进电脱盐温度
    value = tofloat(dict['operation_conditionInfo']['CrudeOilToDesaltTemp'])
    if value != None:
        sql = 'insert into `operation_condition`(`name`, `system_id`, `tower_name`, `unit`, `value`) \
                values (%s, %s, %s, %s, %s)'
        values = ['原油进电脱盐温度', system_id, '__common__', '℃', value]
        cursor.execute(sql, values)
    # 处理闪底油进常压炉温度
    value = tofloat(dict['operation_conditionInfo']['FlasBotmToAtmoFurnTemp'])
    if value != None:
        sql = 'insert into `operation_condition`(`name`, `system_id`, `tower_name`, `unit`, `value`) \
                values (%s, %s, %s, %s, %s)'
        values = ['闪底油进常压炉温度', system_id, '__common__', '℃', value]
        cursor.execute(sql, values)
    # 处理下方的表格
    for item in dict['tableDatas']:
        # print(item)
        name = item['name']['content']
        unit = item['unit']['content']
        for k, v in item.items():
            value = tofloat(v['content'])
            if k == 'name' or k == 'unit' or value == None:
                continue
            sql = 'insert into `operation_condition`(`name`, `system_id`, `tower_name`, `unit`, `value`) \
                values (%s, %s, %s, %s, %s)'
            values = [
                name,
                system_id,
                tostring(map[k]),
                unit,
                value
            ]
            cursor.execute(sql, values)
    return


# 处理公用工程的输入 关注公用工程的 Note
def handle_publicwork(dict, cursor):
    # print(dict)
    # publicwork表的SQL和数据
    sql = "insert into `publicwork` (`name`,`system_id`,`unit`,`value`,`note`)\
        values "
    values = []
    for item in dict['tableDatas']:
        pk = tofloat(item['value']['content'])
        if pk !=None :
            sql = sql + "(%s, %s, %s, %s, %s),"
            values = values + [
                tostring(item['name']['content']),
                system_id,
                tostring(item['unit']['content']),
                tofloat(item['value']['content']),
                tostring(item['note']['content'])
            ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理装置投资的输入
# 装置投资 经检查 Front and Back :名称一致
def handle_investment(dict, cursor):
    # investment表的SQL和数据
    sql = "insert into `investment` (`system_id`,`total`,`con_invest`,`project_cost`,\
        `equipment_fee`,`installation_fee`,`construction_fee`,`else`) \
            values (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = [system_id,
              tofloat(dict['total']),
              tofloat(dict['con_invest']),
              tofloat(dict['project_cost']),
              tofloat(dict['equipment_fee']),
              tofloat(dict['installation_fee']),
              tofloat(dict['construction_fee']),
              tofloat(dict['else'])
              ]
    cursor.execute(sql, values)
    return


# 处理主要设备的输入
def handle_device(dict, cursor):
    sql = "insert into `device` (`type`, `system_id`, `internal`, `overseas`, `note`)  \
        values "
    values = []
    for item in dict['tableDatas']:
        sql = sql + "(%s, %s, %s, %s, %s),"
        values = values + [
            tostring(item['type']['content']),
            system_id,
            tointNotNone(item['internal']['content']),
            tointNotNone(item['overseas']['content']),
            tostring(item['note']['content'])
        ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)


# 处理三废排放的输入
def handle_waste(dict, cursor):
    sql = "insert into `waste` (`name`,`system_id`,`unit`,`value_con`,\
        `value_dis`, `note`) values "
    values = []
    for item in dict['tableDatas']:
        sql = sql + "(%s, %s, %s, %s, %s, %s),"
        values = values + [
            tostring(item['name']['content']),
            system_id,
            tostring(item['unit']['content']),
            tofloat(item['value']['content']),
            tofloat(item['CONTvalue']['content']),
            tostring(item['note']['content'])
        ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


# 处理化学药剂的输入
# 化学药剂 经检查 Front and Back 名称一致:
def handle_chemical(dict, cursor):
    # print(dict)
    sql = "insert into `chemical` (`name`, `system_id`, `unit`, `value`, `type`,\
        `pattern`, `transport`, `note`) values "
    values = []
    for item in dict['tableDatas']:
        value = tofloat(item['value']['content'])
        if value != None:
            sql = sql + "(%s, %s, %s, %s, %s, %s, %s, %s),"
            values = values + [
                tostring(item['name']['content']),
                system_id,
                tostring(item['unit']['content']),
                value,
                tostring(item['type']['content']),
                tostring(item['pattern']['content']),
                tostring(item['transport']['content']),
                tostring(item['note']['content'])
            ]
    if len(values) > 0:
        sql = sql.rstrip(",")
        cursor.execute(sql, values)
    return


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
# 4. 如果某字段为None而数据库要求not null，就不要插入该条记录
# 5. 为了避免同一行的字符串过长，使用 \ 主动折行
# 6. 为了提高数据库处理速度，需要向同一个表中插入多条数据时，应该使用批量插入语句而不是多次使用单插入语句
