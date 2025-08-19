# Playwright Interview Question Sets

This document contains comprehensive interview question sets for assessing candidates' knowledge of Playwright, organized by experience level and topic area.

## Table of Contents
- [Beginner Level Questions](#beginner-level-questions)
- [Intermediate Level Questions](#intermediate-level-questions)
- [Advanced Level Questions](#advanced-level-questions)
- [Scenario-Based Questions](#scenario-based-questions)
- [Code Review Questions](#code-review-questions)
- [Interview Assessment Guidelines](#interview-assessment-guidelines)

---

## Beginner Level Questions

### Fundamentals of Playwright

1. **What is Playwright and what problem does it solve in web testing?**
   - *Expected answer:* Playwright is a modern automation testing framework for web applications that allows for cross-browser testing. It solves problems like flaky tests, browser compatibility issues, and provides reliable automation across Chromium, Firefox, and WebKit browsers.

2. **Which browsers and platforms does Playwright support?**
   - *Expected answer:* Playwright supports Chromium (Chrome, Edge), Firefox, and WebKit (Safari) browsers across Windows, macOS, and Linux operating systems.

3. **How do you install Playwright in a project?**
   - *Expected answer:* Using npm: `npm init playwright@latest` or `npm install -D @playwright/test`

4. **What programming languages can be used with Playwright?**
   - *Expected answer:* JavaScript, TypeScript, Python, Java, and .NET (C#)

5. **Explain the difference between Playwright and Selenium.**
   - *Expected answer:* Playwright is more modern with better auto-waiting capabilities, has a more consistent cross-browser API, better mobile emulation, and generally faster and more reliable tests. Selenium has broader browser support and a larger community but often requires more explicit waits and handling.

6. **What is a Playwright fixture and how is it used?**
   - *Expected answer:* Fixtures in Playwright are a way to establish a environment for testing, providing things like browser instances, pages, and custom test data. They help with test setup, teardown, and sharing objects between tests.

7. **How do you launch a browser in Playwright?**
   - *Expected answer:* Using the `playwright.chromium.launch()` method (or firefox/webkit), or through the test runner which handles this automatically.

8. **What is the purpose of the `page` object in Playwright?**
   - *Expected answer:* The `page` object represents a page in the browser. It provides APIs to interact with the page, navigate to URLs, interact with elements, handle dialogs, etc.

9. **How do you navigate to a URL in Playwright?**
   - *Expected answer:* Using `await page.goto('https://example.com')` method.

10. **What are locators in Playwright and how do they work?**
    - *Expected answer:* Locators are the primary way to interact with page elements. They automatically wait for elements to be actionable and retry operations if needed. Example: `page.locator('button.submit')`.

### Basic Interactions

11. **How do you click a button in Playwright?**
    - *Expected answer:* `await page.click('button.submit')` or `await page.locator('button.submit').click()`

12. **How do you fill a form field in Playwright?**
    - *Expected answer:* `await page.fill('#username', 'myname')` or `await page.locator('#username').fill('myname')`

13. **How do you handle a browser alert/dialog in Playwright?**
    - *Expected answer:* Using dialog event listeners: 
      ```javascript
      page.on('dialog', dialog => dialog.accept());
      ```

14. **How do you take a screenshot in Playwright?**
    - *Expected answer:* `await page.screenshot({ path: 'screenshot.png' })`

15. **How do you check if an element is visible on the page?**
    - *Expected answer:* `await expect(page.locator('.element')).toBeVisible()`

---

## Intermediate Level Questions

### Advanced Playwright Concepts

16. **Explain Playwright's auto-waiting mechanism.**
    - *Expected answer:* Playwright automatically waits for elements to be actionable before performing actions. It waits for elements to be visible, enabled, and stable before clicking, for example, reducing the need for explicit waits.

17. **What are the different selector engines available in Playwright?**
    - *Expected answer:* CSS selectors, XPath, text selectors (text=Button), CSS-in-JS selectors (css=button), role selectors (role=button), and test ID selectors (data-testid=submit).

18. **How do you handle iframes in Playwright?**
    - *Expected answer:* Using the `frameLocator` method:
      ```javascript
      const frameLocator = page.frameLocator('#iframe');
      await frameLocator.locator('button').click();
      ```

19. **How can you debug Playwright tests?**
    - *Expected answer:* Using the Playwright Inspector with `npx playwright test --debug`, adding `page.pause()` in tests, using the `--headed` flag, or using the VS Code extension.

20. **What is the difference between `locator.click()` and `page.click()`?**
    - *Expected answer:* `page.click()` is a convenience method that creates a locator internally and then calls click on it. `locator.click()` is used when you want to reuse a locator for multiple operations.

21. **How do you handle multiple tabs/windows in Playwright?**
    - *Expected answer:* Using the `context.waitForEvent('page')` method to capture new pages/tabs:
      ```javascript
      const [newPage] = await Promise.all([
        context.waitForEvent('page'),
        page.click('a[target="_blank"]')
      ]);
      ```

22. **Explain how to use Playwright's network interception capabilities.**
    - *Expected answer:* Using `page.route()` to intercept network requests and modify responses:
      ```javascript
      await page.route('**/api/users', route => {
        route.fulfill({
          status: 200,
          body: JSON.stringify([{ name: 'John' }])
        });
      });
      ```

23. **How do you handle authentication in Playwright tests?**
    - *Expected answer:* By setting up the authentication state once and reusing it with `browserContext.storageState()`:
      ```javascript
      // Login
      await page.fill('#username', 'user');
      await page.fill('#password', 'pass');
      await page.click('#login');
      
      // Save storage state
      await context.storageState({ path: 'auth.json' });
      
      // Reuse in other tests
      const context = await browser.newContext({ storageState: 'auth.json' });
      ```

24. **What are Playwright traces and how do you use them?**
    - *Expected answer:* Traces are recordings of test executions that can be used for debugging. They capture screenshots, DOM snapshots, and network requests:
      ```javascript
      // In config
      use: {
        trace: 'on-first-retry', // or 'on', 'off', 'retain-on-failure'
      }
      
      // View traces
      npx playwright show-trace trace.zip
      ```

25. **How do you handle file downloads in Playwright?**
    - *Expected answer:* Using the `page.waitForEvent('download')` method:
      ```javascript
      const [download] = await Promise.all([
        page.waitForEvent('download'),
        page.click('button#download')
      ]);
      const path = await download.path();
      ```

### Testing Frameworks and Assertions

26. **How do you structure tests in Playwright Test?**
    - *Expected answer:* Using the `test` function to define test cases and `describe` to group related tests:
      ```javascript
      test.describe('Login functionality', () => {
        test('should login with valid credentials', async ({ page }) => {
          // Test code
        });
      });
      ```

27. **What assertions are available in Playwright Test?**
    - *Expected answer:* Playwright Test includes expect assertions like `toBeVisible()`, `toHaveText()`, `toHaveValue()`, `toBeEnabled()`, etc.

28. **How do you run a specific test or test file in Playwright?**
    - *Expected answer:* Using test name or file patterns:
      ```
      npx playwright test login.spec.ts
      npx playwright test -g "should login"
      ```

29. **How do you parameterize tests in Playwright?**
    - *Expected answer:* Using test.describe.parallel.each() or for simple cases with arrays:
      ```javascript
      const users = [
        { name: 'User1', password: 'pass1' },
        { name: 'User2', password: 'pass2' }
      ];
      
      for (const user of users) {
        test(`login as ${user.name}`, async ({ page }) => {
          // Test with this user
        });
      }
      ```

30. **How do you set up and tear down test fixtures in Playwright?**
    - *Expected answer:* Using beforeEach, afterEach, beforeAll, and afterAll hooks:
      ```javascript
      test.beforeEach(async ({ page }) => {
        await page.goto('https://example.com');
      });
      
      test.afterEach(async ({ page }) => {
        // Cleanup
      });
      ```

---

## Advanced Level Questions

### Performance and Optimization

31. **How can you make Playwright tests run faster?**
    - *Expected answer:* By running tests in parallel, using the same browser instance for multiple tests, using storage state for authentication, disabling unnecessary browser features, and using specific selectors.

32. **Explain how to implement visual regression testing with Playwright.**
    - *Expected answer:* Using the `toMatchSnapshot()` assertion:
      ```javascript
      await expect(page).toHaveScreenshot('homepage.png');
      ```
      Or using third-party visual comparison tools like Percy or Applitools.

33. **How do you handle flaky tests in Playwright?**
    - *Expected answer:* By using more reliable selectors, adding proper waiting mechanisms, increasing timeouts for specific operations, using retry mechanisms, and analyzing test traces to identify issues.

34. **How would you implement custom retry logic for specific test actions?**
    - *Expected answer:* Using a custom retry function:
      ```javascript
      async function retryOperation(maxAttempts, operation) {
        let lastError;
        for (let attempt = 1; attempt <= maxAttempts; attempt++) {
          try {
            return await operation();
          } catch (error) {
            lastError = error;
            console.log(`Attempt ${attempt} failed, retrying...`);
            await page.waitForTimeout(1000); // Wait before retry
          }
        }
        throw lastError;
      }
      
      await retryOperation(3, async () => {
        await page.click('#flaky-button');
      });
      ```

35. **How do you implement API testing alongside UI testing in Playwright?**
    - *Expected answer:* Using Playwright's `request` fixture:
      ```javascript
      test('API test', async ({ request }) => {
        const response = await request.get('https://api.example.com/users');
        expect(response.ok()).toBeTruthy();
        const body = await response.json();
        expect(body.users.length).toBeGreaterThan(0);
      });
      ```

### Advanced Scenarios and Techniques

36. **How would you test WebSockets with Playwright?**
    - *Expected answer:* By listening to WebSocket frames:
      ```javascript
      await page.route('**/*', route => {
        const request = route.request();
        if (request.resourceType() === 'websocket') {
          // Handle WebSocket
        }
        return route.continue();
      });
      ```

37. **How do you test canvas elements with Playwright?**
    - *Expected answer:* By using JavaScript execution to interact with the canvas API:
      ```javascript
      await page.evaluate(() => {
        const canvas = document.querySelector('canvas');
        const context = canvas.getContext('2d');
        // Interact with canvas
      });
      ```

38. **Explain how to implement custom selector engines in Playwright.**
    - *Expected answer:* By registering a custom selector engine:
      ```javascript
      await playwright.selectors.register('data-qa', () => ({
        query(root, selector) {
          return root.querySelector(`[data-qa="${selector}"]`);
        },
        queryAll(root, selector) {
          return Array.from(root.querySelectorAll(`[data-qa="${selector}"]`));
        }
      }));
      
      // Usage
      await page.click('data-qa=submit-button');
      ```

39. **How would you implement accessibility testing with Playwright?**
    - *Expected answer:* Using Playwright's accessibility testing capabilities:
      ```javascript
      const snapshot = await page.accessibility.snapshot();
      expect(snapshot.children.some(node => 
        node.role === 'button' && node.name === 'Submit'
      )).toBeTruthy();
      ```

40. **How do you test responsive design with Playwright?**
    - *Expected answer:* By using different viewport sizes and device emulation:
      ```javascript
      // In config
      projects: [
        {
          name: 'Desktop Chrome',
          use: { browserName: 'chromium', viewport: { width: 1280, height: 720 } },
        },
        {
          name: 'Mobile Safari',
          use: { browserName: 'webkit', ...devices['iPhone 12'] },
        }
      ]
      ```

41. **How would you implement load testing or performance measurement with Playwright?**
    - *Expected answer:* Using Playwright's performance API and custom metrics:
      ```javascript
      const performanceTiming = await page.evaluate(() => 
        JSON.stringify(performance.getEntriesByType('navigation'))
      );
      const metrics = JSON.parse(performanceTiming);
      expect(metrics[0].domContentLoadedEventEnd).toBeLessThan(1000);
      ```

42. **How do you handle shadow DOM elements in Playwright?**
    - *Expected answer:* Playwright can pierce through shadow DOM automatically with standard selectors:
      ```javascript
      await page.click('button#shadow-host >>> .shadow-content');
      // Or with newer syntax
      await page.click('button#shadow-host ::-p-deep(.shadow-content)');
      ```

43. **Explain how to implement data-driven testing in Playwright.**
    - *Expected answer:* Using external data sources and parameterized tests:
      ```javascript
      const testData = require('./test-data.json');
      
      for (const data of testData) {
        test(`Test scenario: ${data.name}`, async ({ page }) => {
          await page.goto(data.url);
          await page.fill('#input', data.input);
          await page.click('#submit');
          await expect(page.locator('#result')).toHaveText(data.expected);
        });
      }
      ```

44. **How would you implement cross-browser testing strategies with Playwright?**
    - *Expected answer:* Using Playwright's multi-browser projects:
      ```javascript
      // In playwright.config.js
      projects: [
        {
          name: 'chromium',
          use: { browserName: 'chromium' },
        },
        {
          name: 'firefox',
          use: { browserName: 'firefox' },
        },
        {
          name: 'webkit',
          use: { browserName: 'webkit' },
        },
      ]
      ```

45. **How do you implement custom reporting in Playwright tests?**
    - *Expected answer:* By using custom reporters:
      ```javascript
      // In playwright.config.js
      reporter: [
        ['html'],
        ['json', { outputFile: 'results.json' }],
        ['./my-custom-reporter.js']
      ]
      
      // Custom reporter implementation
      class MyReporter {
        onBegin(config, suite) {
          console.log(`Starting the run with ${suite.allTests().length} tests`);
        }
        
        onTestEnd(test, result) {
          console.log(`Test ${test.title} finished with status ${result.status}`);
        }
        
        onEnd(result) {
          console.log(`Finished the run: ${result.status}`);
        }
      }
      ```

---

## Scenario-Based Questions

46. **Scenario: You need to test a complex single-page application with dynamic content loading. How would you approach this with Playwright?**
    - *Expected answer:* I would use Playwright's auto-waiting capabilities and network idle detection. For dynamic content, I'd use waitForSelector or waitForLoadState('networkidle'). I'd also implement request interception to stabilize API responses and use custom assertions to verify content loading correctly.

47. **Scenario: Your team is migrating from Selenium to Playwright. What migration strategy would you recommend and what challenges do you anticipate?**
    - *Expected answer:* I'd recommend a phased approach, starting with new tests in Playwright while maintaining existing Selenium tests. Gradually refactor critical paths to Playwright. Challenges include: different selector strategies, adapting to Playwright's auto-waiting (vs explicit waits in Selenium), and training the team on the new framework. I'd create a selector strategy guide and common patterns document to help the team transition.

48. **Scenario: You notice that tests are failing intermittently in the CI pipeline but pass locally. How would you debug and fix this issue?**
    - *Expected answer:* I would:
      1. Enable Playwright traces in CI to capture detailed execution information
      2. Add video recording for failing tests
      3. Check for environment-specific issues (browser versions, viewport sizes)
      4. Look for race conditions or timing issues
      5. Check for resource constraints in CI (memory, CPU)
      6. Implement retries for flaky tests while investigating
      7. Consider using containerization to ensure consistent environments

49. **Scenario: You need to test a feature that involves file uploads and downloads. How would you implement this in Playwright?**
    - *Expected answer:* For uploads:
      ```javascript
      await page.setInputFiles('input[type="file"]', 'path/to/file.pdf');
      ```
      
      For downloads:
      ```javascript
      const [download] = await Promise.all([
        page.waitForEvent('download'),
        page.click('#download-button')
      ]);
      
      const path = await download.path();
      // Verify file contents
      const fs = require('fs');
      const content = fs.readFileSync(path, 'utf8');
      expect(content).toContain('expected text');
      ```

50. **Scenario: Your application uses a third-party authentication provider. How would you handle authentication in your Playwright tests?**
    - *Expected answer:* I would:
      1. Set up authentication once and save the state:
         ```javascript
         // Login through UI or API
         await page.goto('https://auth-provider.com');
         await page.fill('#email', 'user@example.com');
         await page.fill('#password', 'password');
         await page.click('#login');
         await page.waitForURL('https://myapp.com/dashboard');
         
         // Save authentication state
         await context.storageState({ path: 'auth.json' });
         ```
      
      2. Reuse the authentication state in tests:
         ```javascript
         const context = await browser.newContext({ 
           storageState: 'auth.json' 
         });
         const page = await context.newPage();
         ```
      
      3. For CI, I might mock the auth provider or use API authentication instead of UI login.

---

## Code Review Questions

51. **What's wrong with this Playwright test code?**
    ```javascript
    test('submits a form', async ({ page }) => {
      await page.goto('https://example.com/form');
      page.fill('#username', 'testuser');
      page.fill('#password', 'password123');
      page.click('#submit');
      expect(page.locator('.success-message').isVisible()).toBeTruthy();
    });
    ```
    - *Expected answer:* Multiple issues:
      1. Missing `await` for page.fill and page.click operations
      2. Incorrect assertion syntax - should use `await expect(page.locator('.success-message')).toBeVisible()`
      3. No waiting for form submission to complete
      4. No error handling

52. **How would you improve this Playwright test?**
    ```javascript
    test('user login test', async ({ page }) => {
      await page.goto('https://example.com');
      await page.click('text=Login');
      await page.type('#username', 'user1');
      await page.type('#password', 'pass123');
      await page.click('#loginButton');
      await page.waitForTimeout(2000);
      const welcomeMessage = await page.textContent('#welcome');
      expect(welcomeMessage).toContain('Welcome');
    });
    ```
    - *Expected answer:* Improvements:
      1. Replace `page.type()` with `page.fill()` for better reliability
      2. Replace arbitrary `waitForTimeout` with proper waiting: `await page.waitForSelector('#welcome')`
      3. Use Playwright's built-in assertions: `await expect(page.locator('#welcome')).toContainText('Welcome')`
      4. Add error handling or test retry logic
      5. Consider extracting login steps to a reusable function or fixture

53. **Review this code and identify potential issues:**
    ```javascript
    const { test, expect } = require('@playwright/test');
    
    test('adds item to cart', async ({ page }) => {
      await page.goto('https://shop.example.com');
      const products = await page.$$('.product');
      await products[0].click();
      await page.click('button.add-to-cart');
      const cartCount = await page.$eval('.cart-count', el => el.textContent);
      expect(cartCount).toBe('1');
    });
    ```
    - *Expected answer:* Issues:
      1. Using `page.$$` and array indexing is brittle - better to use locators
      2. No waiting for navigation after clicking the product
      3. No verification that the correct product was added
      4. The assertion doesn't account for existing items in cart
      5. No error handling if elements aren't found
      
      Better approach:
      ```javascript
      test('adds item to cart', async ({ page }) => {
        await page.goto('https://shop.example.com');
        const firstProduct = page.locator('.product').first();
        const productName = await firstProduct.locator('.name').textContent();
        await firstProduct.click();
        await page.waitForURL('**/product/*');
        await page.click('button.add-to-cart');
        await expect(page.locator('.cart-count')).toHaveText('1');
        await page.click('.view-cart');
        await expect(page.locator('.cart-item .name')).toHaveText(productName);
      });
      ```

54. **What's wrong with this page object implementation?**
    ```javascript
    class LoginPage {
      constructor(page) {
        this.page = page;
        this.usernameInput = '#username';
        this.passwordInput = '#password';
        this.loginButton = '#login';
      }
      
      async login(username, password) {
        await this.page.fill(this.usernameInput, username);
        await this.page.fill(this.passwordInput, password);
        await this.page.click(this.loginButton);
      }
    }
    ```
    - *Expected answer:* Issues:
      1. No navigation to the login page in the class
      2. Using string selectors directly instead of Playwright locators
      3. No waiting for login completion or verification of successful login
      4. No error handling
      
      Improved version:
      ```javascript
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
          // Wait for navigation or success indicator
          await this.page.waitForURL('/dashboard');
        }
        
        async getErrorMessage() {
          return this.errorMessage.textContent();
        }
      }
      ```

55. **What issues do you see with this test configuration?**
    ```javascript
    // playwright.config.js
    module.exports = {
      timeout: 5000,
      retries: 0,
      use: {
        headless: true,
        viewport: { width: 1280, height: 720 },
        launchOptions: {
          slowMo: 100,
        },
      },
      projects: [
        {
          name: 'Chrome',
          use: {
            browserName: 'chromium',
          },
        },
        {
          name: 'Firefox',
          use: {
            browserName: 'firefox',
          },
        },
      ],
    };
    ```
    - *Expected answer:* Issues:
      1. Timeout of 5000ms is too short for many real-world scenarios
      2. No retries configured for flaky tests (retries: 0)
      3. slowMo will make tests run slower unnecessarily in headless mode
      4. No trace or screenshot configuration for debugging failures
      5. No reporter configuration for better test results visualization
      
      Improved version:
      ```javascript
      module.exports = {
        timeout: 30000,
        retries: process.env.CI ? 2 : 0, // Retry in CI
        reporter: [['html'], ['junit', { outputFile: 'results.xml' }]],
        use: {
          headless: process.env.CI ? true : false,
          viewport: { width: 1280, height: 720 },
          trace: process.env.CI ? 'on-first-retry' : 'on',
          screenshot: 'only-on-failure',
          video: 'on-first-retry',
        },
        projects: [
          {
            name: 'Chrome',
            use: { browserName: 'chromium' },
          },
          {
            name: 'Firefox',
            use: { browserName: 'firefox' },
          },
        ],
      };
      ```

---

## Interview Assessment Guidelines

### Evaluation Criteria

When evaluating candidates based on their responses to these questions, consider the following criteria:

#### Junior Level (0-2 years experience)
- **Basic Knowledge:** Should be able to answer most beginner questions correctly
- **Tool Familiarity:** Should demonstrate understanding of basic Playwright commands and concepts
- **Problem Solving:** Should be able to identify simple issues in code examples
- **Expected Score:** 60-70% correct on beginner questions, 30-40% on intermediate

#### Mid-Level (2-5 years experience)
- **Comprehensive Knowledge:** Should answer most beginner and intermediate questions correctly
- **Best Practices:** Should demonstrate understanding of testing best practices
- **Problem Identification:** Should identify most issues in code review questions
- **Practical Experience:** Should provide practical examples from experience
- **Expected Score:** 90%+ on beginner, 70-80% on intermediate, 40-50% on advanced

#### Senior Level (5+ years experience)
- **Expert Knowledge:** Should answer beginner and intermediate questions with depth and nuance
- **Advanced Concepts:** Should demonstrate strong understanding of advanced topics
- **Architecture Understanding:** Should articulate testing architecture considerations
- **Problem Solving:** Should provide multiple solutions to scenario-based questions
- **Code Quality:** Should identify all issues in code review questions and suggest optimal solutions
- **Expected Score:** 90%+ across all categories, with particular strength in scenarios and advanced topics

### Interview Structure Recommendations

1. **Screening Round:**
   - Select 5-7 questions from the beginner section
   - Include 1-2 basic code review questions
   - Time allocation: 20-30 minutes

2. **Technical Interview:**
   - Mix of questions based on candidate's experience level:
     - Junior: 70% beginner, 30% intermediate
     - Mid-level: 30% beginner, 50% intermediate, 20% advanced
     - Senior: 20% beginner, 40% intermediate, 40% advanced
   - Include at least 2 scenario-based questions
   - Include at least 2 code review questions
   - Time allocation: 45-60 minutes

3. **Practical Assessment:**
   - Consider adding a take-home or live coding exercise where the candidate writes actual Playwright tests
   - For senior roles, include a system design component (e.g., "Design a test automation framework using Playwright")

### Red Flags

- Inability to explain basic Playwright concepts
- Confusion between Playwright and other testing frameworks
- Overreliance on sleep/timeout instead of proper waiting strategies
- Poor understanding of asynchronous testing concepts
- Inability to identify basic issues in code review questions
- No consideration for test reliability or maintenance

### Green Flags

- Deep understanding of Playwright's unique features
- Emphasis on test reliability and maintenance
- Knowledge of performance optimization techniques
- Experience with CI/CD integration
- Understanding of when to use UI tests vs API tests
- Ability to discuss trade-offs between different testing approaches

