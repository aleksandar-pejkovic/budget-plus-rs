import { defineConfig } from '@playwright/test';
const baseURL = `http://127.0.0.1:${process.env.BUDZET_PREVIEW_PORT || 8765}`;
export default defineConfig({
  testDir: './tests/ui', timeout: 60000, workers: 1, reporter: 'list',
  use: { baseURL, browserName: 'chromium', headless: true, screenshot: 'only-on-failure' },
  webServer: { command: 'node scripts/preview.mjs', url: baseURL, reuseExistingServer: !process.env.CI },
});
