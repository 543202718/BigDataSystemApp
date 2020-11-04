use bigdata;
-- 项目表
create table `project`(
    `id` varchar(50) primary key,     -- 项目号
    `name` varchar(50), -- 项目名称
    `description` text, -- 项目描述
    `place` varchar(100), -- 建设地点
    `owner` varchar(50), -- 业主单位
    `owner_doc_no` varchar(50) -- 业主文件号
);

-- 装置表
create table `system`(
    `id` int auto_increment primary key, -- 自增的内部id
    `project_id` varchar(50) , -- 项目号（外键）
    `system_id` varchar(50), -- 装置号
    `type` varchar(30) not null, -- 装置类型
    `designer` varchar(50), -- 设计单位
    `design_time` date, -- 设计完成时间
    `name` varchar(50), -- 装置名称
    `property` enum('新建','改扩建'), -- 装置性质
    `design_stage` enum('方案设计','可行性研究','基础设计','详细设计'), -- 设计阶段
    `scale` int, -- 装置规模，单位万吨/年
    `set` int, -- 装置系列
    `work_hour` int, -- 年开工时，单位小时
    `flexibility` varchar(30), -- 操作弹性，单位%
    `process_type` varchar(30), -- 工艺类型
    `patentee` varchar(50), -- 专利商
    `field` text, -- 装置范围
    `technical_route` text, -- 工艺技术路线
    `area` float, -- 占地面积，单位m^2
    `population` int, -- 装置定员
    `energy` float, -- 装置能耗，单位MJ/t进料
    `file_path` varchar(200), -- 原始文件路径
    foreign key (`project_id`) references `project`(`id`)
);

-- 材料性质简表
create table `material`(
    `id` int auto_increment primary key, -- 自增的原料号
    `system_id` int, -- 从属的装置id（外键）
    `name` varchar(50), -- 原料名称
    `density` float not null, -- 密度（20℃），单位kg/m^3
    `api` float, -- 比重指数API
    `solidifying` float, -- 凝点，单位℃
    `acid` float, -- 酸值，单位mgKOH/g
    `flash_open` float, -- 闪点（开口），单位℃
    `flash_close` float, -- 闪点（闭口），单位℃
    `ash` float, -- 灰分，单位%(m/m)
    `carbon` float, -- 残炭，单位%(m/m)
    `wax` float, -- 含蜡量，单位%(m/m)
    `salt` float, -- 盐含量，单位mg/L
    `sulfur` float, -- 硫醇硫，单位ppm
    `water` float, -- 水分，单位%(m/m)
    `precipitate` float, -- 沉淀，单位%(m/m)
    `calorific` float, -- 原油热值，单位kJ/kg
    `type` varchar(30), -- 原油类别
    `gum` float, -- 胶质，单位%(m/m)
    `asphaltene` float, -- 沥青质，单位%(m/m)
    foreign key (`system_id`) references `system`(`id`)
);

-- 原料元素含量表
create table `element`(
    `material_id` int, -- 原料号（外键）
    `symbol` varchar(5), -- 元素符号 
    `unit` varchar(20) not null, -- 单位
    `value` float not null, -- 含量值
    foreign key (`material_id`) references `material`(`id`),
    primary key (`material_id`,`symbol`)
);

-- 原料粘度简表
create table `viscosity_material`(
    `material_id` int, -- 原料号（外键）
    `tempature` float, -- 温度 
    `value` float not null, -- 粘度值
    foreign key (`material_id`) references `material`(`id`),
    primary key (`material_id`,`tempature`)
);

-- 原料轻烃组成表
create table `hydrocarbon`(
    `material_id` int, -- 原料号（外键）
    `name` varchar(20), -- 轻烃名称
    `unit` varchar(20) not null, -- 单位
    `value` float not null, -- 含量值
    foreign key (`material_id`) references `material`(`id`),
    primary key (`material_id`,`name`)
);

-- 原料性质详表
create table `material_detail`(
    `material_id` int, -- 原料号（外键）
    `boiling_range` varchar(30), -- 沸点范围
    `yield_fraction` float, -- 每馏分收率，单位%
    `yield_total` float, -- 总收率，单位%
    `density` float, -- 密度（20℃），单位kg/m^3
    `solidifying` float, -- 凝点，单位℃
    `acidity` float, -- 酸度，单位mgKOH/100ml
    `acid` float, -- 酸值，单位mgKOH/g
    `characteristic` float, -- 特质因数
    `related` float, -- 相关指数
    `api` float, -- 比重指数
    `refraction_t1` float, -- 温度1，用于折射率，单位℃
    `refraction_v1` float, -- 在温度1下的折射率
    `refraction_t2` float, -- 温度2，用于折射率，单位℃
    `refraction_v2` float, -- 在温度2下的折射率
    foreign key (`material_id`) references `material`(`id`),
    primary key (`material_id`,`boiling_range`)
);

