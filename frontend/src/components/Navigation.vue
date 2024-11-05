<template>
    <v-toolbar>
        <v-toolbar-items>
            <v-btn variant="text" v-for="navItem in navItems" :to="navItem.link">{{ navItem.text }}</v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-toolbar-title>{{ currentRoute.name }}</v-toolbar-title>
        <v-toolbar-title>Recipeasy</v-toolbar-title>
    </v-toolbar>
</template>

<script setup lang="ts">

import { useRoute } from 'vue-router';

const currentRoute = useRoute();

const navItems = [
    {text: 'Dashboard', link: '/'},
    {text: 'Recipes', link: '/recipes'},
    {text: 'Ingredients', link: '/ingredients'},
]
</script>