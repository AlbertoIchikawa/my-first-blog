<template>
  <div class="hello">
    <h1 class="text-center">{{ msg }}</h1>
    <h2 v-show="showText" class="text-center">{{ text }}</h2>
    <div align="center"><v-btn   rounded color="#008000"  @click="toggle">toggle</v-btn> <!--追加!!!!!!--></div>
    
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: '課題１のトグル機能',
      text: 'Test data',
      showText: false
    }
  },//こっから下追加！！！！！！！！
  methods: { 
    toggle: function () {
      this.showText = !this.showText
    }
  }
}
</script>