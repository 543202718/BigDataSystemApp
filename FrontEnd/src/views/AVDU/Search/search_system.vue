<template>
<div id="search" style="background:white">
    <table border="1" align="center">
        <caption>
            <h4>装置概况</h4>
        </caption>
        <tr>
            <td colspan="1"><b>项目名称</b></td>
            <td colspan="6">{{systemInfo.project_name}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>项目描述</b></td>
            <td colspan="6">{{systemInfo.description}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>项目号</b></td>
            <td colspan="6">{{systemInfo.id}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>建设地点</b></td>
            <td colspan="6">{{systemInfo.place}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>业主单位</b></td>
            <td colspan="6">{{systemInfo.owner}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>业主文件号</b></td>
            <td colspan="6">{{systemInfo.owner_doc_no}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置号</b></td>
            <td colspan="6">{{systemInfo.system_no}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置名称</b></td>
            <td colspan="6">{{systemInfo.system_name}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置类别</b></td>
            <td colspan="6">{{systemInfo.system_type}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置性质</b></td>
            <td colspan="6">{{systemInfo.property}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>设计单位</b></td>
            <td colspan="6">{{systemInfo.designer}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>设计完成时间</b></td>
            <td colspan="6">{{systemInfo.design_time}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>设计阶段</b></td>
            <td colspan="6">{{systemInfo.design_stage}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置规模</b></td>
            <td colspan="6">{{systemInfo.scale}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置系列</b></td>
            <td colspan="6">{{systemInfo.set}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>年开工时</b></td>
            <td colspan="6">{{systemInfo.work_hour}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>操作弹性</b></td>
            <td colspan="6">{{systemInfo.flexibility}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>工艺类型</b></td>
            <td colspan="6">{{systemInfo.process_type}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>专利商</b></td>
            <td colspan="6">{{systemInfo.patentee}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置范围</b></td>
            <td colspan="6">{{systemInfo.field}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>工艺技术路线</b></td>
            <td colspan="6">{{systemInfo.technical_route}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>占地面积</b></td>
            <td colspan="6">{{systemInfo.area}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置定员</b></td>
            <td colspan="6">{{systemInfo.population}}</td>
        </tr>
        <tr>
            <td colspan="1"><b>装置能耗</b></td>
            <td colspan="6">{{systemInfo.energy}}</td>
        </tr>

        <!-- 类似的做完剩下的属性 -->
    </table>
    
</div>
</template>

<script>
export default {
    data() {
        return {
            systemInfo: {
                id: '',
                project_name: '',
                description: '',
                place: '',
                owner: '',
                owner_doc_no: '',
                system_no: '',
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
        
        this.systemInfo = this.$store.search_systemInfo;

    },
    methods: {
        addToStore: function () {
            this.$store.systemInfo = this.systemInfo;
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store systemInfo to device');
        }
    },

}
</script>
