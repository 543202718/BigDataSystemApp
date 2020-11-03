# BigDataSystemApp

## 环境安装

### MySQL数据库
+ 版本：8.0.21
+ 前置条件
  + 安装Visual Studio 2019 (https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=16)
  + 如果之前没有安装Python，可以在安装Visual Studio 2019时勾选Python开发，同时下载Python环境
+ 安装指南：https://www.runoob.com/w3cnote/windows10-mysql-installer.html
  + 大部分操作按照指南进行
  + 第15步设置密码为123456
  + 第16步新增管理员：
    + User Name: Admin
    + Host: localhost
    + Role: DB Admin
    + Password: 123456
  + 第22步配置mysql router不要勾选，直接点击next


### Python3
+ 版本：3.7.8
+ 注意，Python2和Python3不兼容，不要使用Python2编程
+ 如果已经在上一步中通过Visual Studio 2019下载了Python环境，那么将Python目录添加到环境变量中（控制面板-系统与安全-系统-高级系统设置-环境变量-系统变量-Path）。如果Visual Studio 2019安装在默认位置，那么Python目录应该是C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64
+ 为了使用pip3安装依赖，将Python目录下的Scripts目录也加入环境变量。如果Visual Studio 2019安装在默认位置，那么Python目录应该是C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts
+ 对于缺乏的依赖库，一律采用下列命令安装
  > pip3 install 依赖库名称

### Vue
+ 版本：2.6.12
+ 参考文档：https://cn.vuejs.org/v2/guide/
+ 采用npm和vue-cli构建项目
  + 下载npm：
    + 参考网页：https://www.runoob.com/vue2/vue-install.html
    + 先下载NodeJS，可以去[官网](https://nodejs.org/en/download/)下载，在Windows10平台上可以下载64位msi文件进行安装
    + 安装完毕后，可以在命令行中使用下面的命令判断是否安装成功
        > npm -v
  + 为了加快下载速度，使用淘宝npm镜像：
    > npm install -g cnpm --registry=https://registry.npm.taobao.org
  + 下载vue.js：
    > cnpm install -g vue  
    > cnpm install -g vue-cli
  + 下载elementUI
    > npm install element-ui -S
  + 下载vuex
    > npm install vuex --save
### Chrome浏览器
+ 版本：83.0.4103.97
+ 下载地址：https://www.google.cn/chrome/


## 系统框架
+ 数据使用MySQL数据库存储，我们建立了bigdata库用于存放我们的数据；
+ 后端通过数据库的默认端口（3306）访问数据库的数据；
+ 后端使用Python3和Flask，它会启动一个后台服务，根据前端的指令从数据库中读取数据；
+ 前端使用Flask的默认端口（5000）接受前端的指令；
+ 前端使用Vue搭建一个可供用户操作的网页，可以使用浏览器通过Vue的默认端口（8080）访问。



## 开始
1. 运行MySQL，建议使用可视化的WorkBench，建立连接，打开SQL/test.sql文件(File-Open SQL Script)并运行，就可以建立数据表并向其中添加示例数据；
2. 输入下面的命令运行后端：
    > python main.py
3. 输入下面的命令运行前端：
    > cnpm install   
    > cnpm run dev
4. 进入Chrome浏览器，在地址栏输入localhost:8080即可进入系统；
5. 点击“关于”按钮（目前只有这一个按钮是有效的），可以跳转到“项目人员”页面，显示一个包含本项目所有人员和对应身份的表格。

## 编程指南
参考已有的示例代码，一些关键点单独列在下方：

### 前端页面路由
+ 将需要路由的页面加入FrontEnd\src\router\index.js，格式可以仿照已有的条目
+ 在需要进行页面切换时，在javascript脚本中使用下面的方法进行切换
    ```js
    this.$router.push({path:'/author'});
    ```        

### 前后端交互
在前端使用下面的代码发送信息给后端，以及解析后端发送的响应报文：

```js
    this.$http.post('http://' + document.domain + ':5000/author', {
        type: "Search",
        //发送给后端的信息，可以按照需求增加条目
    },{  
        emulateJSON:true  //必需，否则可能会json解析出错
    }).then(function (response) {
        //response.body是报文的主体内容
        if (parseInt(response.body.code) === 200){
            ...      
        }                
    })
```

在后端使用下面的代码解析前端发送的信息，并发送响应报文：

```python
    # 解析前端发送的信息
    type=request.form['type']

    # 给前端发送响应报文
    response = make_response(jsonify({    
                                        'code':200,
                                        'msg':'ok'
                                        # 报文的主体，可以按需求增加条目
                                    })
                                )
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response
```

### 后端操作数据库
利用pymysql库操作MySQL数据库，教程见https://www.runoob.com/python3/python3-mysql.html。

一次SQL查询的Python代码如下：
```python
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
```
