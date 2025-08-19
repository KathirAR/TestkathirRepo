# Playwright Interview Scenarios

This document contains realistic scenarios to assess a candidate's problem-solving abilities and practical knowledge of Playwright. These scenarios can be used in technical interviews to evaluate how candidates approach real-world testing challenges.

## Table of Contents
- [Scenario 1: Flaky Test Investigation](#scenario-1-flaky-test-investigation)
- [Scenario 2: Performance Testing](#scenario-2-performance-testing)
- [Scenario 3: Complex UI Interaction](#scenario-3-complex-ui-interaction)
- [Scenario 4: Test Architecture Design](#scenario-4-test-architecture-design)
- [Scenario 5: Debugging a Failing Test](#scenario-5-debugging-a-failing-test)
- [Assessment Guidelines](#assessment-guidelines)

---

## Scenario 1: Flaky Test Investigation

**Context:** Your team has a Playwright test suite that runs in CI. One particular test has been failing intermittently (about 30% of the time). The test is for a user registration flow that involves filling out a form, submitting it, and verifying that the user is redirected to a welcome page.

**Test Code:**

```javascript
test('user registration', async ({ page }) => {
  await page.goto('https://example.com/register');
  
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'password123');
  await page.fill('#confirm-password', 'password123');
  
  await page.click('#submit-button');
  
  await page.waitForTimeout(2000);
  
  const welcomeMessage = await page.textContent('h1');
  expect(welcomeMessage).toBe('Welcome, test@example.com!');
});
```

**Task:** Identify potential causes of flakiness in this test and propose solutions to make it more reliable.

**Expected Discussion Points:**
1. Identifying the use of `waitForTimeout` as a potential issue
2. Suggesting better waiting strategies (waitForNavigation, waitForURL, waitForSelector)
3. Discussing potential race conditions in the form submission
4. Considering network conditions and response time variations
5. Proposing retry mechanisms for flaky tests
6. Discussing how to use Playwright's tracing to debug intermittent failures

**Example Solution:**

```javascript
test('user registration', async ({ page }) => {
  await page.goto('https://example.com/register');
  
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'password123');
  await page.fill('#confirm-password', 'password123');
  
  // Wait for navigation after clicking submit
  await Promise.all([
    page.waitForNavigation({ waitUntil: 'networkidle' }),
    page.click('#submit-button')
  ]);
  
  // Wait for specific element instead of arbitrary timeout
  await page.waitForSelector('h1.welcome-message');
  
  const welcomeMessage = await page.textContent('h1.welcome-message');
  expect(welcomeMessage).toBe('Welcome, test@example.com!');
});

// In playwright.config.js
retries: process.env.CI ? 2 : 0, // Add retries in CI
use: {
  trace: 'on-first-retry', // Capture traces for debugging
}
```

---

## Scenario 2: Performance Testing

**Context:** Your team wants to implement performance testing for a critical user flow in your web application. You need to measure page load times, time to interactive, and identify potential performance bottlenecks.

**Task:** Design a Playwright test that measures key performance metrics for a user flow and sets appropriate thresholds for pass/fail criteria.

**Expected Discussion Points:**
1. Understanding of performance metrics (FCP, LCP, TTI, etc.)
2. Knowledge of Playwright's capabilities for performance measurement
3. Approaches to capture and analyze performance data
4. Setting realistic thresholds for different environments
5. Handling variability in performance measurements
6. Integration with performance monitoring tools

**Example Solution:**

```javascript
const { test, expect } = require('@playwright/test');

test('measure critical user flow performance', async ({ page }) => {
  // Start performance measurement
  await page.coverage.startJSCoverage();
  
  // Navigate to the page
  const startTime = Date.now();
  await page.goto('https://example.com/dashboard');
  
  // Wait for the page to be fully loaded and interactive
  await page.waitForSelector('#main-content', { state: 'visible' });
  await page.waitForFunction(() => 
    document.readyState === 'complete' && 
    !document.querySelector('.loading-indicator')
  );
  
  const loadTime = Date.now() - startTime;
  console.log(`Page load time: ${loadTime}ms`);
  
  // Perform user flow actions
  await page.click('#user-profile');
  const navigationStart = Date.now();
  await page.waitForNavigation();
  const navigationTime = Date.now() - navigationStart;
  
  // Get performance metrics from browser
  const performanceTimings = await page.evaluate(() => {
    const perfEntries = performance.getEntriesByType('navigation');
    return perfEntries.length > 0 ? perfEntries[0] : {};
  });
  
  // Get JS coverage
  const jsCoverage = await page.coverage.stopJSCoverage();
  let usedBytes = 0;
  let totalBytes = 0;
  for (const entry of jsCoverage) {
    totalBytes += entry.text.length;
    for (const range of entry.ranges) {
      usedBytes += range.end - range.start;
    }
  }
  
  const usedPercentage = (usedBytes / totalBytes) * 100;
  console.log(`JS coverage: ${usedPercentage.toFixed(2)}%`);
  
  // Assert on performance metrics
  expect(loadTime).toBeLessThan(3000); // Page should load within 3 seconds
  expect(navigationTime).toBeLessThan(1000); // Navigation should be under 1 second
  expect(performanceTimings.domContentLoadedEventEnd).toBeLessThan(2500);
  expect(usedPercentage).toBeGreaterThan(60); // At least 60% of JS should be used
  
  // Take a performance trace for further analysis
  await page.tracing.start({ screenshots: true, categories: ['devtools.timeline'] });
  await page.click('#another-action');
  await page.waitForResponse('**/api/data');
  await page.tracing.stop({ path: 'trace.json' });
});
```

---

## Scenario 3: Complex UI Interaction

**Context:** Your application has a complex drag-and-drop interface for a kanban board. Users can drag tasks between different columns (To Do, In Progress, Done). Each task card has buttons for editing, deleting, and viewing details.

**Task:** Write a Playwright test that:
1. Creates a new task
2. Drags it from "To Do" to "In Progress"
3. Edits the task description
4. Verifies the task appears correctly in the "In Progress" column with the updated description

**Expected Discussion Points:**
1. Handling drag-and-drop operations in Playwright
2. Strategies for waiting for UI updates after actions
3. Dealing with dynamic elements and shadow DOM if applicable
4. Approaches to verify element positions and states
5. Error handling for complex interactions
6. Test stability considerations

**Example Solution:**

```javascript
const { test, expect } = require('@playwright/test');

test('kanban board task workflow', async ({ page }) => {
  // Navigate to the kanban board
  await page.goto('https://example.com/kanban');
  
  // Create a new task
  await page.click('#create-task-button');
  await page.fill('#task-title-input', 'New Test Task');
  await page.fill('#task-description-input', 'This is a test task created by automation');
  await page.click('#save-task-button');
  
  // Wait for the task to appear in the "To Do" column
  const todoColumn = page.locator('.column[data-status="todo"]');
  const taskCard = todoColumn.locator('.task-card:has-text("New Test Task")');
  await expect(taskCard).toBeVisible();
  
  // Drag the task to "In Progress" column
  const inProgressColumn = page.locator('.column[data-status="in-progress"]');
  
  // Get source and target positions
  const sourceBox = await taskCard.boundingBox();
  const targetBox = await inProgressColumn.boundingBox();
  
  // Perform drag and drop
  await page.mouse.move(
    sourceBox.x + sourceBox.width / 2,
    sourceBox.y + sourceBox.height / 2
  );
  await page.mouse.down();
  await page.mouse.move(
    targetBox.x + targetBox.width / 2,
    targetBox.y + targetBox.height / 2,
    { steps: 10 } // Move in steps for more reliable drag
  );
  await page.mouse.up();
  
  // Wait for the task to be updated in the backend
  await page.waitForResponse(response => 
    response.url().includes('/api/tasks') && 
    response.status() === 200
  );
  
  // Verify task is now in "In Progress" column
  const movedTask = inProgressColumn.locator('.task-card:has-text("New Test Task")');
  await expect(movedTask).toBeVisible();
  
  // Edit the task
  await movedTask.locator('.edit-button').click();
  await page.fill('#task-description-input', 'Updated task description');
  await page.click('#save-task-button');
  
  // Wait for the update to be saved
  await page.waitForResponse(response => 
    response.url().includes('/api/tasks') && 
    response.status() === 200
  );
  
  // Verify the task description was updated
  await expect(movedTask).toContainText('Updated task description');
  
  // Verify task status is correctly set to "In Progress"
  const taskStatus = await page.evaluate(() => {
    const taskElement = document.querySelector('.task-card:has-text("New Test Task")');
    return taskElement.getAttribute('data-status');
  });
  
  expect(taskStatus).toBe('in-progress');
});
```

---

## Scenario 4: Test Architecture Design

**Context:** Your company is starting a new web application project, and you've been asked to design the test automation framework using Playwright. The application will be a complex SaaS platform with multiple user roles, dashboards, and integrations with third-party services.

**Task:** Design a test automation architecture that addresses:
1. Test organization and structure
2. Authentication and user management
3. Test data management
4. CI/CD integration
5. Reporting and monitoring
6. Maintenance and scalability

**Expected Discussion Points:**
1. Project structure and organization
2. Page Object Model or other design patterns
3. Authentication strategies
4. Test data generation and management
5. Test selection and parallelization
6. CI/CD pipeline integration
7. Reporting and monitoring solutions
8. Maintenance considerations

**Example Solution:**

```
Project Structure:
/tests
  /e2e                     # End-to-end tests
    /auth                  # Authentication tests
    /dashboard             # Dashboard tests
    /admin                 # Admin functionality tests
    /user                  # User functionality tests
  /api                     # API tests
  /component               # Component tests
  /performance             # Performance tests
  /accessibility           # Accessibility tests
/fixtures                  # Test fixtures and data
/pages                     # Page objects
  /components              # Reusable component objects
  /pages                   # Page objects
/utils                     # Utility functions
  /api-helpers.js          # API helper functions
  /test-data.js            # Test data generation
  /auth-helpers.js         # Authentication helpers
/config                    # Configuration files
  /playwright.config.js    # Main config
  /playwright.ci.config.js # CI-specific config
/reports                   # Test reports
```

```javascript
// Example authentication implementation
// auth-helpers.js
const { chromium } = require('@playwright/test');

async function getAuthenticatedContext(userRole) {
  // User credentials based on role
  const users = {
    admin: { email: 'admin@example.com', password: 'adminPass' },
    user: { email: 'user@example.com', password: 'userPass' },
    // Add more roles as needed
  };
  
  const user = users[userRole];
  if (!user) throw new Error(`Unknown user role: ${userRole}`);
  
  // Launch browser and create context
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // Login
  await page.goto('https://example.com/login');
  await page.fill('#email', user.email);
  await page.fill('#password', user.password);
  await page.click('#login-button');
  
  // Wait for login to complete
  await page.waitForSelector('.user-avatar');
  
  // Save storage state
  await context.storageState({ path: `./auth-${userRole}.json` });
  await browser.close();
  
  // Return path to saved storage state
  return `./auth-${userRole}.json`;
}

module.exports = { getAuthenticatedContext };

// Example test using authenticated context
// dashboard.spec.js
const { test, expect } = require('@playwright/test');
const { DashboardPage } = require('../../pages/DashboardPage');

test.describe('Dashboard tests', () => {
  test.use({ storageState: './auth-user.json' });
  
  test('user can view dashboard', async ({ page }) => {
    const dashboardPage = new DashboardPage(page);
    await dashboardPage.goto();
    await dashboardPage.waitForLoad();
    
    await expect(dashboardPage.welcomeMessage).toBeVisible();
    await expect(dashboardPage.userWidgets).toHaveCount(5);
  });
});

// Example CI configuration
// playwright.ci.config.js
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 60000,
  retries: 2,
  workers: 4,
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['junit', { outputFile: 'results.xml' }],
    ['github']
  ],
  projects: [
    {
      name: 'Chrome',
      use: { browserName: 'chromium' },
      testMatch: /.*\.spec\.js/
    },
    {
      name: 'Firefox',
      use: { browserName: 'firefox' },
      testMatch: /.*\.spec\.js/
    },
    {
      name: 'WebKit',
      use: { browserName: 'webkit' },
      testMatch: /.*\.spec\.js/
    },
    {
      name: 'API',
      testMatch: /.*\.api\.spec\.js/
    }
  ]
});
```

---

## Scenario 5: Debugging a Failing Test

**Context:** A critical test in your CI pipeline has started failing after a recent code change. The test is for a checkout process in an e-commerce application. The test passes locally but fails consistently in CI.

**Test Code:**

```javascript
test('checkout process', async ({ page }) => {
  await page.goto('https://example.com/shop');
  
  // Add item to cart
  await page.click('.product-card:first-child .add-to-cart');
  await page.click('.cart-icon');
  
  // Proceed to checkout
  await page.click('#checkout-button');
  
  // Fill shipping information
  await page.fill('#first-name', 'John');
  await page.fill('#last-name', 'Doe');
  await page.fill('#address', '123 Test St');
  await page.fill('#city', 'Test City');
  await page.fill('#zip', '12345');
  await page.selectOption('#country', 'US');
  
  // Continue to payment
  await page.click('#continue-to-payment');
  
  // Fill payment information
  await page.fill('#card-number', '4111111111111111');
  await page.fill('#card-expiry', '12/25');
  await page.fill('#card-cvc', '123');
  
  // Complete order
  await page.click('#complete-order');
  
  // Verify order confirmation
  await expect(page.locator('.order-confirmation')).toBeVisible();
  await expect(page.locator('.order-number')).toBeVisible();
});
```

**CI Error:**
```
Error: Timeout 30000ms exceeded.
=========================== logs ===========================
waiting for locator('#continue-to-payment')
============================================================
```

**Task:** Analyze the potential causes of the failure and propose debugging steps and solutions.

**Expected Discussion Points:**
1. Differences between local and CI environments
2. Strategies for debugging timing/async issues
3. Using Playwright's tracing and debugging tools
4. Improving test reliability in CI
5. Approaches to reproduce and fix the issue

**Example Solution:**

```javascript
// Debugging approach:

// 1. Enable verbose logging and tracing
// playwright.config.js
use: {
  trace: 'on',
  video: 'on',
  screenshot: 'on',
}

// 2. Add explicit waiting and logging
test('checkout process', async ({ page }) => {
  // Enable request/response logging
  page.on('request', request => console.log(`Request: ${request.method()} ${request.url()}`));
  page.on('response', response => console.log(`Response: ${response.status()} ${response.url()}`));
  
  await page.goto('https://example.com/shop');
  console.log('Page loaded');
  
  // Add item to cart with better waiting
  await page.click('.product-card:first-child .add-to-cart');
  await page.waitForResponse(response => 
    response.url().includes('/api/cart') && 
    response.status() === 200
  );
  console.log('Item added to cart');
  
  await page.click('.cart-icon');
  await page.waitForSelector('#checkout-button', { state: 'visible' });
  
  // Proceed to checkout with navigation waiting
  await Promise.all([
    page.waitForNavigation(),
    page.click('#checkout-button')
  ]);
  console.log('Navigated to checkout');
  
  // Verify shipping form is loaded before filling
  await page.waitForSelector('#shipping-form', { state: 'visible' });
  
  // Fill shipping information
  await page.fill('#first-name', 'John');
  await page.fill('#last-name', 'Doe');
  await page.fill('#address', '123 Test St');
  await page.fill('#city', 'Test City');
  await page.fill('#zip', '12345');
  await page.selectOption('#country', 'US');
  console.log('Shipping info filled');
  
  // Check if continue button is actually visible and enabled
  await page.waitForSelector('#continue-to-payment', { state: 'visible' });
  const isEnabled = await page.isEnabled('#continue-to-payment');
  console.log(`Continue button enabled: ${isEnabled}`);
  
  // Take screenshot before clicking
  await page.screenshot({ path: 'before-continue.png' });
  
  // Continue to payment with retry logic
  try {
    await page.click('#continue-to-payment', { timeout: 5000 });
  } catch (e) {
    console.log('First click attempt failed, retrying...');
    // Check for any overlays or modals
    const overlays = await page.$$('.modal, .overlay, .spinner');
    if (overlays.length > 0) {
      console.log(`Found ${overlays.length} potential overlays`);
      // Wait for overlays to disappear
      await page.waitForSelector('.modal, .overlay, .spinner', { state: 'hidden', timeout: 10000 });
    }
    // Try clicking again
    await page.click('#continue-to-payment');
  }
  
  console.log('Clicked continue to payment');
  
  // Wait for payment form with longer timeout
  await page.waitForSelector('#payment-form', { state: 'visible', timeout: 60000 });
  
  // Rest of the test...
});

// 3. Investigate CI-specific issues
// - Check if there are network latency differences
// - Verify if there are any CI-specific feature flags
// - Check if the application behaves differently in headless mode
// - Verify browser/OS differences between local and CI

// 4. Potential fixes:
// - Add explicit waits for network requests to complete
// - Increase timeouts in CI environment
// - Add retry logic for flaky steps
// - Check for CI-specific environment variables affecting the application
// - Consider using visual assertions to verify page state
```

---

## Assessment Guidelines

When evaluating candidates based on these scenarios, consider the following criteria:

### Junior Level (0-2 years experience)
- **Problem Identification:** Should identify basic issues like improper waiting
- **Solution Quality:** May propose simple fixes that address the immediate problem
- **Technical Knowledge:** Should demonstrate basic understanding of Playwright's API
- **Expected Performance:** Can partially solve simpler scenarios (1 and 5)

### Mid-Level (2-5 years experience)
- **Problem Analysis:** Should identify multiple potential causes for issues
- **Solution Depth:** Should propose comprehensive solutions with proper error handling
- **Best Practices:** Should incorporate testing best practices in solutions
- **Technical Knowledge:** Should demonstrate good understanding of Playwright's capabilities
- **Expected Performance:** Can fully solve scenarios 1, 3, and 5, and partially solve 2 and 4

### Senior Level (5+ years experience)
- **Comprehensive Analysis:** Should identify all potential issues, including edge cases
- **Solution Architecture:** Should propose robust, maintainable solutions
- **System Thinking:** Should consider the broader testing ecosystem and integration points
- **Advanced Knowledge:** Should demonstrate deep understanding of Playwright and testing principles
- **Expected Performance:** Can fully solve all scenarios with optimal solutions

### Evaluation Process

1. **Initial Response:**
   - How quickly does the candidate identify the core issues?
   - Do they ask clarifying questions before jumping to solutions?

2. **Solution Approach:**
   - Is their approach methodical and structured?
   - Do they consider multiple solutions before selecting one?
   - Do they explain their reasoning clearly?

3. **Technical Depth:**
   - How well do they understand Playwright's capabilities?
   - Do they demonstrate knowledge of testing principles beyond the tool itself?
   - Can they discuss trade-offs between different approaches?

4. **Code Quality:**
   - Is their proposed code well-structured and maintainable?
   - Do they incorporate error handling and resilience?
   - Do they follow best practices for test automation?

5. **Communication:**
   - How clearly do they explain complex technical concepts?
   - Can they discuss solutions at different levels of abstraction?
   - Do they demonstrate good collaboration skills when discussing approaches?

