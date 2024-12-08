import { Ingredient } from "@/types/api/ingredients";
import { faker } from '@faker-js/faker';
import { getRandomBaseUnit, getRandomNumber } from "./utils";

export const createMockIngredient = (): Ingredient => ({
    id: faker.string.uuid(),
    makro_calories: getRandomNumber(1, 20),
    makro_carbs: getRandomNumber(1, 20),
    makro_fat: getRandomNumber(1, 20),
    makro_protein: getRandomNumber(1, 20),
    name: faker.food.ingredient(),
    base_unit: getRandomBaseUnit()
});