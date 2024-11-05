<template>
    <v-card class="recipe-card" max-width="344">
      <v-img v-if="recipe.image" :src="recipe.image" height="200" class="recipe-card-img"/>
      <v-img v-else src="https://via.placeholder.com/300" height="200" alt="Placeholder Image" class="recipe-card-img"/>
  
      <v-card-title>{{ recipe.name }}</v-card-title>
      <v-card-subtitle>{{ recipe.description }}</v-card-subtitle>
  
      <v-card-actions>
        <v-btn text color="primary">View Recipe</v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    recipe: {
      type: Object,
      required: true
    }
  });
  </script>
  
  <style scoped>
  .recipe-card {
    margin: 16px;
  }
  .recipe-card-img {
    margin-top: 16px;
  }
  </style>
  