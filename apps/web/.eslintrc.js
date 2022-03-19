require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  extends: ['plugin:vue/vue3-recommended', 'prettier'],
  rules: {
    'vue/max-attributes-per-line': 'off',
    'vue/singleline-html-element-content-newline': 'off',
  },
};
