<template>
    <v-container>
        <v-row justify="center" v-if="isRecipeLoading">
            <v-progress-circular color="primary" indeterminate :size="64" :width="8"></v-progress-circular>
        </v-row>
        <v-row v-else>
            <v-col cols="12" md="8">
                <v-img src="https://picsum.photos/1000/1000" height="400" cover class="mb-4" />
                <!-- Description Section -->
                <section class="mb-4">
                    <v-card>
                        <v-card-title>
                            <h2>{{ recipe?.name }}</h2>
                            <v-chip color="secondary">
                                Breakfast
                            </v-chip>
                            <v-chip color="secondary">
                                Lunch
                            </v-chip>
                        </v-card-title>
                        <v-divider></v-divider>
                        <v-card-text>
                            {{ recipe?.description }}
                        </v-card-text>
                    </v-card>
                </section>
                <v-divider></v-divider>
                <!-- Ingredients Section -->
                <section class="mb-4">
                    <v-data-table :hide-default-footer="true" v-model="tableSelected" item-value="name" show-select
                        :headers="tableHeaders" :items="ingredientsTableData" class="elevation-1">
                        <template #top>
                            <v-toolbar flat>
                                <v-toolbar-title>Ingredients</v-toolbar-title>
                                <v-spacer></v-spacer>
                            </v-toolbar>
                        </template>
                    </v-data-table>
                </section>
                <!-- Steps Section -->
                <section class="mb-4">
                    <v-card>
                        <v-card-title>
                            <h2>Steps</h2>
                        </v-card-title>
                        <v-divider></v-divider>
                        <v-list>
                            <v-list-item v-for="(step, index) in recipeSteps" :key="index">
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <v-icon color="primary">mdi-numeric-{{ index + 1
                                            }}-circle</v-icon>
                                        {{ step }}
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                    </v-card>
                </section>
            </v-col>
            <v-col cols="12" md="4">
                <v-card>
                    <v-card-title>
                        <h2>Nutrition</h2>
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-list>
                        <v-list-item v-for="(item, index) in nutrition" :key="index">
                            <div class="d-flex justify-space-between align-center w-100">
                                <div class="d-flex align-center">
                                    <v-icon color="success" class="me-2">mdi-nutrition</v-icon>
                                    <span>{{ item.name }}</span>
                                </div>
                                <span>{{ item.value }}</span>
                            </div>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup lang="ts">
import { fetchRecipeIngredients, fetchSingleRecipe } from '@/services/recipeService';
import { Recipe, RecipeIngredientsList } from '@/types/api/recipes';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router/auto';

interface IngredientTableData {
    name: String;
    quantity: number;
    base_unit: String;
    calories: number;
    carbs: number;
    fat: number;
    protein: number;
}

const currentRoute = useRoute();
const recipeId = currentRoute.params.uuid as string;
const tableHeaders = [
    { title: "Quantity", key: "quantity" },
    { title: "Unit", key: "base_unit" },
    { title: "Name", key: "name" },
    { title: "Calories", key: "calories" },
    { title: "Carbs", key: "carbs" },
    { title: "Fat", key: "fat" },
    { title: "Protein", key: "protein" },
];

const isRecipeLoading = ref(false)
const error = ref(null);
const recipe = ref<Recipe>();
const tableSelected = ref([]);
const recipeIngredients = ref<RecipeIngredientsList>();
const ingredientsTableData = ref<IngredientTableData[]>();
const recipeSteps = [
    "Preheat the oven to 180°C (350°F).",
    "Mix ingredient A with ingredient B.",
    "Add ingredient C and stir thoroughly.",
    "Bake for 25-30 minutes, or until golden brown."
];

const nutrition = ref([
    { name: "kcal", value: 0 },
    { name: "Carb", value: 0 },
    { name: "Protein", value: 0 },
    { name: "Fat", value: 0 }
]);

const calculateNutrition = () => {
    if (!recipeIngredients.value) throw new Error("recipe ingredients are undefined");

    recipeIngredients.value.forEach(recipeIngredient => {
        if (recipeIngredient.ingredient.base_unit === "pcs") {
            nutrition.value[0].value += recipeIngredient.ingredient.makro_calories * recipeIngredient.recipeIngredient.quantity;
            nutrition.value[1].value += recipeIngredient.ingredient.makro_carbs * recipeIngredient.recipeIngredient.quantity;
            nutrition.value[2].value += recipeIngredient.ingredient.makro_protein * recipeIngredient.recipeIngredient.quantity;
            nutrition.value[3].value += recipeIngredient.ingredient.makro_fat * recipeIngredient.recipeIngredient.quantity;
        } else {
            nutrition.value[0].value += recipeIngredient.ingredient.makro_calories * recipeIngredient.recipeIngredient.quantity / 100.0;
            nutrition.value[1].value += recipeIngredient.ingredient.makro_carbs * recipeIngredient.recipeIngredient.quantity / 100.0;
            nutrition.value[2].value += recipeIngredient.ingredient.makro_protein * recipeIngredient.recipeIngredient.quantity / 100.0;
            nutrition.value[3].value += recipeIngredient.ingredient.makro_fat * recipeIngredient.recipeIngredient.quantity / 100.0;

        }
    });
}

onMounted(async () => {
    try {
        isRecipeLoading.value = true;
        recipe.value = await fetchSingleRecipe(recipeId);
        recipeIngredients.value = await fetchRecipeIngredients(recipeId);
        if (!recipeIngredients.value)
            throw new Error("Service returned undefined value");
        ingredientsTableData.value = recipeIngredients.value.map((recipeIngredient) => ({
            name: recipeIngredient.ingredient.name,
            quantity: recipeIngredient.recipeIngredient.quantity,
            base_unit: recipeIngredient.ingredient.base_unit,
            calories: recipeIngredient.ingredient.makro_calories,
            carbs: recipeIngredient.ingredient.makro_carbs,
            fat: recipeIngredient.ingredient.makro_fat,
            protein: recipeIngredient.ingredient.makro_protein,
        }));
        calculateNutrition();


    } catch (err: any) {
        error.value = err
    } finally {
        isRecipeLoading.value = false;
    }
});

</script>

<style scoped>
.mb-4 {
    margin-bottom: 16px;
}

.mb-8 {
    margin-bottom: 32px;
}
</style>