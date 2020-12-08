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
            radio1:""
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
                        console.log(response.body.materialInfo)
                        console.log(response.body.balanceInfo)
                        this.$store.search_systemInfo = response.body.systemInfo;
                        this.$store.search_materialInfo = response.body.materialInfo;
                        this.$store.search_productInfo = response.body.productInfo
                        this.$store.search_balanceInfo = response.body.balanceInfo;
                        this.$store.search_operation_conditionInfo = response.body.operation_conditionInfo
                        this.$store.search_public_workInfo = response.body.public_workInfo
                        this.$store.search_deviceInfo = response.body.deviceInfo
                        this.$store.search_investmentInfo = response.body.investmentInfo
                        this.$store.search_wasteInfo = response.body.wasteInfo
                        this.$store.search_chemicalInfo = response.body.chemicalInfo
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
            this.$router.push("/AVDU/search/bar/material");
        },
        toBalance() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/balance");
        },
        toDevice() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/device");
        },
        toChemical() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/chemical");
        },
        toInvestment() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/investment");
        },
        toOperationCondition() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/operation_condition");
        },
        toProduct() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/product");
        },
        toPublicWork() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/public_work");
        },
        toWaste() {
            console.log("turn to system page, from input");
            this.$router.push("/AVDU/search/bar/waste");
        },       
       
    }
};
</script>

<style>
.el-form-item {
    border: lawngreen;

}
</style>
