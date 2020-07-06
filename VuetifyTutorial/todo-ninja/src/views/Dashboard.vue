<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <v-container >
      <v-layout row wrap class="my-5" >
        <v-flex xs12 md6 >
          <v-btn outlined block color="primary">1</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn block outlined color="primary">2</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn block outlined color="primary">2</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn block outlined color="primary">2</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-space-around>
        <v-flex xs4 md3>
          <v-btn outlined block color="success">1</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outlined block color="success">2</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {};
</script>
