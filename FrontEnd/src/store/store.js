import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isLoggedIn: false,
        account: '',
        deviceInfo: {
            tableCols: null,
            tableDatas: null,
        },
        systemInfo: null,

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