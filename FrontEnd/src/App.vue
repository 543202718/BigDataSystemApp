/* 入口界面 */ /* 这是一个视图(或者说组件和页面)，相当于一个容器 */ /*
在Vue中，官网叫它做组件，单页面的意思， *
是结构，样式，逻辑代码都写在同一个文件中， *
当我们引入这个文件后，就相当于引入对应的结构、样式和JS代码 */

<template>
<router-view></router-view>
</template>

<script>
import Index from "@/views/index.vue";
export default {
    name: "App",
    components: {
        Index
    }
};
</script>

<style>

  html, body, #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    background-color: #324057;
  }
</style>
