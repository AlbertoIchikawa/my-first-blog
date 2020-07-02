<template>
  <div class="home">
    <h1>Homepage</h1>
    <v-btn class="pink white--text">CLICK ME</v-btn>
    <v-btn depressed color="pink">click me</v-btn>
    <v-btn text color="pink">click me</v-btn>

    <v-btn depressed class="pink white--text">
      <v-icon left>mdi-email</v-icon>
      <span>EMAIl ME</span>
    </v-btn>
    <v-btn depressed small class="pink white--text">
      <v-icon left small>mdi-email</v-icon>
      <span>EMAIl ME</span>
    </v-btn>
    <v-btn depressed large class="pink white--text">
     <span>EMAIl ME</span> 
     <v-icon right large >mdi-email</v-icon>
    </v-btn>
    <v-btn fab depressed small dark class="purple">
     <v-icon>mdi-heart</v-icon>
    </v-btn>
</div>
</template>

<script>
// @ is an alias to /src

export default {
}
</script>
