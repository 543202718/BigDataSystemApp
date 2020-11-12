<template>
<div>
    <el-radio-group v-model="radio1">
        <el-radio-button @click.native="toSystem" label="装置概况"></el-radio-button>
        <el-radio-button @click.native="toMaterial" label="原料性质"></el-radio-button>
        <el-radio-button @click.native="toProduct" label="产品性质"></el-radio-button>
        <el-radio-button @click.native="toBalance" label="物料平衡"></el-radio-button>
        <el-radio-button @click.native="toOperationCondition" label="操作条件"></el-radio-button>
        <br>
        <el-radio-button @click.native="toPublicWork" label="公用工程"></el-radio-button>
        <el-radio-button @click.native="toInvestment" label="装置投资"></el-radio-button>
        <el-radio-button @click.native="toDevice" label="主要设备"></el-radio-button>
        <el-radio-button @click.native="toWaste" label="三废排放"></el-radio-button>
        <el-radio-button @click.native="toChemical" label="化学药剂"></el-radio-button>
    </el-radio-group>

    <el-button type="primary" @click="onSubmit">立即创建</el-button>

    <br>

    <router-view></router-view>
    <!--
    <el-form v-if='false' ref="form" :model="systemInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="systemInfo.project_name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-input v-model="systemInfo.description" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
            </el-input>
        </el-form-item>
        <el-form-item label="项目号">
            <el-input v-model="systemInfo.id" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="建设地点">
            <el-input v-model="systemInfo.place" placeholder="例：某地"></el-input>
        </el-form-item>
        <el-form-item label="业主单位">
            <el-input v-model="systemInfo.owner" placeholder="例：xx科技有限公司">
            </el-input>
        </el-form-item>
        <el-form-item label="业主文件号">
            <el-input v-model="systemInfo.owner_doc_no"></el-input>
        </el-form-item>
        <el-form-item label="装置号">
            <el-input v-model="systemInfo.system_id"></el-input>
        </el-form-item>
        <el-form-item label="装置名称">
            <el-input v-model="systemInfo.system_name" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="装置类别" style="text-align:left">
            <el-select v-model="systemInfo.system_type" filterable allow-create>
                <el-option label="炼油装置（燃料油）" value="炼油装置（燃料油）"></el-option>
                <el-option label="炼油装置（润滑油）" value="炼油装置（润滑油）"></el-option>
                <el-option label="化工装置" value="化工装置"></el-option>
                <el-option label="炼油化工一体化装置" value="炼油化工一体化装置"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="装置性质" style="text-align:left">
            <el-radio-group v-model="systemInfo.property">
                <el-radio-button label="新建"></el-radio-button>
                <el-radio-button label="改扩建"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="设计单位">
            <el-input v-model="systemInfo.designer" placeholder="例：SEI">
            </el-input>
        </el-form-item>
        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="systemInfo.design_time" style="width: 100%;"></el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="设计阶段" style="text-align:left">
            <el-radio-group v-model="systemInfo.design_stage">
                <el-radio-button label="可行性研究"></el-radio-button>
                <el-radio-button label="方案设计"></el-radio-button>
                <el-radio-button label="基础设计"></el-radio-button>
                <el-radio-button label="详细设计"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="装置规模">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="装置系列" style="text-align:left">
            <el-radio-group v-model="systemInfo.set">
                <el-radio-button label="1"></el-radio-button>
                <el-radio-button label="2"></el-radio-button>
                <el-radio-button label="3"></el-radio-button>
                <el-radio-button label="4"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="年开工时">
            <el-input v-model="systemInfo.work_hour" placeholder="单位：小时"></el-input>
        </el-form-item>
        <el-form-item label="操作弹性">
            <el-input v-model="systemInfo.flexibility" placeholder="单位：%"></el-input>
        </el-form-item>
        <el-form-item label="工艺类型" style="text-align:left">
            <el-select v-model="systemInfo.process_type" filterable allow-create>
                <el-option label="单常压装置" value="单常压装置"></el-option>
                <el-option label="单减压装置" value="单减压装置"></el-option>
                <el-option label="常减压装置" value="常减压装置"></el-option>
                <el-option label="双减压装置" value="双减压装置"></el-option>
            </el-select>
        </el-form-item>

        <el-form-item label="专利商">
            <el-input v-model="systemInfo.patentee"></el-input>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="本装置主要由原油电脱盐脱水部分、换热网络及加热炉部分、常压蒸馏部分、减压蒸馏部分等组成，装置内考虑防腐设置有塔顶注氨、注缓蚀剂、注水设施。
