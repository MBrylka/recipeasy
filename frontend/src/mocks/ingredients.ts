import { Ingredient } from "@/types/api/ingredients";
import { faker } from '@faker-js/faker';

export const createMockIngredient = (): Ingredient => ({
    id: faker.string.uuid(),
    makro_calories: 100.0,
    makro_carbs: 10.0,
    makro_fat: 10.0,
    makro_protein: 10.0,
    name: faker.food.ingredient()
});