import { defineConfig } from 'vite'
import path from 'path'

const repoRawDataPath = path.resolve(__dirname, 'repo_raw_data');
console.log('Resolved repo_raw_data path:', repoRawDataPath);

export default defineConfig({
  server: {
    fs: {
      // Allow serving files from the repo_raw_data directory
      allow: [
        repoRawDataPath  // Use __dirname for a more robust path resolution
      ]
    }
  },
  build: {
    // Make sure the image folder is included in the build output if needed
    assetsDir: 'assets'
  }
})