-- 原料粘度详表
create table `viscosity_detail`(
    `material_id` int, -- 原料号（外键）
    `boiling_range` varchar(30), -- 沸点范围（外键）
    `tempature` float, -- 温度 
    `value` float not null, -- 粘度值
    foreign key (`material_id`,`boiling_range`) references `material_detail`(`material_id`,`boiling_range`),
    primary key (`material_id`,`boiling_range`,`tempature`)
);

-- 操作条件表
create table `operation_condition`(
	`name` varchar(30), -- 操作名称
    `system_id` int, -- 装置号（外键）
    `tower_name` varchar(30), -- 塔名    
    `unit` varchar(30), -- 单位
    `value` float not null, -- 值
    foreign key (`system_id`) references `system`(`id`),
    primary key (`name`,`system_id`,`tower_name`)
);

-- 化学药剂表
create table `chemical`(
	`name` varchar(30), -- 药剂名称
    `system_id` int, -- 装置号（外键）
    `unit` varchar(30), -- 单位
    `value` float not null, -- 值
    `type` varchar(30), -- 类别
    `pattern` varchar(30), -- 型号或规格
    `transport` enum('barrel','pipe'), -- 运输方式，桶装或管道
    `note` varchar(100), -- 备注
    foreign key (`system_id`) references `system`(`id`),
    primary key (`name`,`system_id`)
);

-- 三废排放表
create table `waste`(
	`name` varchar(30), -- 三废名称
    `system_id` int, -- 装置号（外键）
    `unit` varchar(30), -- 单位
    `value_con` float, -- 排放量
    `value_dis` float, -- 间断排放量
    `note` varchar(100), -- 备注
    foreign key (`system_id`) references `system`(`id`),
    primary key (`name`,`system_id`)
);

-- 公用工程表
create table `publicwork`(
	`name` varchar(30), -- 三废名称
    `system_id` int, -- 装置号（外键）
    `unit` varchar(30), -- 单位
    `value` float not null, -- 值
    `note` varchar(100), -- 备注
    foreign key (`system_id`) references `system`(`id`),
    primary key (`name`,`system_id`)
);

-- 装置投资表
create table `investment`(
	`system_id` int primary key, -- 装置号（外键） 
    `total` float not null, -- 工程项目总投资，单位万元
    `con_invest` float, -- 建设投资，单位万元
    `project_cost` float, -- 工程费用，单位万元
    `equipment_fee` float, -- 设备购置费，单位万元
    `installation_fee` float, -- 安装工程费，单位万元
    `construction_fee` float, -- 建筑工程费，单位万元
    `else` float, -- 其它费用，单位万元
    foreign key (`system_id`) references `system`(`id`)
);

-- 主要设备表
create table `device`(
	`type` varchar(30), -- 设备类型
    `system_id` int, -- 装置号（外键）
    `internal` int default 0 not null, -- 国内订货数
    `overseas` int default 0 not null, -- 国外订货数
	`note` varchar(100), -- 备注
    foreign key (`system_id`) references `system`(`id`)
);

-- 产品性质表
create table `product`(
	`id` int auto_increment primary key, -- 产品号
    `system_id` int, -- 装置号（外键）
    `name` varchar(30), -- 名称
    `density` float, -- 密度（20℃），单位kg/m^3
    `api` float, -- 比重指数
    `m_weight` float, -- 分子量
    `characteristic` float, -- 特质因数
    `acid` float, -- 酸值，单位mgKOH/g
    `sulfur_content` float, -- 硫含量，单位wt/%
    foreign key (`system_id`) references `system`(`id`)
);

-- 产品粘度表
create table `viscosity_product`(
    `product_id` int, -- 原料号（外键）
    `tempature` float, -- 温度 
    `value` float not null, -- 粘度值
    foreign key (`product_id`) references `product`(`id`),
    primary key (`product_id`,`tempature`)
);

-- 物料表
create table `balance_item`(
	`id` int auto_increment primary key, -- 物料号
    `name` varchar(30) not null, -- 名称
    `inout` enum('出方','入方') not null -- 出入方
);

-- 物料平衡表
create table `balance`(
	`item_id` int, -- 物料号（外键）
    `system_id` int, -- 装置号（外键）
    `cutting_range` varchar(30), -- 实沸点切割范围，单位℃
    `yield` float, -- 收率，单位m%
    `flow` float, -- 流率，单位万吨/年
    `note` varchar(200), -- 备注
    foreign key (`item_id`) references `balance_item`(`id`),
    foreign key (`system_id`) references `system`(`id`),
    primary key (`item_id`,`system_id`)
);









