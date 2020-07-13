// Core Components
import Toolbar from '../components/core/Toolbar.vue';
import Navigation from '../components/core/NavigationDrawer.vue';
import Breadcrumbs from '../components/core/Breadcrumbs.vue';
import PageFooter from '../components/core/PageFooter.vue';

import Widget from '../components/Widget.vue';
import SocialWidget from '../components/SocialWidget.vue';




import LocationStatistic from '../components/statistics/LocationStatistic.vue';
import SiteViewStatistic from '../components/statistics/SiteViewStatistic.vue';
import TotalEarningsStatistic from '../components/statistics/TotalEarningsStatistic.vue';

function setupComponents(Vue){

  Vue.component('toolbar', Toolbar);
  Vue.component('navigation', Navigation);
  Vue.component('breadcrumbs', Breadcrumbs);
  Vue.component('page-footer', PageFooter);
  Vue.component('widget', Widget);
  Vue.component('social-widget', SocialWidget);
 
  
  
  

  Vue.component('location-statistic', LocationStatistic);
  Vue.component('site-view-statistic', SiteViewStatistic);
  Vue.component('total-earnings-statistic', TotalEarningsStatistic);
}


export {
  setupComponents
}
