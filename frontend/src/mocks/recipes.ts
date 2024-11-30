import { Recipe, RecipeIngredientsList, Recipes } from '@/types/api/recipes';
import { faker } from '@faker-js/faker';
import { createMockIngredient } from './ingredients';
import { createMockRecipeIngredient } from './recipeIngredients';

export const createMockRecipes = (): Recipes =>  ({
  recipes: Array.from({ length: 20 }, () => ({
    id: faker.string.uuid(),
    name: faker.food.dish(),
    description: faker.food.description(),
  })),
});

export const createMockSingleRecipe = (): Recipe => ({
  id: faker.string.uuid(),
  name: faker.food.dish(),
  description: faker.food.description(),
});

export const createMockRecipeIngredients = (): RecipeIngredientsList => Array.from({ length: 10 }, () => (
  {
    ingredient: createMockIngredient(),
    recipeIngredient: createMockRecipeIngredient()
  }
));
