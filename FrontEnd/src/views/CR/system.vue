<template>
<div>
    <el-form ref="form" :model="systemInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="systemInfo.project_name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-input v-model="systemInfo.description" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
            </el-input>
        </el-form-item>
        <el-form-item label="项目号">
            <el-input v-model="systemInfo.id" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="建设地点">
            <el-input v-model="systemInfo.place" placeholder="例：某地"></el-input>
        </el-form-item>
        <el-form-item label="业主单位">
            <el-input v-model="systemInfo.owner" placeholder="例：xx科技有限公司">
            </el-input>
        </el-form-item>
        <el-form-item label="业主文件号">
            <el-input v-model="systemInfo.owner_doc_no"></el-input>
        </el-form-item>
        <el-form-item label="装置号">
            <el-input v-model="systemInfo.system_id"></el-input>
        </el-form-item>
        <el-form-item label="装置名称">
            <el-input v-model="systemInfo.system_name" placeholder="例：20200101"></el-input>
        </el-form-item>


        <el-form-item label="装置性质" style="text-align:left">
            <el-radio-group v-model="systemInfo.property">
                <el-radio-button label="新建"></el-radio-button>
                <el-radio-button label="改扩建"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="设计单位">
            <el-input v-model="systemInfo.designer" placeholder="例：SEI">
            </el-input>
        </el-form-item>
        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="systemInfo.design_time" style="width: 100%;"></el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="设计阶段" style="text-align:left">
            <el-radio-group v-model="systemInfo.design_stage">
                <el-radio-button label="可行性研究"></el-radio-button>
                <el-radio-button label="方案设计"></el-radio-button>
                <el-radio-button label="基础设计"></el-radio-button>
                <el-radio-button label="详细设计"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="装置总规模">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>




        <el-form-item label="1-预处理">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="2-重整">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="3-催化剂再生">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="4-苯抽提">
            <el-input v-model="systemInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>





        <el-form-item label="装置系列" style="text-align:left">
            <el-radio-group v-model="systemInfo.set">
                <el-radio-button label="1"></el-radio-button>
                <el-radio-button label="2"></el-radio-button>
                <el-radio-button label="3"></el-radio-button>
                <el-radio-button label="4"></el-radio-button>
            </el-radio-group>
        </el-form-item>



        <el-form-item label="年开工时">
            <el-input v-model="systemInfo.work_hour" placeholder="单位：小时"></el-input>
        </el-form-item>
        <el-form-item label="操作弹性">
            <el-input v-model="systemInfo.flexibility" placeholder="单位：%"></el-input>
        </el-form-item>



        <el-form-item label="工艺类型" style="text-align:left">
            <el-select v-model="systemInfo.process_type" filterable allow-create>
                <el-option label="半再生重整" value="半再生重整"></el-option>
                <el-option label="循环再生重整" value="循环再生重整"></el-option>
                <el-option label="连续再生重整" value="连续再生重整"></el-option>
            </el-select>
        </el-form-item>



        <el-form-item label="专利商">
            <el-input v-model="systemInfo.patentee"></el-input>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="催化重整包括环烷烃脱氢、烷烃环化脱氢、异构化、加氢裂化及积碳等反应" v-model="systemInfo.field"></el-input>
        </el-form-item>
        <el-form-item label="工艺技术路线">
            <el-input type="textarea" :rows="2" placeholder="预处理→重整" v-model="systemInfo.technical_route">
            </el-input>
        </el-form-item>

        <el-form-item label="占地面积">
            <el-input v-model="systemInfo.area" placeholder="单位:m^2"></el-input>
        </el-form-item>
        <el-form-item label="装置定员">
            <el-input v-model="systemInfo.population" placeholder="单位:人"></el-input>
        </el-form-item>
        <el-form-item label="装置能耗">
            <el-input v-model="systemInfo.energy" placeholder="单位:MJ/t进料"></el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="addToStore">暂存此页</el-button>

        </el-form-item>
    </el-form>
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
                system_id: '',
                system_name: '',
            //  system_type: '炼油装置（燃料油）',
                designer: '',
                design_time: '',
                property: '新建',
                design_stage: '可行性研究',
                scale: '',       //总规模
                scale_pre: '',   //预处理 preprocess
                scale_cr: '',    //重整   catalytic reforming
                scale_rg: '',    //再生   regenerate
                scale_be: '',    //苯抽提 benzene extraction
                set: '1',
                work_hour: '',
                flexibility: '',
                process_type: '半再生重整',
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
