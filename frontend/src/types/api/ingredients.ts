export interface Ingredient {
    id: string;
    makro_calories: number;
    makro_carbs: number;
    makro_fat: number;
    makro_protein: number;
    name: string;
    base_unit: string;
    density: number | null;
    weight_per_piece: number | null;
}