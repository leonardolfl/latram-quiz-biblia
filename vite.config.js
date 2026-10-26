import { resolve } from 'path';
import { fileURLToPath } from 'url';
import { defineConfig } from 'vite';

const __dirname = fileURLToPath(new URL('.', import.meta.url));

export default defineConfig({
  plugins: [
    {
      name: 'rewrite-routes',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url === '/appbiblia' || req.url === '/appbiblia/') {
            req.url = '/appbiblia/index.html';
          }
          if (req.url === '/fofuras' || req.url === '/fofuras/') {
            req.url = '/fofuras/index.html';
          }
          next();
        });
      },
    },
  ],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        appbiblia: resolve(__dirname, 'appbiblia/index.html'),
        fofuras: resolve(__dirname, 'fofuras/index.html'),
      },
    },
  },
});
