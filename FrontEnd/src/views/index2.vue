<template>
<div>

    <el-container>
        <el-header style="text-align: center; font-size: 20px">中石化典型装置数据结构化系统</el-header>
        <el-container>
            <el-aside width="350px">

                <el-row class="tac">
                    <el-col :span="12">
                        <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                            <el-submenu index="1">
                                <template slot="title">
                                    <i class="el-icon-menu"></i>
                                    <span>常减压装置</span>
                                </template>
                                <el-menu-item-group>
                                    <el-menu-item index="1-1" v-on:click="inputTemplate1" style="">输入</el-menu-item>
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
                </el-row>
            </el-aside>

            <el-main>
                <router-view>
                    //嵌套子路由
                </router-view>
            </el-main>

        </el-container>
    </el-container>
    <el-container>
        
        <el-footer>
            <br>
            清华大学 软件学院<br />
            2020年秋季学期<br />
            大数据系统基础课程项目<br /></el-footer>
    </el-container>

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
    background-color: #545c64;
    color: #fff;
    line-height: 60px;
}

.el-aside {
    overflow-y:hidden;
    height: 100%;
    width: auto;
}
.el-submenu .el-menu-item{
    min-width: 100px;
}
.el-footer {
    text-align:center;
    background-color: #545c64;
    font-family: "Fira Code", "汉仪南宫体简";
    font-size: 10px;
    color: darkgray;
    line-height: 100%;
}
</style>