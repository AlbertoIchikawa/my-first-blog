<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <v-container class="my-5">
      <v-card flat class="pa-3">
        <v-layout row wrap>
          <v-flex xs12 md6>
            <div class="caption grey--text">Project title</div>
            <div>Create a new website</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>The Net Ninja</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>1st jan 2020</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div>ongoing</div>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {};
</script>
