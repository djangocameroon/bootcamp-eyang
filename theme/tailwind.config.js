module.exports = {
  content: [
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    './static/**/*.js',
  ],

  theme: {
    extend: {},
  },
  plugins: [
      require('tailwindcss-animate'),
      require('daisyui'),
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),


  ],

  daisyui: {
    themes: true,
  }
}

