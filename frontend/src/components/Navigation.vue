<template>
    <v-app-bar scroll-behavior="fade-image" image="@/assets/banner2.webp" height="100">
        <v-app-bar-nav-icon color="primary" @click.stop="toggleNavigation()"></v-app-bar-nav-icon>
        <v-app-bar-title class="text-primary font-weight-black text-h5">Recipeasy</v-app-bar-title>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" temporary>
        <v-list>
            <v-list-subheader>Pages</v-list-subheader>
            <v-list-item v-for="item in navItems" :key="item.title" :to="item.link" link color="secondary">
                <template v-slot:prepend>
                    <v-icon icon="$vuetify"></v-icon>
                </template>
                <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script setup lang="ts">

import { ref } from 'vue';

const drawer = ref(false);
const navItems = [
    { title: 'Dashboard', link: '/' },
    { title: 'Recipes', link: '/recipes' },
    { title: 'Ingredients', link: '/ingredients' },
]

const toggleNavigation = () => {
    drawer.value = !drawer.value
}

</script>