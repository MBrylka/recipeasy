import { RecipeIngredient } from "@/types/api/recipeIngredients";
import { faker } from '@faker-js/faker';

export const createMockRecipeIngredient = (): RecipeIngredient => ({
    id: faker.string.uuid(),
    ingredient_id: faker.string.uuid(),
    quantity: 3.0,
    recipe_id: faker.string.uuid()
});