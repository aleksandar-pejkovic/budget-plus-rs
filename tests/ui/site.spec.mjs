import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { readdir } from 'node:fs/promises';
const folders = await readdir(new URL('../..', import.meta.url), { withFileTypes: true });
const pages = ['/', ...folders.filter(f => f.isDirectory() && /^(iskra-|izvrsenje-|knjizenje-|obrazac-|oris-|osnovna-|program-|rucni-|spiri-|uplate-|zatvaranje-)/.test(f.name)).map(f => `/${f.name}/`)];
if (pages.length !== 13) throw new Error(`Expected 13 public pages, found ${pages.length}`);

test.beforeEach(async ({ page }) => {
  await page.route(/google-analytics|googletagmanager|challenges.cloudflare.com/, route => route.abort());
});

test('introduction and contact choices are visible on the first screen', async ({ page }) => {
  for (const [width, height] of [[1366, 768], [1440, 900], [360, 800], [390, 844]]) {
    await page.setViewportSize({ width, height });
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);
    await expect(page.locator('.hero-intro')).toContainText('Vi proveravate i potvrđujete');
    for (const selector of ['.hero h1', '.hero .btn.primary', '.hero .text-link', '.hero-phone a']) {
      const box = await page.locator(selector).boundingBox();
      expect(box.y, `${width}: ${selector} starts on screen`).toBeGreaterThanOrEqual(0);
      expect(box.y + box.height, `${width}: ${selector} fits on screen`).toBeLessThanOrEqual(height);
    }
    await page.screenshot({ path: `.cache/screens/first-screen-${width}.png` });
  }
});

for (const width of [360, 390, 768, 1024, 1440]) {
  test(`all pages fit at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 960 });
    for (const path of pages) {
      await page.goto(path);
      await expect(page.locator('h1')).toHaveCount(1);
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), path).toBeTruthy();
      if (width === 1440 || width === 390) await page.screenshot({ path: `.cache/screens/${width}-${path.replaceAll('/', '') || 'home'}.png`, fullPage: true });
    }
  });
}
test('all pages pass automated WCAG A/AA checks', async ({ page }) => {
  for (const path of pages) {
    await page.goto(path);
    const result = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
    expect(result.violations, path).toEqual([]);
  }
});
test('mobile menu, image dialog and solution links work with keyboard', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/');
  const menu = page.getByRole('button', { name: 'Meni' });
  await menu.click(); await expect(menu).toHaveAttribute('aria-expanded', 'true');
  await page.keyboard.press('Escape'); await expect(menu).toBeFocused(); await expect(menu).toHaveAttribute('aria-expanded', 'false');
  await page.locator('.zoom-image').click(); await expect(page.locator('dialog')).toBeVisible();
  await page.keyboard.press('Escape'); await expect(page.locator('dialog')).not.toBeVisible(); await expect(page.locator('.zoom-image')).toBeFocused();
  await page.goto('/spiri-izvodi-skole/');
  const advanceLink = page.locator('#avansi a');
  await advanceLink.focus(); await page.keyboard.press('Enter');
  await expect(page).toHaveURL(/knjizenje-e-faktura-za-skole\/#avansi$/);
  await expect(page.locator('#avansi')).toBeInViewport();
  await page.locator('.related-links a[href="../spiri-izvodi-skole/"]').click();
  await expect(page).toHaveURL(/spiri-izvodi-skole\/$/);
  await page.locator('.landing-cta a').click();
  await expect(page).toHaveURL(/\?tema=spiri-izvodi-skole#kontakt$/);
  await expect(page.locator('#contact-form')).toBeVisible();
});
test('form validation, accepted submission, retry and mode switch', async ({ page }) => {
  await page.route('**/assets/contact-config.js', route => route.fulfill({ contentType: 'application/javascript', body: "window.BUDZET_CONTACT={endpoint:'https://api.budzetplus.rs/contact',sitekey:'test'};" }));
  await page.route('https://challenges.cloudflare.com/**', route => route.fulfill({ contentType: 'application/javascript', body: "window.turnstile={render:(s,o)=>{window.testWidget=o;o.callback('fresh');return 'widget';},reset:()=>window.testWidget.callback('fresh')};window.budzetTurnstileReady();" }));
  let calls = 0; let success = false;
  await page.route('https://api.budzetplus.rs/contact', async route => {
    calls++; const data = route.request().postDataJSON(); expect(data.jbkjs).toBe('00123');
    await route.fulfill({ status: success ? 200 : 503, contentType: 'application/json', body: JSON.stringify({ ok: success }) });
  });
  await page.goto('/#kontakt');
  const form = page.locator('#contact-form');
  await form.getByRole('button', { name: 'Prijavite se za prezentaciju' }).click();
  await expect(page.locator('#contact-name')).toHaveAttribute('aria-invalid', 'true'); expect(calls).toBe(0);
  await page.locator('#contact-name').fill('Demo korisnik'); await page.locator('#contact-org').fill('Demo škola');
  await page.locator('#contact-jbkjs').fill('00123'); await page.locator('#contact-email').fill('demo@example.com');
  await page.locator('#contact-message').fill('Sačuvana napomena');
  await form.getByRole('button', { name: 'Prijavite se za prezentaciju' }).click();
  await expect(form.locator('.form-feedback')).toHaveAttribute('data-state', 'error');
  await expect(page.locator('#contact-message')).toHaveValue('Sačuvana napomena');
  await page.locator('.form-mode-switch').click(); await expect(page.locator('#contact-message')).toHaveValue('Sačuvana napomena');
  success = true; await form.getByRole('button', { name: 'Pošaljite pitanje' }).click();
  await expect(form.locator('.form-feedback')).toHaveAttribute('data-state', 'success');
  expect(calls).toBe(2); await expect(page.locator('#contact-email')).toHaveValue('');
});

test('local preview validates without contacting production or Turnstile', async ({ page }) => {
  const requests = [];
  page.on('request', request => {
    if (/workers\.dev|challenges\.cloudflare\.com/.test(request.url())) requests.push(request.url());
  });
  await page.goto('/#kontakt');
  const form = page.locator('#contact-form');
  await expect(form.locator('.form-feedback')).toContainText('Lokalni pregled');
  await page.locator('#contact-name').fill('Demo korisnik');
  await page.locator('#contact-org').fill('Demo škola');
  await page.locator('#contact-jbkjs').fill('00123');
  await page.locator('#contact-email').fill('demo@example.com');
  await form.getByRole('button', { name: 'Prijavite se za prezentaciju' }).click();
  await expect(form.locator('.form-feedback')).toContainText('Podaci su ispravni.');
  await expect(page.locator('#contact-email')).toHaveValue('demo@example.com');
  expect(requests).toEqual([]);
});
