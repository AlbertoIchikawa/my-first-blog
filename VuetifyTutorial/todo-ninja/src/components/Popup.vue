<template>
  <v-dialog max-width="600px">
    <template v-slot:activator="{on}">
      <v-btn v-on="on" text slot="activator" class="success">Add new project</v-btn>
    </template>
    <v-card>
      <v-card-title>
        <h2>Add a New Project</h2>
      </v-card-title>
      <v-card-text>
        <v-form class="px-3" ref="form">
          <v-text-field label="Title" v-model="title" prepend-icon="folder" :rules="inputRules"></v-text-field>
          <v-textarea label="Information" v-model="content" prepend-icon="edit"  :rules="inputRules"></v-textarea>
          <v-menu>
            <template v-slot:activator="{ on, attrs }" >
              <v-text-field
                :rules="inputRules"
                :value="due"
                label="Due date"
                prepend-icon="date_range"
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="due"></v-date-picker>
          </v-menu>
          <v-btn text class="success mx-0 mt-3" @click="submit">Add project</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import format from "date-fns/format";
export default {
  data() {
    return {
      title: "",
      content: "",
      due: null,
      inputRules:[
        v => v && v.length >= 3 ||'Minimum length is 3 characters'
      ]
    };
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()){
          console.log(this.title, this.content)
      }
    }
  },
  computed: {
    formattedDate() {
      return this.due ? format(this.due, "Do MMM YYYY") : "";
    }
  }
};
</script>