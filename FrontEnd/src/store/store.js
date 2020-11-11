import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isLoggedIn: false,
        account: '',
        deviceInfo: {
            tableCols: '',
            tableDatas: '',
        },
        systemInfo: null,
        operation_conditionInfo: {
            tableCols: null,
            tableDatas: null,
            operation_conditionInfo: null
        },
    },
    /*
    mutations: {
        login(state, account) {
            state.isLoggedIn = true;
            state.account = account;
        },
        logout(state) {
            state.isLoggedIn = false;
            state.account = '';
        },
    },
    actions: {

    }
    */
})