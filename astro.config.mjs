import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: 'https://johndorion.com',
  base: '',
  output: 'static',
  integrations: [mdx(), sitemap(), tailwind()],
  // Sharp image optimization at build time
  // Note: Cloudflare adapter warning about runtime sharp is informational only.
  // With output: "static", all images are optimized at build time, not runtime.
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  },
});