/** @type {import('tailwindcss').Config} */
module.exports = {
  purge:[
    './src/**/*.{js,jsx}', 
  ],
  darkMode:false,
  content: [],
  theme: {
    extend: {
      fontFamily: {
        'kaushan': ['Kaushan Script', 'cursive'],
      },
    },
  },
  plugins: [],
}

