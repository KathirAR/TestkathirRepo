# Playwright Cheat Sheet

A comprehensive reference guide for Playwright automation framework.

## Table of Contents
- [Installation](#installation)
- [Basic Setup](#basic-setup)
- [Selectors](#selectors)
- [Navigation](#navigation)
- [Interactions](#interactions)
- [Assertions](#assertions)
- [Waiting](#waiting)
- [Network](#network)
- [Screenshots & Videos](#screenshots--videos)
- [Debugging](#debugging)
- [Configuration](#configuration)
- [Test Hooks](#test-hooks)
- [Advanced Features](#advanced-features)
- [API Testing](#api-testing)
- [Mobile Emulation](#mobile-emulation)
- [Common Patterns](#common-patterns)

---

## Installation

```bash
# Install Playwright with the test runner
npm init playwright@latest

# Install Playwright manually
npm install -D @playwright/test

# Install browsers
npx playwright install

# Install specific browsers
npx playwright install chromium firefox webkit
```

## Basic Setup

### Basic Test Structure

```javascript
const { test, expect } = require('@playwright/test');

test('basic test', async ({ page }) => {
  await page.goto('https://example.com');
  const title = await page.title();
  expect(title).toBe('Example Domain');
});
```

### Playwright Config

```javascript
// playwright.config.js
const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],
});
```

## Selectors

### Selector Types

```javascript
// CSS selectors
page.locator('div.class-name');
page.locator('#id');
page.locator('button[type="submit"]');

// Text selectors
page.locator('text=Submit');
page.getByText('Submit');
page.getByText('Submit', { exact: true });

// Role selectors
page.getByRole('button');
page.getByRole('button', { name: 'Submit' });

// Test ID selectors
page.getByTestId('submit-button');

// Placeholder selectors
page.getByPlaceholder('Email');

// Label selectors
page.getByLabel('Password');

// Alt text selectors
page.getByAltText('Logo');

// Title selectors
page.getByTitle('Information');

// Combining selectors
page.locator('form').getByRole('button');
```

### Selector Chaining

```javascript
// Chain selectors to narrow down
const form = page.locator('form');
const submitButton = form.locator('button[type="submit"]');

// Equivalent to
const submitButton = page.locator('form button[type="submit"]');
```

### Filtering Selectors

```javascript
// Filter by text
page.locator('div').filter({ hasText: 'Hello' });

// Filter by not having text
page.locator('div').filter({ hasNotText: 'Hidden' });

// Filter by having another element
page.locator('li').filter({ has: page.locator('.highlight') });

// Filter by not having another element
page.locator('li').filter({ hasNot: page.locator('.disabled') });
```

## Navigation

```javascript
// Navigate to URL
await page.goto('https://example.com');

// Navigate with options
await page.goto('https://example.com', {
  waitUntil: 'networkidle', // 'load', 'domcontentloaded', 'networkidle'
  timeout: 30000
});

// Go back/forward
await page.goBack();
await page.goForward();

// Reload page
await page.reload();

// Wait for URL
await page.waitForURL('https://example.com/dashboard');
await page.waitForURL(/.*dashboard/);
```

## Interactions

### Mouse Interactions

```javascript
// Click
await page.click('button');
await page.locator('button').click();

// Double click
await page.dblclick('button');
await page.locator('button').dblclick();

// Right click
await page.click('button', { button: 'right' });

// Hover
await page.hover('button');

// Drag and drop
await page.dragAndDrop('#source', '#target');
```

### Keyboard Interactions

```javascript
// Type text
await page.fill('input', 'Hello World');
await page.locator('input').fill('Hello World');

// Type with delay (for visible typing)
await page.fill('input', 'Hello World', { delay: 100 });

// Press a key
await page.press('input', 'Enter');
await page.keyboard.press('Enter');

// Key combinations
await page.keyboard.press('Control+A');
await page.keyboard.press('Control+C');

// Type raw keyboard input
await page.keyboard.type('Hello World');

// Key down/up
await page.keyboard.down('Shift');
await page.click('button');
await page.keyboard.up('Shift');
```

### Form Interactions

```javascript
// Fill input
await page.fill('#username', 'user123');

// Clear input
await page.fill('#username', '');

// Select option by value
await page.selectOption('select#country', 'US');

// Select option by label
await page.selectOption('select#country', { label: 'United States' });

// Select option by index
await page.selectOption('select#country', { index: 0 });

// Select multiple options
await page.selectOption('select#colors', ['red', 'blue']);

// Check/uncheck checkbox
await page.check('#agree');
await page.uncheck('#subscribe');

// Set file inputs
await page.setInputFiles('input[type="file"]', 'path/to/file.pdf');
await page.setInputFiles('input[type="file"]', ['file1.pdf', 'file2.pdf']);

// Clear file input
await page.setInputFiles('input[type="file"]', []);
```

## Assertions

```javascript
// Element assertions
await expect(page.locator('h1')).toBeVisible();
await expect(page.locator('button')).toBeEnabled();
await expect(page.locator('input')).toBeDisabled();
await expect(page.locator('input')).toBeEditable();
await expect(page.locator('input')).toBeEmpty();
await expect(page.locator('input')).toBeChecked();
await expect(page.locator('input')).not.toBeChecked();
await expect(page.locator('div')).toBeHidden();

// Text assertions
await expect(page.locator('h1')).toHaveText('Welcome');
await expect(page.locator('h1')).toContainText('Welcome');
await expect(page.locator('h1')).not.toHaveText('Error');

// Attribute assertions
await expect(page.locator('input')).toHaveAttribute('type', 'email');
await expect(page.locator('input')).toHaveValue('test@example.com');
await expect(page.locator('input')).toHaveClass('form-input');
await expect(page.locator('input')).toHaveCSS('color', 'rgb(255, 0, 0)');

// Count assertions
await expect(page.locator('li')).toHaveCount(5);

// Page assertions
await expect(page).toHaveTitle('Example Domain');
await expect(page).toHaveURL(/example\.com/);

// Screenshot assertions
await expect(page).toHaveScreenshot('homepage.png');
await expect(page.locator('div')).toHaveScreenshot('element.png');
```

## Waiting

```javascript
// Wait for element
await page.waitForSelector('button');
await page.waitForSelector('button', { state: 'visible' });
await page.waitForSelector('div.loading', { state: 'hidden' });

// Wait for navigation
await page.waitForNavigation();
await Promise.all([
  page.waitForNavigation(),
  page.click('a.link')
]);

// Wait for load state
await page.waitForLoadState('load'); // 'load', 'domcontentloaded', 'networkidle'

// Wait for function
await page.waitForFunction(() => document.querySelector('.status').textContent === 'Ready');

// Wait for timeout
await page.waitForTimeout(1000); // Avoid using in production tests
```

## Network

### Network Monitoring

```javascript
// Listen for all requests
page.on('request', request => console.log(request.url()));
page.on('response', response => console.log(response.status()));

// Wait for specific request
const responsePromise = page.waitForResponse('**/api/users');
await page.click('button#load-users');
const response = await responsePromise;
```

### Network Interception

```javascript
// Mock API response
await page.route('**/api/users', route => {
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify([{ name: 'John Doe' }])
  });
});

// Abort requests
await page.route('**/*.{png,jpg,jpeg}', route => route.abort());

// Modify requests
await page.route('**/api/submit', route => {
  const json = JSON.parse(route.request().postData() || '{}');
  json.extra = 'field';
  route.continue({
    postData: JSON.stringify(json)
  });
});

// Continue with modified headers
await page.route('**/*', route => {
  const headers = route.request().headers();
  headers['X-Custom'] = 'value';
  route.continue({ headers });
});
```

## Screenshots & Videos

```javascript
// Take screenshot
await page.screenshot({ path: 'screenshot.png' });

// Screenshot options
await page.screenshot({
  path: 'screenshot.png',
  fullPage: true,
  clip: { x: 0, y: 0, width: 500, height: 500 },
  omitBackground: true
});

// Element screenshot
await page.locator('div.hero').screenshot({ path: 'hero.png' });

// Enable video recording in config
// playwright.config.js
use: {
  video: 'on-first-retry', // 'on', 'off', 'retain-on-failure'
}
```

## Debugging

```javascript
// Pause execution for debugging
await page.pause();

// Run in headed mode
npx playwright test --headed

// Run with inspector
npx playwright test --debug

// Slow down execution
// playwright.config.js
use: {
  launchOptions: {
    slowMo: 100
  }
}

// Enable verbose API logs
// playwright.config.js
use: {
  logger: {
    isEnabled: (name, severity) => true,
    log: (name, severity, message, args) => console.log(`${name} ${message}`)
  }
}

// Trace viewer
// playwright.config.js
use: {
  trace: 'on', // 'on', 'off', 'on-first-retry', 'retain-on-failure'
}

// View trace
npx playwright show-trace trace.zip
```

## Configuration

### Browser Context Options

```javascript
// playwright.config.js
use: {
  // Browser context options
  viewport: { width: 1280, height: 720 },
  ignoreHTTPSErrors: true,
  javaScriptEnabled: true,
  bypassCSP: false,
  timezoneId: 'America/New_York',
  geolocation: { latitude: 40.7128, longitude: -74.0060 },
  permissions: ['geolocation'],
  locale: 'en-US',
  colorScheme: 'dark', // 'light', 'dark', 'no-preference'
  reducedMotion: 'reduce', // 'reduce', 'no-preference'
  
  // Browser launch options
  launchOptions: {
    args: ['--disable-web-security'],
    headless: false,
    slowMo: 100,
    channel: 'chrome', // 'chrome', 'msedge', etc.
  }
}
```

### Test Parallelism

```javascript
// playwright.config.js
module.exports = defineConfig({
  // Run tests in files in parallel
  fullyParallel: true,
  
  // Fail the build on CI if you accidentally left test.only in the source code
  forbidOnly: !!process.env.CI,
  
  // Retry on CI only
  retries: process.env.CI ? 2 : 0,
  
  // Opt out of parallel tests on CI
  workers: process.env.CI ? 1 : undefined,
});
```

## Test Hooks

```javascript
// Before/after hooks
test.beforeAll(async () => {
  // Setup before all tests
});

test.afterAll(async () => {
  // Teardown after all tests
});

test.beforeEach(async ({ page }) => {
  // Setup before each test
  await page.goto('https://example.com');
});

test.afterEach(async ({ page }) => {
  // Teardown after each test
});

// Skip tests
test.skip('skipped test', async ({ page }) => {
  // This test will be skipped
});

// Skip in specific conditions
test('conditional skip', async ({ page, browserName }) => {
  test.skip(browserName === 'firefox', 'Not supported in Firefox');
  // Test code
});

// Mark as failing
test('known failure', async ({ page }) => {
  test.fail();
  // Test code
});

// Conditional failure
test('conditional failure', async ({ page, browserName }) => {
  test.fail(browserName === 'webkit', 'This feature is not implemented in WebKit');
  // Test code
});

// Fixme
test.fixme('test to be fixed', async ({ page }) => {
  // This test will be marked as fixme
});

// Timeout
test('custom timeout', async ({ page }) => {
  test.setTimeout(60000);
  // Test with longer timeout
});
```

## Advanced Features

### Authentication

```javascript
// Login and save state
const authFile = 'auth.json';

async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  await page.goto('https://example.com/login');
  await page.fill('#username', 'user');
  await page.fill('#password', 'pass');
  await page.click('#login');
  
  // Wait for login to complete
  await page.waitForSelector('.logged-in-indicator');
  
  // Save storage state
  await page.context().storageState({ path: authFile });
  await browser.close();
}

// Use in tests
// playwright.config.js
use: {
  storageState: 'auth.json'
}
```

### Fixtures

```javascript
// Custom fixtures
// fixtures.js
const base = require('@playwright/test');
const { test: baseTest, expect } = base;

const test = baseTest.extend({
  loggedInPage: async ({ page }, use) => {
    await page.goto('https://example.com/login');
    await page.fill('#username', 'user');
    await page.fill('#password', 'pass');
    await page.click('#login');
    await page.waitForSelector('.logged-in-indicator');
    
    await use(page);
  },
  
  // Fixture with parameters
  authenticatedRequest: async ({ request }, use, testInfo) => {
    const enhancedRequest = async (url, options = {}) => {
      const headers = options.headers || {};
      return request.fetch(url, {
        ...options,
        headers: {
          ...headers,
          'Authorization': 'Bearer token123'
        }
      });
    };
    
    await use(enhancedRequest);
  }
});

// Export custom test with fixtures
module.exports = { test, expect };

// Use in tests
const { test, expect } = require('./fixtures');

test('use custom fixture', async ({ loggedInPage }) => {
  await loggedInPage.click('#dashboard');
  // Test with logged in user
});
```

### Parameterized Tests

```javascript
// Simple parameterization
const users = [
  { name: 'User1', role: 'admin' },
  { name: 'User2', role: 'editor' },
  { name: 'User3', role: 'viewer' }
];

for (const user of users) {
  test(`test with ${user.name}`, async ({ page }) => {
    // Test with this user
  });
}

// Using test.describe.parallel.each
test.describe.parallel.each(users)(
  (user) => {
    test(`test with ${user.name}`, async ({ page }) => {
      // Test with this user
    });
  }
);
```

## API Testing

```javascript
// API requests
const { test, expect } = require('@playwright/test');

test('API test', async ({ request }) => {
  // GET request
  const getResponse = await request.get('https://api.example.com/users');
  expect(getResponse.ok()).toBeTruthy();
  expect(getResponse.status()).toBe(200);
  
  const users = await getResponse.json();
  expect(users.length).toBeGreaterThan(0);
  
  // POST request
  const postResponse = await request.post('https://api.example.com/users', {
    data: {
      name: 'John Doe',
      email: 'john@example.com'
    },
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer token123'
    }
  });
  
  expect(postResponse.ok()).toBeTruthy();
  const newUser = await postResponse.json();
  expect(newUser.id).toBeDefined();
  
  // PUT request
  const putResponse = await request.put(`https://api.example.com/users/${newUser.id}`, {
    data: {
      name: 'John Updated',
      email: 'john@example.com'
    }
  });
  
  expect(putResponse.ok()).toBeTruthy();
  
  // DELETE request
  const deleteResponse = await request.delete(`https://api.example.com/users/${newUser.id}`);
  expect(deleteResponse.ok()).toBeTruthy();
});
```

## Mobile Emulation

```javascript
// playwright.config.js
const { devices } = require('@playwright/test');

module.exports = defineConfig({
  projects: [
    {
      name: 'iPhone 12',
      use: { ...devices['iPhone 12'] }
    },
    {
      name: 'Pixel 5',
      use: { ...devices['Pixel 5'] }
    }
  ]
});

// Custom device
{
  name: 'Custom Phone',
  use: {
    viewport: { width: 375, height: 667 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    userAgent: 'Custom User Agent'
  }
}

// Geolocation, permissions and orientation
test('mobile test with location', async ({ page }) => {
  await page.context().grantPermissions(['geolocation']);
  await page.context().setGeolocation({ latitude: 40.7128, longitude: -74.0060 });
  
  // Set orientation
  await page.setViewportSize({ width: 667, height: 375 }); // landscape
});
```

## Common Patterns

### Page Object Model

```javascript
// LoginPage.js
class LoginPage {
  constructor(page) {
    this.page = page;
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('#login');
    this.errorMessage = page.locator('.error-message');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(username, password) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getErrorMessage() {
    return this.errorMessage.textContent();
  }
}

// DashboardPage.js
class DashboardPage {
  constructor(page) {
    this.page = page;
    this.welcomeMessage = page.locator('.welcome');
    this.logoutButton = page.locator('#logout');
  }

  async isLoaded() {
    await this.page.waitForURL('**/dashboard');
    await this.welcomeMessage.waitFor();
    return true;
  }

  async logout() {
    await this.logoutButton.click();
  }
}

// Using page objects in tests
const { test, expect } = require('@playwright/test');
const { LoginPage } = require('./LoginPage');
const { DashboardPage } = require('./DashboardPage');

test('successful login', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const dashboardPage = new DashboardPage(page);
  
  await loginPage.goto();
  await loginPage.login('user', 'password');
  
  expect(await dashboardPage.isLoaded()).toBeTruthy();
});
```

### Visual Testing

```javascript
// Basic screenshot comparison
test('visual comparison', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveScreenshot('homepage.png');
});

// With options
test('visual comparison with options', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveScreenshot('homepage.png', {
    maxDiffPixels: 100,
    threshold: 0.2,
    animations: 'disabled',
    caret: 'hide',
    mask: [page.locator('.dynamic-content')]
  });
});

// Element screenshot
test('element visual comparison', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});

// Update screenshots
npx playwright test --update-snapshots
```

### Accessibility Testing

```javascript
test('accessibility audit', async ({ page }) => {
  await page.goto('https://example.com');
  
  // Get accessibility snapshot
  const snapshot = await page.accessibility.snapshot();
  
  // Check specific elements
  expect(snapshot.children.some(node => 
    node.role === 'button' && node.name === 'Submit'
  )).toBeTruthy();
  
  // Check for specific roles
  const buttons = snapshot.children.filter(node => node.role === 'button');
  expect(buttons.length).toBeGreaterThan(0);
  
  // Check that all images have alt text
  const images = snapshot.children.filter(node => node.role === 'img');
  for (const image of images) {
    expect(image.name).toBeTruthy();
  }
});
```

### Performance Testing

```javascript
test('performance metrics', async ({ page }) => {
  // Enable JS coverage
  await page.coverage.startJSCoverage();
  await page.coverage.startCSSCoverage();
  
  // Navigate to page
  await page.goto('https://example.com');
  
  // Get performance metrics
  const metrics = await page.evaluate(() => JSON.stringify(performance.getEntriesByType('navigation')));
  const navigationMetrics = JSON.parse(metrics);
  
  // Assert on metrics
  expect(navigationMetrics[0].domContentLoadedEventEnd).toBeLessThan(1000);
  expect(navigationMetrics[0].loadEventEnd).toBeLessThan(2000);
  
  // Get coverage reports
  const jsCoverage = await page.coverage.stopJSCoverage();
  const cssCoverage = await page.coverage.stopCSSCoverage();
  
  // Calculate coverage
  let jsUsed = 0;
  let jsTotal = 0;
  for (const entry of jsCoverage) {
    jsTotal += entry.text.length;
    for (const range of entry.ranges) {
      jsUsed += range.end - range.start;
    }
  }
  
  console.log(`JS coverage: ${jsUsed / jsTotal * 100}%`);
});
```

### Multi-tab and Window Handling

```javascript
test('handle multiple tabs', async ({ page, context }) => {
  await page.goto('https://example.com');
  
  // Wait for new page when clicking link
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    page.click('a[target="_blank"]')
  ]);
  
  // Work with the new page
  await newPage.waitForLoadState();
  expect(await newPage.title()).toBe('New Page');
  
  // Switch back to original page
  await page.bringToFront();
  
  // Close the new page
  await newPage.close();
});
```

### Handling File Downloads

```javascript
test('file download', async ({ page }) => {
  await page.goto('https://example.com/download');
  
  // Start waiting for download before clicking
  const downloadPromise = page.waitForEvent('download');
  await page.click('#download-button');
  const download = await downloadPromise;
  
  // Wait for download to complete
  const path = await download.path();
  
  // Get download info
  console.log(await download.suggestedFilename());
  
  // Save to specific path
  await download.saveAs('/path/to/save/file.pdf');
  
  // Verify file content
  const fs = require('fs');
  const content = fs.readFileSync(path, 'utf8');
  expect(content).toContain('Expected content');
});
```

### Handling Dialogs

```javascript
test('handle dialogs', async ({ page }) => {
  // Set dialog handler before action that triggers dialog
  page.on('dialog', async dialog => {
    expect(dialog.type()).toBe('alert');
    expect(dialog.message()).toBe('Are you sure?');
    await dialog.accept(); // or dialog.dismiss()
  });
  
  // Trigger the dialog
  await page.click('#alert-button');
  
  // For prompts with input
  page.on('dialog', async dialog => {
    expect(dialog.type()).toBe('prompt');
    await dialog.accept('User input');
  });
  
  await page.click('#prompt-button');
});
```

### Handling iframes

```javascript
test('interact with iframe', async ({ page }) => {
  await page.goto('https://example.com/iframe-page');
  
  // Using frame locator (recommended)
  const frameLocator = page.frameLocator('#my-iframe');
  await frameLocator.locator('button').click();
  
  // Get frame by name or URL
  const frame = page.frame('frame-name');
  // or
  const frameByUrl = page.frame({ url: /.*iframe-content.html/ });
  
  // Interact with frame content
  await frame.fill('input', 'text in iframe');
  
  // Wait for frame to load
  await page.waitForSelector('#my-iframe');
  const frameElement = await page.$('#my-iframe');
  const contentFrame = await frameElement.contentFrame();
  
  // Interact with content frame
  await contentFrame.click('button');
});
```

