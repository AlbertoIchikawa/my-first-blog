<template>
  <v-form v-model="valid" ref="form">
    <v-container>
      <v-layout>
        <v-flex xs6>
          <v-layout justify-space-between>
            メールアドレス
            <v-chip class="ml-0 mr-2 black--text" color="pink" label small>必須</v-chip>
          </v-layout>
        </v-flex>

        <v-flex>
          <v-text-field
            xs6
            field
            placeholder="例) example@pol-japan.co.jp"
            background-color="#EEEEEE"
            v-model="mail"
            :rules="inputRules"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs6>
          <v-layout justify-space-between>
            貴社・団体名
            <v-chip class="ml-0 mr-2 black--text" color="pink" label small>必須</v-chip>
          </v-layout>
        </v-flex>
        <v-flex>
          <v-text-field
            xs6
            field
            placeholder="例) ペネトレイト・オブ・リミット株式会社"
            background-color="#EEEEEE"
            v-model="company"
            :rules="inputRules"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs6>
          <v-layout justify-space-between>
            ご担当者名
            <v-chip class="ml-0 mr-2 black--text" color="pink" label small>必須</v-chip>
          </v-layout>
        </v-flex>
        <v-flex>
          <v-text-field xs6 field placeholder="例) 山田太郎" background-color="#EEEEEE" v-model="name" :rules="inputRules"></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs6>貴社URL</v-flex>
        <v-flex>
          <v-text-field
            xs6
            field
            placeholder="例) https://pol-japan.co.jp/"
            background-color="#EEEEEE"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs6>電話番号</v-flex>
        <v-flex>
          <v-text-field xs6 field placeholder="例) 03-6272-6871" background-color="#EEEEEE"></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs6>お問い合わせ内容</v-flex>
        <v-flex>
          <v-textarea xs6 field placeholder="お問い合わせ内容を記載してください。" background-color="#EEEEEE"></v-textarea>
        </v-flex>
      </v-layout>

      <v-layout justify-center>
        <v-btn large color="blue" class="align-center" @click="submit">確認する</v-btn>
      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      mail: "",
      company: "",
      name: "",
      inputRules: [v => !!v || "必須項目に入力してください"]
    };
  }
};
</script>