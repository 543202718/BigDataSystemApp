<template>
<div>
    
    <el-container>
        <el-header>中石化典型装置数据结构化系统</el-header>
        <el-container>
            <el-aside width="400px">

                <el-row class="tac">
                    <el-col :span="12">
                        <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                            <el-submenu index="1">
                                <template slot="title">
                                    <i class="el-icon-location"></i>
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
                                <i class="el-icon-document"></i>
                                <span slot="title">加氢裂化装置</span>
                            </el-menu-item>
                            <el-menu-item index="4">
                                <i class="el-icon-setting"></i>
                                <span slot="title">蜡油加氢装置</span>
                            </el-menu-item>
                            <el-menu-item index="5">
                                <i class="el-icon-setting"></i>
                                <span slot="title">S-Zorb装置</span>
                            </el-menu-item>
                        </el-menu>
                    </el-col>
                </el-row>
            </el-aside>
            <el-container>
                <el-main>
                    <router-view>
                        //嵌套子路由
                    </router-view>
                </el-main>
            </el-container>
        </el-container>
    </el-container>

</div>
</template>

<script>
export default {
    name: "Index",
    data() {
        return {
            items: []
        };
    },
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
    background-color:#545c64;
    color: #fff;
    line-height: 60px;
  }</style>
