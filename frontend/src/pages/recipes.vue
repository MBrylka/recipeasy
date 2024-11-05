<template>
  <v-container>
    <h1> Recipes page </h1>

    <v-row justify="center" v-if="isRecipesLoading">
      <v-progress-circular color="primary" indeterminate :size="64" :width="8"></v-progress-circular>
    </v-row>

    <v-alert v-else-if="error" color="error" colored-border>
      Error: {{ error }}
    </v-alert>


    <v-row v-else>
      <v-col v-for="recipe in recipes.recipes" :key="recipe.id" cols="12" sm="6" md="4">
        <RecipeCard :recipe="recipe" />
      </v-col>
    </v-row>

  </v-container>
</template>

<script lang="ts" setup>
import { fetchRecipes } from '@/services/recipeService';
import { Recipes } from '@/types/api/recipes';
import { onMounted, ref } from 'vue';

const isRecipesLoading = ref(false)
const error = ref(null);
const recipes = ref<Recipes>({
  recipes: []
});

onMounted(async () => {
  try {
    isRecipesLoading.value = true;
    recipes.value = await fetchRecipes();
  } catch (err:any) {
    error.value = err
  } finally {
    isRecipesLoading.value = false;
  }
});


</script>
