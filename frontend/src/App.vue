<template>
  <v-app>
    <v-container>
      <v-col>
        <v-row>
          <Navigation />
        </v-row>
        <v-row>
          <v-main>
            <router-view />
          </v-main>
        </v-row>
      </v-col>
    </v-container>

  </v-app>
</template>

<script lang="ts" setup>
</script>
