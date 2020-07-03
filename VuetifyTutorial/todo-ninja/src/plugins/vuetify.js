import Vue from 'vue';
import Vuetify from 'vuetify/lib';
Vue.use(Vuetify);

export default new Vuetify({
    iconfont: 'md',
    theme: {
        themes: {
            light: {
                primary: "#9652ff",
                error: "#f83e70",
                info: "#ffaa2c",
                success: "#3cd1c2"
            },
        },
    }
}); 