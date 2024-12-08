import { RecipeIngredient } from "@/types/api/recipeIngredients";
import { faker } from '@faker-js/faker';
import { getRandomNumber } from "./utils";

export const createMockRecipeIngredient = (): RecipeIngredient => ({
    id: faker.string.uuid(),
    ingredient_id: faker.string.uuid(),
    quantity: getRandomNumber(1, 300),
    recipe_id: faker.string.uuid()
});