<template>
<div>
    <el-form ref="form" :model="materialInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="原料名称">
            <el-input v-model="materialInfo.material_name" placeholder="例：沙轻和科威特混合原油"></el-input>
        </el-form-item>
        <el-form-item label="原料密度（20℃）">
            <el-input v-model="materialInfo.density" placeholder="单位：kg/m³">
            </el-input>
        </el-form-item>
        <el-form-item label="粘度">
            <el-input v-model="materialInfo.viscosity" placeholder="单位：m㎡/s"></el-input>
        </el-form-item>
        <el-form-item label="凝点">
            <el-input v-model="materialInfo.freezing_point" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="酸值">
            <el-input v-model="materialInfo.acid_value" placeholder="单位：mg KOH/g">
            </el-input>
        </el-form-item>
        <el-form-item label="闪点（开口）">
            <el-input v-model="materialInfo.flash_point_open" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="闪点（闭口）">
            <el-input v-model="materialInfo.flash_point_close" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="原油热值">
            <el-input v-model="materialInfo.heat_value" placeholder="单位：kJ/kg"></el-input>
        </el-form-item>
        <el-form-item label="原油类别">
            <el-input v-model="materialInfo.type" placeholder="例：低硫环烷中间基"></el-input>
        </el-form-item>
        <el-form-item label="灰分">
            <el-input v-model="materialInfo.ash" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="残炭">
            <el-input v-model="materialInfo.carbon_residual" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="含蜡量">
            <el-input v-model="materialInfo.wax_content" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="盐含量">
            <el-input v-model="materialInfo.salt_content" placeholder="单位：mg/L"></el-input>
        </el-form-item>
        <el-form-item label="硫醇硫">
            <el-input v-model="materialInfo.mercaptan_sulfur" placeholder="单位：ppm"></el-input>
        </el-form-item>
        <el-form-item label="水分">
            <el-input v-model="materialInfo.water" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="沉淀物">
            <el-input v-model="materialInfo.precipitate" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="胶质">
            <el-input v-model="materialInfo.colloid" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="沥青质">
            <el-input v-model="materialInfo.asphalt" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="元素组成">
        </el-form-item>
        <el-form-item label="H">
            <el-input v-model="materialInfo.H" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="C">
            <el-input v-model="materialInfo.C" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="S">
            <el-input v-model="materialInfo.S" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="N">
            <el-input v-model="materialInfo.N" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="Ni">
            <el-input v-model="materialInfo.Ni" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="V">
            <el-input v-model="materialInfo.V" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Ca">
            <el-input v-model="materialInfo.Ca" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Fe">
            <el-input v-model="materialInfo.Fe" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Cu">
            <el-input v-model="materialInfo.Cu" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Pb">
            <el-input v-model="materialInfo.Pb" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Mg">
            <el-input v-model="materialInfo.Mg" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Na">
            <el-input v-model="materialInfo.Na" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="轻烃组成">
        </el-form-item>
        <el-form-item label="甲烷">
            <el-input v-model="materialInfo.methane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="乙烷">
            <el-input v-model="materialInfo.ethane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="丙烷">
            <el-input v-model="materialInfo.propane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="正丁烷">
            <el-input v-model="materialInfo.n_butane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="异丁烷">
            <el-input v-model="materialInfo.isobutane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="正戊烷">
            <el-input v-model="materialInfo.n_pentane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="异戊烷">
            <el-input v-model="materialInfo.isopentane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="环戊烷">
            <el-input v-model="materialInfo.cyclopentane" placeholder="单位：v%"></el-input>
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
            materialInfo: {
                material_name: '',
                density: '',
                viscosity: '',
                freezing_point: '',
                acid_value: '',
                flash_point_open: '',
                flash_point_close:'',
                ash: '',
                carbon_residual: '',
                wax_content:'',
                salt_content:'',
                mercaptan_sulfur:'',
                water:'',
                precipitate:'',
                heat_value:'',
                type:'',
                colloid:'',
                asphalt:'',
                H:'',
                C:'',
                S:'',
                N:'',
                Ni:'',
                V:'',
                Ca:'',
                Fe:'',
                Cu:'',
                Pb:'',
                Mg:'',
                Na:'',
                methane:'',
                ethane:'',
                propane:'',
                n_butane:'',
                isobutane:'',
                n_pentane:'',
                isopentane:'',
                cyclopentane:'',
            },
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {},

}
</script>
