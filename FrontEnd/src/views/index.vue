<template>
<div style="height: 100%">

    <el-header style="text-align: center; font-size: 20px">中石化典型装置数据结构化系统</el-header>

    <el-row style="height: 85%; background-color: white">
        <el-col :span="4" style="height: 100%; background-color: white; overflow: auto; text-align: left">
            <el-menu style="height: 100%" default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"   active-text-color="#ffd04b">
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-menu"></i>
                        <span>常减压装置</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="1-1" v-on:click="inputTemplate1">输入</el-menu-item>
                        <el-menu-item index="1-2">查询</el-menu-item>
                        <el-menu-item index="1-3">比对</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">重整装置</span>
                </el-menu-item>
                <el-menu-item index="3">
                    <i class="el-icon-menu"></i>
                    <span slot="title">加氢裂化装置</span>
                </el-menu-item>
                <el-menu-item index="4">
                    <i class="el-icon-menu"></i>
                    <span slot="title">蜡油加氢装置</span>
                </el-menu-item>
                <el-menu-item index="5">
                    <i class="el-icon-menu"></i>
                    <span slot="title">S-Zorb装置</span>
                </el-menu-item>
            </el-menu>
        </el-col>
    <el-col :span="20" style="height: 100%; background-color: white; overflow: auto;">
            <el-main>
                <router-view>
                    //嵌套子路由
                </router-view>
            </el-main>
        </el-col>
    </el-row>

    <el-footer style="height: 5%">
        <br>
        清华大学 软件学院<br />
   </el-footer>

</div>
</template>

<script>
export default {
    name: "Index",

    created() {
        console.log("get here")
    },

    methods: {
        inputTemplate1: function () {
            this.$router.push("/changjianya/input");
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        }
    }
};
</script>

<style>
.el-header {
height: 10%;
    text-align: left;
    padding: 13px;
    color:white;
}



.el-submenu .el-menu-item {
    min-width: 100px;
}

.el-footer {
    color: #fff;
}
</style>
