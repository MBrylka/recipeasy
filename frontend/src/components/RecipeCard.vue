<template>
  <v-card class="recipe-card" max-width="344">
    <v-img v-if="recipe.image" :src="recipe.image" height="200px" cover />
    <v-img v-else src="https://picsum.photos/1000/1000" height="200" cover />

    <v-card-title>{{ recipe.name }}</v-card-title>
    <v-card-subtitle>
      <v-chip color="secondary">
        Breakfast
      </v-chip>
    </v-card-subtitle>
    <v-card-text>{{ recipe.description }}</v-card-text>

    <v-card-actions>
      <v-btn text color="primary" variant="tonal" size="small" :to="`/recipes/${recipe.id}`">View Recipe</v-btn>
      <v-btn text color="secondary" variant="tonal" size="small">Add to week</v-btn>
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
</style>