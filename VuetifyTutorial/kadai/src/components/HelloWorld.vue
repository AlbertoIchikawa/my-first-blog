<template>
  <v-container>
    <v-btn large @click="greet" color="red">PUSH</v-btn>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    
  }),
  methods: {
      greet: function() {
        // メソッド内の `this` は、 Vue インスタンスを参照します
        alert("Alert表示課題 ");
        // `event` は、ネイティブ DOM イベントです
      }
    }

};
</script>