" v-model="systemInfo.field">
            </el-input>
        </el-form-item>
        <el-form-item label="工艺技术路线">
            <el-input type="textarea" :rows="2" placeholder="原油进料→电脱盐→闪蒸塔→常压塔→减压塔
" v-model="systemInfo.technical_route">
            </el-input>
        </el-form-item>
        <el-form-item label="占地面积">
            <el-input v-model="systemInfo.area" placeholder="单位:m^2"></el-input>
        </el-form-item>
        <el-form-item label="装置定员">
            <el-input v-model="systemInfo.population" placeholder="单位:人"></el-input>
        </el-form-item>
        <el-form-item label="装置能耗">
            <el-input v-model="systemInfo.energy" placeholder="单位:MJ/t进料"></el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>

    </el-form>
-->
</div>
</template>

<script>
export default {

    data() {
        return {
            show: [true, false, false],
            radio1: '装置概况',
            systemInfo: {
                id: '',
                project_name: '',
                description: '',
                place: '',
                owner: '',
                owner_doc_no: '',
                system_id: '',
                system_name: '',
                system_type: '炼油装置（燃料油）',
                designer: '',
                design_time: '',
                property: '新建',
                design_stage: '可行性研究',
                scale: '',
                set: '1',
                work_hour: '',
                flexibility: '',
                process_type: '常减压装置',
                patentee: '',
                field: '',
                technical_route: '',
                area: '',
                population: '',
                energy: '',
                file_path: '',
            },

        };
    },
    methods: {
        toSystem() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/system");
        },
        toMaterial() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/material");
        },
        toBalance() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/balance");
        },
        toDevice() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/device");
        },
        toChemical() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/chemical");
        },
        toInvestment() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/investment");
        },
        toOperationCondition() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/operation_condition");
        },
        toProduct() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/product");
        },
        toPublicWork() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/public_work");
        },
        toWaste() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/waste");
        },
        dateFormat(fmt, date) {
            let ret;
            const opt = {
                "Y+": date.getFullYear().toString(), // 年
                "m+": (date.getMonth() + 1).toString(), // 月
                "d+": date.getDate().toString(), // 日
                "H+": date.getHours().toString(), // 时
                "M+": date.getMinutes().toString(), // 分
                "S+": date.getSeconds().toString() // 秒
                // 有其他格式化字符需求可以继续添加，必须转化成字符串
            };
            for (let k in opt) {
                ret = new RegExp("(" + k + ")").exec(fmt);
                if (ret) {
                    fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
                };
            };
            return fmt;
        },
        onSubmit() {

            var systemInfo = this.$store.systemInfo;
            var deviceInfo = this.$store.deviceInfo;
            var operation_conditionInfo = this.$store.operation_conditionInfo;
            var materialInfo = this.$store.materialInfo;
            console.log(operation_conditionInfo);
            if (this.systemInfo.design_time instanceof Date) {
                this.systemInfo.design_time = this.dateFormat("YYYY-mm-dd", this.systemInfo.design_time); //格式化日期，否则传到后端会出错
            } else {
                this.systemInfo.design_time = "";
            }
            var Instance = this;
            this.$axios({
                method: "post",
                url: 'http://' + document.domain + ':5000/AVDU_import',
                data: {
                    systemInfo: systemInfo,
                    // deviceInfo: deviceInfo,
                    // operation_conditionInfo: operation_conditionInfo,
                    materialInfo: materialInfo,
                },
                //发送给后端的信息，可以按照需求增加条目
                header: {
                    'Content-Type': 'application/json' //如果写成contentType会报错
                }
            }).then(function (response) {
                //response.body是报文的主体内容
                console.log(response);
                if (parseInt(response.data.code) === 200) {
                    Instance.$message({
                        message: '创建成功',
                        type: 'success',
                        duration: 3000,
                        showClose: true
                    });
                } else {
                    Instance.$message({
                        message: '创建失败，请检查您的输入',
                        type: 'error',
                        duration: 3000,
                        showClose: true
                    });
                }
            })
            console.log('submit!');
        },
        changeFormShow(showFormID) {
            console.log('change showed form');
            this.show = [false, false, false]
            this.show[showFormID] = true;
            console.log(this.show);
        }
    }
};
</script>

<style>
.el-form-item {
    border: lawngreen;

}
</style>
