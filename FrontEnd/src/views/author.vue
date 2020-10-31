<template>
    <div>
        <h1>项目人员</h1>
        <table border="1" align="center">
            <tr v-for="item in items" :key="item">
                <td>{{ item.identity }}</td>
                <td>{{ item.name }}</td>
            </tr>
        </table>
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
        console.log('start fetch data');
        this.$http
            .post(
                "http://" + document.domain + ":5000/author",
                {
                    type: "Search"
                    //发送给后端的信息，可以按照需求增加条目
                },
                {
                    emulateJSON: true //必需，否则可能会json解析出错
                }
            )
            .then(function(response) {
                //response.body是报文的主体内容
                if (parseInt(response.body.code) === 200) {
                    this.items = response.body.list;
                    // this.items = this.items.concat(response.body.list);
                    console.log(this.items);
                }
            });
    }
};
</script>

<style></style>
