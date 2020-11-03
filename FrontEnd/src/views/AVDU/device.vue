<template>
<div>
    <el-form ref="form" :model="deviceInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="deviceInfo.project_name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-input v-model="deviceInfo.description" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
            </el-input>
        </el-form-item>
        <el-form-item label="项目号">
            <el-input v-model="deviceInfo.id" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="建设地点">
            <el-input v-model="deviceInfo.place" placeholder="例：某地"></el-input>
        </el-form-item>
        <el-form-item label="业主单位">
            <el-input v-model="deviceInfo.owner" placeholder="例：xx科技有限公司">
            </el-input>
        </el-form-item>
        <el-form-item label="业主文件号">
            <el-input v-model="deviceInfo.owner_doc_no"></el-input>
        </el-form-item>
        <el-form-item label="装置号">
            <el-input v-model="deviceInfo.system_id"></el-input>
        </el-form-item>
        <el-form-item label="装置名称">
            <el-input v-model="deviceInfo.system_name" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="装置类别" style="text-align:left">
            <el-select v-model="deviceInfo.system_type" filterable allow-create>
                <el-option label="炼油装置（燃料油）" value="炼油装置（燃料油）"></el-option>
                <el-option label="炼油装置（润滑油）" value="炼油装置（润滑油）"></el-option>
                <el-option label="化工装置" value="化工装置"></el-option>
                <el-option label="炼油化工一体化装置" value="炼油化工一体化装置"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="装置性质" style="text-align:left">
            <el-radio-group v-model="deviceInfo.property">
                <el-radio-button label="新建"></el-radio-button>
                <el-radio-button label="改扩建"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="设计单位">
            <el-input v-model="deviceInfo.designer" placeholder="例：SEI">
            </el-input>
        </el-form-item>
        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="deviceInfo.design_time" style="width: 100%;"></el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="设计阶段" style="text-align:left">
            <el-radio-group v-model="deviceInfo.design_stage">
                <el-radio-button label="可行性研究"></el-radio-button>
                <el-radio-button label="方案设计"></el-radio-button>
                <el-radio-button label="基础设计"></el-radio-button>
                <el-radio-button label="详细设计"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="装置规模">
            <el-input v-model="deviceInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="装置系列" style="text-align:left">
            <el-radio-group v-model="deviceInfo.set">
                <el-radio-button label="1"></el-radio-button>
                <el-radio-button label="2"></el-radio-button>
                <el-radio-button label="3"></el-radio-button>
                <el-radio-button label="4"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="年开工时">
            <el-input v-model="deviceInfo.work_hour" placeholder="单位：小时"></el-input>
        </el-form-item>
        <el-form-item label="操作弹性">
            <el-input v-model="deviceInfo.flexibility" placeholder="单位：%"></el-input>
        </el-form-item>
        <el-form-item label="工艺类型" style="text-align:left">
            <el-select v-model="deviceInfo.process_type" filterable allow-create>
                <el-option label="单常压装置" value="单常压装置"></el-option>
                <el-option label="单减压装置" value="单减压装置"></el-option>
                <el-option label="常减压装置" value="常减压装置"></el-option>
                <el-option label="双减压装置" value="双减压装置"></el-option>
            </el-select>
        </el-form-item>

        <el-form-item label="专利商">
            <el-input v-model="deviceInfo.patentee"></el-input>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="本装置主要由原油电脱盐脱水部分、换热网络及加热炉部分、常压蒸馏部分、减压蒸馏部分等组成，装置内考虑防腐设置有塔顶注氨、注缓蚀剂、注水设施。
" v-model="deviceInfo.field">
            </el-input>
        </el-form-item>
        <el-form-item label="工艺技术路线">
            <el-input type="textarea" :rows="2" placeholder="原油进料→电脱盐→闪蒸塔→常压塔→减压塔
" v-model="deviceInfo.technical_route">
            </el-input>
        </el-form-item>
        <el-form-item label="占地面积">
            <el-input v-model="deviceInfo.area" placeholder="单位:m^2"></el-input>
        </el-form-item>
        <el-form-item label="装置定员">
            <el-input v-model="deviceInfo.population" placeholder="单位:人"></el-input>
        </el-form-item>
        <el-form-item label="装置能耗">
            <el-input v-model="deviceInfo.energy" placeholder="单位:MJ/t进料"></el-input>
        </el-form-item>
        <!--
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
-->
    </el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            deviceInfo: {
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
    },
    methods: {},

}
</script>
