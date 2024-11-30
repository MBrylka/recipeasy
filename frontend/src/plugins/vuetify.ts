/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides


const recipeasyLightTheme = {
  dark: false,
  colors: {
    background: '#FAFAFA',       // Jasnoszary dla lepszej przejrzystości
    surface: '#FFFFFF',          // Czysta biel na główne elementy
    'surface-bright': '#E0F7FA', // Delikatny niebieski na wyróżnione elementy
    'surface-light': '#ECEFF1',  // Jasna szarość dla wariantu tła
    'surface-variant': '#B0BEC5',// Chłodna szarość dla kontrastu
    'on-surface-variant': '#455A64', // Ciemna szarość na teksty i ikony
    primary: '#039BE5',          // Niebieski jako kolor przewodni
    'primary-darken-1': '#0277BD', // Lekko ciemniejszy niebieski do akcentów
    secondary: '#FF7043',        // Ciepły pomarańczowy dla kontrastowych elementów
    'secondary-darken-1': '#D84315', // Ciemniejszy pomarańczowy na interaktywne elementy
    error: '#E57373',            // Pastelowa czerwień dla błędów
    info: '#4FC3F7',             // Jasnoniebieski dla informacji
    success: '#81C784',          // Pastelowa zieleń dla sukcesów
    warning: '#FFB74D',          // Ciepły żółty dla ostrzeżeń
  },
  variables: {
    'border-color': '#B0BEC5',    // Chłodna szarość dla subtelnych obramowań
    'border-opacity': 0.15,
    'high-emphasis-opacity': 0.85,
    'medium-emphasis-opacity': 0.65,
    'disabled-opacity': 0.35,
    'idle-opacity': 0.05,
    'hover-opacity': 0.07,
    'focus-opacity': 0.15,
    'selected-opacity': 0.10,
    'activated-opacity': 0.15,
    'pressed-opacity': 0.15,
    'dragged-opacity': 0.10,
    'theme-kbd': '#37474F',
    'theme-on-kbd': '#E0F7FA',
    'theme-code': '#ECEFF1',
    'theme-on-code': '#263238',
  }
}


export default createVuetify({
  theme: {
    defaultTheme: 'recipeasyLightTheme',
    themes: {
      recipeasyLightTheme,
    }
  },
})
