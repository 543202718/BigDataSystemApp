<template>
<div>
    <table border="1" align="center">
        <caption>
            <h4>装置投资表</h4>
        </caption>
        <th> 项目 </th>
        <th> 金额（万元）</th>
        <tr>
            <td><b>工程项目总投资</b></td>
            <td>{{investmentInfo.total}}</td>
        </tr>
        <tr>
            <td><b>建设投资</b></td>
            <td>{{investmentInfo.con_invest}}</td>
        </tr>
        <tr>
            <td><b>工程费用</b></td>
            <td>{{investmentInfo.project_cost}}</td>
        </tr>
        <tr>
            <td><b>设备购置费</b></td>
            <td>{{investmentInfo.equipment_fee}}</td>
        </tr>
        <tr>
            <td><b>安装工程费</b></td>
            <td>{{investmentInfo.installation_fee}}</td>
        </tr>
        <tr>
            <td><b>建筑工程费</b></td>
            <td>{{investmentInfo.construction_fee}}</td>
        </tr>
        <tr>
            <td><b>其他费用</b></td>
            <td>{{investmentInfo.else}}</td>
        </tr>
    </table>
    <br>
</div>
</template>

<script>
export default {
    data() {
        return {
            investmentInfo: {
                system_id: '',
                total: '',
                con_invest: '',
                project_cost: '',
                equipment_fee: '',
                installation_fee: '',
                construction_fee: '',
                else: '',
            },
        };

    },

    created: function () {
        console.log("turn to investment page");
        // console.log(this.$store.search_investmentInfo.investmentInfo);
        this.investmentInfo = this.$store.search_investmentInfo;
        // console.log("the investment info: ");
        // console.log(this.investmentInfo);
    },
    methods: {},

}
</script>
