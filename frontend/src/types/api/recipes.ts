import { Ingredient } from "./ingredients";
import { RecipeIngredient } from "./recipeIngredients";

export interface Recipe {
    "description": string;
    "id": string;
    "name": string;
}

export interface Recipes {
    recipes: Recipe[];
}

export interface RecipeIngredientWithDetails {
    ingredient: Ingredient;
    recipeIngredient: RecipeIngredient;
}

export type RecipeIngredientsList = RecipeIngredientWithDetails[];