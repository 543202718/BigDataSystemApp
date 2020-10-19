<template>
    <div>
        <h1>中石化数据决策支持系统</h1>
        <div v-html="message"></div>
        <br />
        <div>
            <button class="buttonred">
                <span>常减压装置</span>
            </button>
            <button class="buttonred">
                <span>重整装置</span>
            </button>
            <button class="buttonred">
                <span>加氢裂化装置</span>
            </button>
            <br>
            <button class="buttonred">
                <span>蜡油加氢装置</span>
            </button>
            <button class="buttonred">
                <span>S-Zorb装置</span>
            </button>
            <button class="buttonred" v-on:click="goAuthor">
                <span>关于</span>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Index",
    data() {
        return {
            type: "",
            message: ""
        };
    },
    methods: {
        goAuthor: function() {
            this.$router.push("/author");
        },
    }
};
</script>

<style>
.buttonred {
    font-family: "Fira Code", "汉仪南宫体简";
    display: inline-block;
    border-radius: 4px;
    background-color: #f4511e;
    border: none;
    color: #ffffff;
    text-align: center;
    font-size: 18px;
    padding: 20px;
    width: 250px;
    transition: all 0.5s;
    cursor: pointer;
    margin: 5px;
}

.buttonred span {
    cursor: pointer;
    display: inline-block;
    position: relative;
    transition: 0.5s;
}
.buttonred:hover span:after {
    opacity: 1;
    right: 0;
}
.buttonred span:after {
    content: "»";
    position: absolute;
    opacity: 0;
    top: 0;
    right: -20px;
    transition: 0.5s;
}

.buttonred:hover span {
    padding-right: 25px;
}

.buttonred:hover span:after {
    opacity: 1;
    right: 0;
}
</style>
