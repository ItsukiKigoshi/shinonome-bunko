// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from "vite-plugin-vuetify";
export default defineNuxtConfig({
  app: {
    baseURL: process.env.NUXT_APP_BASE_URL || "/",
  },
  build: {
    transpile: ["vuetify"],
  },
  compatibilityDate: "2024-11-01",
  components: [
    {
      path: "~/components",
      pathPrefix: false,
    },
  ],
  devtools: { enabled: true },
  modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook("vite:extendConfig", (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }));
      });
    },
  ],
  ssr: false, // GitHub Pages is for static sites
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
});
