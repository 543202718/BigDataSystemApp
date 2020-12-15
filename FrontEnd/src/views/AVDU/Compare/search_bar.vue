<template>
<div style="background:white">
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


    <br>
    <router-view></router-view>
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

    created: function () {
        console.log("turn to system page");
        console.log(this.$route.query);
        var id = this.$route.query.id
        this.$http
                .post(
                    "http://" + document.domain + ":5000/AVDU_detail", {
                        id: id,
                        //发送给后端的信息，可以按照需求增加条目
                    }, {
                        emulateJSON: true //必需，否则可能会json解析出错
                    }
                )
                .then(function (response) {
                    //response.body是报文的主体内容
                    if (parseInt(response.body.code) === 200) {
                        this.$message({
                            message: "查询成功",
                            type: "success",
                            duration: 3000,
                            showClose: true
                        })
                        console.log(response.body.systemInfo)
                        this.$store.search_systemInfo = response.body.systemInfo
                    } else {
                        this.$message({
                            message: "查询失败",
                            type: "error",
                            duration: 3000,
                            showClose: true
                        });
                    }
                });
        
    },
    methods: {
        toSystem() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/system");
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
            if (this.showErrorMessage(systemInfo, '装置概况')) return;
            var deviceInfo = this.$store.deviceInfo;
            if (this.showErrorMessage(deviceInfo, '主要设备')) return;
            var operation_conditionInfo = this.$store.operation_conditionInfo;
            if (this.showErrorMessage(operation_conditionInfo, '操作条件')) return;
            var materialInfo = this.$store.materialInfo;
            if (this.showErrorMessage(materialInfo, '原料性质')) return;
            var wasteInfo = this.$store.wasteInfo;
            if (this.showErrorMessage(wasteInfo, '三废排放')) return;
            var chemicalInfo = this.$store.chemicalInfo;
            if (this.showErrorMessage(chemicalInfo, '化学药剂')) return;
            var investmentInfo = this.$store.investmentInfo;
            if (this.showErrorMessage(investmentInfo, '装置投资')) return;
            var publicworkInfo = this.$store.publicworkInfo;
            if (this.showErrorMessage(publicworkInfo, '公用工程')) return;
            var productInfo = this.$store.productInfo;
            if (this.showErrorMessage(productInfo, '产品性质')) return;
            var balanceInfo = this.$store.balanceInfo;
            if (this.showErrorMessage(balanceInfo, '物料平衡')) return;
            var design_time = systemInfo.design_time;
            if (systemInfo.design_time instanceof Date) {
                systemInfo.design_time = this.dateFormat("YYYY-mm-dd", systemInfo.design_time); //格式化日期，否则传到后端会出错
            } else {
                systemInfo.design_time = "";
            }
            var Instance = this;
            this.$axios({
                method: "post",
                url: 'http://' + document.domain + ':5000/AVDU_import',
                data: {
                    systemInfo: systemInfo,
                    deviceInfo: deviceInfo,
                    operation_conditionInfo: operation_conditionInfo,
                    materialInfo: materialInfo,
                    wasteInfo: wasteInfo,
                    chemicalInfo: chemicalInfo,
                    investmentInfo: investmentInfo,
                    publicworkInfo: publicworkInfo,
                    productInfo: productInfo,
                    balanceInfo: balanceInfo,
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
                        message: '提交成功',
                        type: 'success',
                        duration: 3000,
                        showClose: true
                    });
                } else {
                    Instance.$message({
                        message: '提交失败，请检查您的输入',
                        type: 'error',
                        duration: 3000,
                        showClose: true
                    });
                }
            })
            systemInfo.design_time = design_time;
            console.log('submit!');
        },
        showErrorMessage(v, s) {
            if (typeof v === "undefined") {
                this.$message({
                    message: '提交失败，未保存' + s,
                    type: 'error',
                    duration: 3000,
                    showClose: true
                });
                return true;
            } else {
                return false;
            }
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
