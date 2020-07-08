<template>
  <div class="team">
    <v-subheader class="grey--text">Team</v-subheader>

    <v-container class="my-5">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3 v-for="person in team" :key="person.name">
          <v-card class="text-center ma-3">
            <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <img :src="person.avatar">
              </v-avatar>
            </v-responsive>
            <v-card-text>
              <div class="subheading">{{ person.name }}</div>
              <div class="grey--text">{{ person.role }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="grey">
                <v-icon small left>message</v-icon>
                <span>Message</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  data() {
    return {
      team: [
        { name: "The Net Ninja", role: "Web developer" , avatar: '/icon1.jpg'},
        { name: "Ryu", role: "Graphic designer" , avatar: '/icon2.jpg'},
        { name: "Chun Li", role: "Web developer" , avatar: '/icon3.jpg'},
        { name: "Gouken", role: "Social media maverick" , avatar: '/icon4.jpg'},
        { name: "Yoshi", role: "Sales guru" , avatar: '/icon5.jpg'}
      ]
    };
  }
};
</script>
