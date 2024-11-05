const API_BASE_URL = '/api'; // Replace with your API base URL

export async function fetchRecipes() {
  try {
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