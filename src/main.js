import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import Oruga from '@oruga-ui/oruga-next'

import { bulmaConfig } from '@oruga-ui/theme-bulma'
import '../sass/style.scss'


import { library, dom, } from '@fortawesome/fontawesome-svg-core';
import { faUser, faCopy, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faPython } from '@fortawesome/free-brands-svg-icons';

library.add(faUser, faGithub, faCopy, faTimesCircle, faPython);
dom.watch();


createApp(App)
    .use(store)
    .use(router)
    .use(Oruga, bulmaConfig)
    .mount('#app')
