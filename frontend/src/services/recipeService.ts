import { createMockRecipes, createMockSingleRecipe, createMockRecipeIngredients} from "@/mocks/recipes";
import { delay } from "@/mocks/utils";

const API_BASE_URL = '/api';

const delayTime = 1000;


export async function fetchRecipes() {
  try {

    if(import.meta.env.MODE === 'development') {
      await delay(delayTime);
      return createMockRecipes();
    }

    const response = await fetch(`${API_BASE_URL}/recipes`);
    if (!response.ok) {
      throw new Error('Failed to fetch recipes');
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function fetchSingleRecipe(recipeId: string) {
  try {

    if(import.meta.env.MODE === 'development') {
      await delay(delayTime);
      return createMockSingleRecipe();
    }

    const response = await fetch(`${API_BASE_URL}/recipes/${recipeId}`);
    if (!response.ok) {
      throw new Error('Failed to fetch recipe');
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function fetchRecipeIngredients(recipeId: string) {
  try {
    if(import.meta.env.MODE === 'development') {
      await delay(delayTime);
      return createMockRecipeIngredients()
    }

    const response = await fetch(`${API_BASE_URL}/recipes/${recipeId}/ingredients`);
    if (!response.ok) {
      throw new Error('Failed to fetch recipe');
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
}