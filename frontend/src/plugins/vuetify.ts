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
    background: '#F1F8E9',
    surface: '#F1F8E9',
    'surface-bright': '#F1F8E9',
    'surface-light': '#DCEDC8',
    'surface-variant': '#424242',
    'on-surface-variant': '#DCEDC8',
    primary: '#7CB342',
    'primary-darken-1': '#1F5592',
    secondary: '#33691E',
    'secondary-darken-1': '#018786',
    error: '#FF8A65',
    info: '#81D4FA',
    success: '#76FF03',
    warning: '#FFCA28',
  },
  variables: {
    'border-color': '#000000',
    'border-opacity': 0.12,
    'high-emphasis-opacity': 0.87,
    'medium-emphasis-opacity': 0.60,
    'disabled-opacity': 0.38,
    'idle-opacity': 0.04,
    'hover-opacity': 0.04,
    'focus-opacity': 0.12,
    'selected-opacity': 0.08,
    'activated-opacity': 0.12,
    'pressed-opacity': 0.12,
    'dragged-opacity': 0.08,
    'theme-kbd': '#212529',
    'theme-on-kbd': '#F1F8E9',
    'theme-code': '#F5F5F5',
    'theme-on-code': '#000000',
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
