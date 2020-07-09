<template>
  <v-footer height="auto" color="#21252F">
    <v-container>
      <v-layout wrap>
      <v-flex >
        <v-card class="text-xs-center" flat tile :color="$root.themeColor" >
          <v-img >
            <img
              src="https://pol-japan.co.jp/wp-content/themes/pol/assets/img/common/footer_logo.svg"
              alt="POL"
            />
          </v-img>
        </v-card>
        <v-card-text class="white--text">
          <div>ペネトレイト・オブ・リミット株式会社</div>
          <div>〒104-0033 東京都中央区新川2-9-6 シュテルン中央ビル 3F</div>
        </v-card-text>
      </v-flex>

      <v-flex  class="text-xs-center">
        <v-card-text class="white--text">
          Follow Us
          <v-btn v-for="icon in icons" :key="icon" class="mx-1 white--text" icon>
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-text>
        <v-card-text  class="white--text ">© 2011-2020 Penetrate of Limits Co.,Ltd.</v-card-text>
      </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      icons: ["fab fa-facebook", "fab fa-twitter", "fab fa-instagram"]
    };
  }
};
</script>

<style>
</style>
