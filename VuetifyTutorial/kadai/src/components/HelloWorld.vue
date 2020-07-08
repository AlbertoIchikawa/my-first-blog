<template>
  <v-container fluid>
    <v-row justify="center">
      <v-expansion-panels popout>
        <!-- 拡張for文みたいなもの(project, i) -->
        <v-expansion-panel v-for="(project, i) in projects" :key="i" hide-actions>
          <v-expansion-panel-header>
            <v-row align="center" class="spacer" no-gutters>
              <!-- this v-col is for avatar and name or title -->
              <v-col cols="4" sm="2" md="1">
                <v-avatar size="36">
                  <!-- v-ifでavatarの場合 -->
                  <img v-if="project.avatar" :src="project.avatar" />
                  <!-- v-elseでそれ以外の場合。今回だとアイコンを表示 -->
                  <v-icon
                    v-else
                    :color="project.color"
                    v-text="project.icon"
                  ></v-icon>
                </v-avatar>
              </v-col>

              <!-- showing Name and title -->
              <v-col class="hidden-xs-only" sm="5" md="3">
                <strong v-html="project.name"></strong>
              <span
                  v-if="project.total"
                  class="grey--text"
                >
                <!-- &nbsp stands non-break-space -->
                  &nbsp;({{ project.total }})
              </span>
              </v-col>


              <!-- this v-col is for Main title -->
              <v-col class="text-no-wrap" cols="5" sm="3">
                <!-- showing new icon with using v-ship -->
                <v-chip
                  v-if="project.new"
                  :color="`${project.color} lighten-4`"
                  class="ml-0 mr-2 black--text"
                  label
                  small
                >
                  {{ project.new }} new
                </v-chip>
                <strong v-html="project.head"></strong>
              </v-col>
              
              <!-- this v-col is for subtitle like grey-message -->
              <v-col
                v-if="project.excerpt"
                class="grey--text text-truncate hidden-sm-and-down"
              > &mdash; {{ project.excerpt }}</v-col>
            </v-row>
          </v-expansion-panel-header>
          <!-- パネル内のコンテンツ。 -->
          <v-expansion-panel-content>
            <!-- v-dividerで区切り線を入れている。 -->
            <v-divider></v-divider>
            <!-- script内のcontentsを引き出す。 -->
            <v-card-text v-text="contents"></v-card-text>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      projects: [
        {
          avatar: "/img1.png",
          name: "John Leider",
          head: "Welcome to Vuetify.js!",
          excerpt: "Thank you for joining our community..."
        },
        {
          icon: "people_alt",
          color:"red",
          name: "Social",
          new:1,
          total:"3",
          head: "Twitter"
        },
        {
          icon: "local_offer",
          color:"teal",
          name: "Promos",
          new:2,
          total:"4",
          head: "Shop your way",
        }
      ],
      contents:
        "Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos. Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no, nostro voluptaria sea eu. Suas eligendi ius at, at nemore equidem est. Sed in error hendrerit, in consul constituam cum."
    };
  }
};
</script>