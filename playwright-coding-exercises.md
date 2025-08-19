# Playwright Coding Exercises

This document contains practical coding exercises to assess candidates' hands-on skills with Playwright. These exercises can be used as take-home assignments or as part of a live coding interview.

## Table of Contents
- [Exercise 1: Basic Page Interaction](#exercise-1-basic-page-interaction)
- [Exercise 2: Form Validation Testing](#exercise-2-form-validation-testing)
- [Exercise 3: API Testing with Playwright](#exercise-3-api-testing-with-playwright)
- [Exercise 4: E-commerce User Flow](#exercise-4-e-commerce-user-flow)
- [Exercise 5: Advanced - Component Testing](#exercise-5-advanced---component-testing)
- [Assessment Guidelines](#assessment-guidelines)

---

## Exercise 1: Basic Page Interaction

**Difficulty Level:** Beginner

**Task:** Write a Playwright test that navigates to a website, interacts with elements, and verifies content.

**Requirements:**
1. Navigate to a public website (e.g., https://playwright.dev)
2. Verify the page title
3. Click on a navigation link
4. Verify that new content has loaded
5. Search for a term using a search box
6. Verify search results contain the expected term

**Example Solution:**

```javascript
const { test, expect } = require('@playwright/test');

test('Basic page interaction', async ({ page }) => {
  // Navigate to website
  await page.goto('https://playwright.dev');
  
  // Verify page title
  await expect(page).toHaveTitle(/Playwright/);
  
  // Click on a navigation link (e.g., "Docs")
  await page.click('text=Docs');
  
  // Verify new content has loaded
  await expect(page).toHaveURL(/.*docs/);
  await expect(page.locator('h1')).toContainText('Installation');
  
  // Search for a term
  await page.fill('[placeholder="Search docs"]', 'locator');
  await page.press('[placeholder="Search docs"]', 'Enter');
  
  // Verify search results
  await expect(page.locator('.search-result')).toContainText('locator');
});
```

**Evaluation Criteria:**
- Proper use of Playwright's API
- Effective use of locators
- Appropriate assertions
- Code readability and structure

---

## Exercise 2: Form Validation Testing

**Difficulty Level:** Intermediate

**Task:** Write tests for a form that validate both successful submission and error handling.

**Requirements:**
1. Navigate to a form page (can use a public demo site like https://demoqa.com/automation-practice-form)
2. Test the happy path - fill all required fields and submit successfully
3. Test validation errors - submit without required fields
4. Test field-specific validation (e.g., email format, phone number format)
5. Implement a Page Object Model pattern for the form

**Example Solution:**

```javascript
// formPage.js
class FormPage {
  constructor(page) {
    this.page = page;
    this.firstNameInput = page.locator('#firstName');
    this.lastNameInput = page.locator('#lastName');
    this.emailInput = page.locator('#userEmail');
    this.genderRadio = page.locator('label[for="gender-radio-1"]');
    this.mobileInput = page.locator('#userNumber');
    this.submitButton = page.locator('#submit');
    this.confirmationModal = page.locator('.modal-content');
    this.errorMessages = page.locator('.field-error');
  }

  async goto() {
    await this.page.goto('https://demoqa.com/automation-practice-form');
  }

  async fillForm(firstName, lastName, email, mobile) {
    await this.firstNameInput.fill(firstName);
    await this.lastNameInput.fill(lastName);
    await this.emailInput.fill(email);
    await this.genderRadio.click();
    await this.mobileInput.fill(mobile);
  }

  async submitForm() {
    await this.submitButton.click();
  }

  async getConfirmationText() {
    return this.confirmationModal.textContent();
  }

  async getErrorMessages() {
    return this.errorMessages.allTextContents();
  }
}

// form.spec.js
const { test, expect } = require('@playwright/test');
const { FormPage } = require('./formPage');

test.describe('Form validation tests', () => {
  let formPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('successful form submission', async () => {
    await formPage.fillForm('John', 'Doe', 'john.doe@example.com', '1234567890');
    await formPage.submitForm();
    
    const confirmationText = await formPage.getConfirmationText();
    expect(confirmationText).toContain('Thanks for submitting the form');
    expect(confirmationText).toContain('John Doe');
    expect(confirmationText).toContain('john.doe@example.com');
  });

  test('form validation - empty required fields', async () => {
    // Submit without filling any fields
    await formPage.submitForm();
    
    const errorMessages = await formPage.getErrorMessages();
    expect(errorMessages.length).toBeGreaterThan(0);
  });

  test('email validation', async () => {
    await formPage.fillForm('John', 'Doe', 'invalid-email', '1234567890');
    await formPage.submitForm();
    
    const errorMessages = await formPage.getErrorMessages();
    expect(errorMessages.some(msg => msg.includes('email'))).toBeTruthy();
  });
});
```

**Evaluation Criteria:**
- Implementation of Page Object Model
- Test organization and structure
- Error handling and validation testing
- Use of test hooks (beforeEach, etc.)
- Code reusability

---

## Exercise 3: API Testing with Playwright

**Difficulty Level:** Intermediate

**Task:** Write tests that use Playwright's API testing capabilities to test a REST API.

**Requirements:**
1. Use Playwright's `request` fixture to test a public API (e.g., https://jsonplaceholder.typicode.com)
2. Write tests for GET, POST, PUT, and DELETE operations
3. Validate response status codes and body content
4. Handle authentication if the API requires it
5. Implement data-driven tests for multiple test cases

**Example Solution:**

```javascript
const { test, expect } = require('@playwright/test');

const API_BASE_URL = 'https://jsonplaceholder.typicode.com';

test.describe('API testing with Playwright', () => {
  test('GET request - fetch users', async ({ request }) => {
    const response = await request.get(`${API_BASE_URL}/users`);
    
    expect(response.status()).toBe(200);
    
    const responseBody = await response.json();
    expect(Array.isArray(responseBody)).toBeTruthy();
    expect(responseBody.length).toBeGreaterThan(0);
    expect(responseBody[0]).toHaveProperty('id');
    expect(responseBody[0]).toHaveProperty('name');
    expect(responseBody[0]).toHaveProperty('email');
  });

  test('GET request - fetch specific user', async ({ request }) => {
    const userId = 1;
    const response = await request.get(`${API_BASE_URL}/users/${userId}`);
    
    expect(response.status()).toBe(200);
    
    const user = await response.json();
    expect(user.id).toBe(userId);
    expect(user.name).toBeTruthy();
    expect(user.email).toMatch(/@/);
  });

  test('POST request - create new post', async ({ request }) => {
    const newPost = {
      title: 'Playwright API Testing',
      body: 'This is a test post created with Playwright',
      userId: 1
    };
    
    const response = await request.post(`${API_BASE_URL}/posts`, {
      data: newPost
    });
    
    expect(response.status()).toBe(201);
    
    const createdPost = await response.json();
    expect(createdPost).toHaveProperty('id');
    expect(createdPost.title).toBe(newPost.title);
    expect(createdPost.body).toBe(newPost.body);
    expect(createdPost.userId).toBe(newPost.userId);
  });

  test('PUT request - update post', async ({ request }) => {
    const postId = 1;
    const updatedData = {
      title: 'Updated Title',
      body: 'This post has been updated with Playwright',
      userId: 1
    };
    
    const response = await request.put(`${API_BASE_URL}/posts/${postId}`, {
      data: updatedData
    });
    
    expect(response.status()).toBe(200);
    
    const updatedPost = await response.json();
    expect(updatedPost.title).toBe(updatedData.title);
    expect(updatedPost.body).toBe(updatedData.body);
  });

  test('DELETE request - delete post', async ({ request }) => {
    const postId = 1;
    const response = await request.delete(`${API_BASE_URL}/posts/${postId}`);
    
    expect(response.status()).toBe(200);
  });

  // Data-driven test example
  const testCases = [
    { userId: 1, expectedName: 'Leanne Graham' },
    { userId: 2, expectedName: 'Ervin Howell' },
    { userId: 3, expectedName: 'Clementine Bauch' }
  ];
  
  for (const { userId, expectedName } of testCases) {
    test(`Fetch user ${userId} - ${expectedName}`, async ({ request }) => {
      const response = await request.get(`${API_BASE_URL}/users/${userId}`);
      
      expect(response.status()).toBe(200);
      
      const user = await response.json();
      expect(user.id).toBe(userId);
      expect(user.name).toBe(expectedName);
    });
  }
});
```

**Evaluation Criteria:**
- Proper use of Playwright's request API
- Comprehensive test coverage for different HTTP methods
- Proper assertions for status codes and response bodies
- Implementation of data-driven testing
- Error handling

---

## Exercise 4: E-commerce User Flow

**Difficulty Level:** Advanced

**Task:** Create an end-to-end test suite for a complete e-commerce user flow.

**Requirements:**
1. Navigate to a public e-commerce site (e.g., https://www.saucedemo.com/)
2. Log in with valid credentials
3. Browse products and apply filters
4. Add multiple items to the cart
5. Proceed to checkout
6. Fill in shipping information
7. Complete the purchase
8. Verify order confirmation
9. Implement proper test organization with fixtures and hooks

**Example Solution:**

```javascript
// ecommerce.spec.js
const { test, expect } = require('@playwright/test');

// Page objects
class LoginPage {
  constructor(page) {
    this.page = page;
    this.usernameInput = page.locator('#user-name');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('#login-button');
    this.errorMessage = page.locator('.error-message-container');
  }

  async goto() {
    await this.page.goto('https://www.saucedemo.com/');
  }

  async login(username, password) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
}

class ProductsPage {
  constructor(page) {
    this.page = page;
    this.productItems = page.locator('.inventory_item');
    this.sortDropdown = page.locator('.product_sort_container');
    this.addToCartButtons = page.locator('button:has-text("Add to cart")');
    this.cartBadge = page.locator('.shopping_cart_badge');
    this.cartLink = page.locator('.shopping_cart_link');
  }

  async sortProducts(option) {
    await this.sortDropdown.selectOption(option);
  }

  async addProductToCart(index) {
    const buttons = await this.addToCartButtons.all();
    if (index < buttons.length) {
      await buttons[index].click();
    }
  }

  async getCartCount() {
    return this.cartBadge.textContent();
  }

  async goToCart() {
    await this.cartLink.click();
  }
}

class CartPage {
  constructor(page) {
    this.page = page;
    this.cartItems = page.locator('.cart_item');
    this.checkoutButton = page.locator('#checkout');
  }

  async getItemCount() {
    return this.cartItems.count();
  }

  async proceedToCheckout() {
    await this.checkoutButton.click();
  }
}

class CheckoutPage {
  constructor(page) {
    this.page = page;
    this.firstNameInput = page.locator('#first-name');
    this.lastNameInput = page.locator('#last-name');
    this.postalCodeInput = page.locator('#postal-code');
    this.continueButton = page.locator('#continue');
    this.finishButton = page.locator('#finish');
    this.confirmationMessage = page.locator('.complete-header');
  }

  async fillShippingInfo(firstName, lastName, postalCode) {
    await this.firstNameInput.fill(firstName);
    await this.lastNameInput.fill(lastName);
    await this.postalCodeInput.fill(postalCode);
    await this.continueButton.click();
  }

  async completePurchase() {
    await this.finishButton.click();
  }

  async getConfirmationMessage() {
    return this.confirmationMessage.textContent();
  }
}

// Test suite
test.describe('E-commerce user flow', () => {
  let loginPage;
  let productsPage;
  let cartPage;
  let checkoutPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    productsPage = new ProductsPage(page);
    cartPage = new CartPage(page);
    checkoutPage = new CheckoutPage(page);

    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');
    // Verify successful login
    await expect(page).toHaveURL(/inventory.html/);
  });

  test('complete purchase flow', async ({ page }) => {
    // Sort products by price (low to high)
    await productsPage.sortProducts('lohi');
    
    // Add 2 products to cart
    await productsPage.addProductToCart(0);
    await productsPage.addProductToCart(1);
    
    // Verify cart count
    expect(await productsPage.getCartCount()).toBe('2');
    
    // Go to cart
    await productsPage.goToCart();
    
    // Verify items in cart
    expect(await cartPage.getItemCount()).toBe(2);
    
    // Proceed to checkout
    await cartPage.proceedToCheckout();
    
    // Fill shipping info
    await checkoutPage.fillShippingInfo('John', 'Doe', '12345');
    
    // Complete purchase
    await checkoutPage.completePurchase();
    
    // Verify confirmation
    expect(await checkoutPage.getConfirmationMessage()).toContain('THANK YOU');
  });
});
```

**Evaluation Criteria:**
- Implementation of Page Object Model for complex flows
- Test organization and structure
- Handling of multi-step processes
- Verification at each step of the flow
- Code maintainability and reusability

---

## Exercise 5: Advanced - Component Testing

**Difficulty Level:** Advanced

**Task:** Write component tests for a web application using Playwright's component testing capabilities.

**Requirements:**
1. Set up Playwright for component testing (with React, Vue, or Svelte)
2. Write tests for a form component that:
   - Renders correctly with default props
   - Handles user input
   - Validates form fields
   - Submits data correctly
   - Shows error states appropriately
3. Use mocks for any external dependencies
4. Implement accessibility testing for the component

**Example Solution (React):**

```javascript
// First, set up component testing in playwright.config.js
// @ts-check
const { defineConfig, devices } = require('@playwright/experimental-ct-react');

module.exports = defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    trace: 'on-first-retry',
    ctPort: 3100,
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});

// ContactForm.jsx
import React, { useState } from 'react';

export const ContactForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Name is required';
    if (!formData.email) newErrors.email = 'Email is required';
    else if (!/\S+@\S+\.\S+/.test(formData.email)) newErrors.email = 'Email is invalid';
    if (!formData.message) newErrors.message = 'Message is required';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      onSubmit(formData);
      setSubmitted(true);
    }
  };

  if (submitted) {
    return <div className="success-message">Thank you for your message!</div>;
  }

  return (
    <form onSubmit={handleSubmit} aria-label="Contact form">
      <div className="form-group">
        <label htmlFor="name">Name</label>
        <input
          id="name"
          name="name"
          type="text"
          value={formData.name}
          onChange={handleChange}
          aria-invalid={errors.name ? 'true' : 'false'}
        />
        {errors.name && <div className="error" role="alert">{errors.name}</div>}
      </div>
      
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input
          id="email"
          name="email"
          type="email"
          value={formData.email}
          onChange={handleChange}
          aria-invalid={errors.email ? 'true' : 'false'}
        />
        {errors.email && <div className="error" role="alert">{errors.email}</div>}
      </div>
      
      <div className="form-group">
        <label htmlFor="message">Message</label>
        <textarea
          id="message"
          name="message"
          value={formData.message}
          onChange={handleChange}
          aria-invalid={errors.message ? 'true' : 'false'}
        />
        {errors.message && <div className="error" role="alert">{errors.message}</div>}
      </div>
      
      <button type="submit">Send Message</button>
    </form>
  );
};

// ContactForm.spec.jsx
import { test, expect } from '@playwright/experimental-ct-react';
import { ContactForm } from './ContactForm';

test.describe('ContactForm Component', () => {
  test('renders the form correctly', async ({ mount }) => {
    const component = await mount(<ContactForm onSubmit={() => {}} />);
    
    await expect(component).toContainText('Name');
    await expect(component).toContainText('Email');
    await expect(component).toContainText('Message');
    await expect(component.locator('button')).toContainText('Send Message');
  });

  test('validates required fields', async ({ mount }) => {
    const component = await mount(<ContactForm onSubmit={() => {}} />);
    
    // Submit without filling fields
    await component.locator('button').click();
    
    // Check for error messages
    await expect(component.locator('.error')).toContainText('Name is required');
    await expect(component.locator('.error')).toContainText('Email is required');
    await expect(component.locator('.error')).toContainText('Message is required');
  });

  test('validates email format', async ({ mount }) => {
    const component = await mount(<ContactForm onSubmit={() => {}} />);
    
    // Fill with invalid email
    await component.locator('#name').fill('John Doe');
    await component.locator('#email').fill('invalid-email');
    await component.locator('#message').fill('Test message');
    
    await component.locator('button').click();
    
    // Check for email error
    await expect(component.locator('.error')).toContainText('Email is invalid');
  });

  test('submits the form with valid data', async ({ mount }) => {
    // Mock the submit function
    const onSubmitMock = test.fn();
    const component = await mount(<ContactForm onSubmit={onSubmitMock} />);
    
    // Fill form with valid data
    await component.locator('#name').fill('John Doe');
    await component.locator('#email').fill('john@example.com');
    await component.locator('#message').fill('Test message');
    
    // Submit form
    await component.locator('button').click();
    
    // Check if onSubmit was called with correct data
    expect(onSubmitMock).toHaveBeenCalledWith({
      name: 'John Doe',
      email: 'john@example.com',
      message: 'Test message'
    });
    
    // Check success message
    await expect(component.locator('.success-message')).toContainText('Thank you');
  });

  test('has proper accessibility attributes', async ({ mount, page }) => {
    const component = await mount(<ContactForm onSubmit={() => {}} />);
    
    // Check form has proper aria-label
    await expect(component.locator('form')).toHaveAttribute('aria-label', 'Contact form');
    
    // Submit empty form to trigger errors
    await component.locator('button').click();
    
    // Check invalid fields have proper aria-invalid attribute
    await expect(component.locator('#name')).toHaveAttribute('aria-invalid', 'true');
    
    // Check error messages have role="alert"
    await expect(component.locator('.error').first()).toHaveAttribute('role', 'alert');
    
    // Take an accessibility snapshot
    const snapshot = await page.accessibility.snapshot();
    expect(snapshot).toBeTruthy();
    
    // You could add more specific accessibility checks here
  });
});
```

**Evaluation Criteria:**
- Setup of component testing environment
- Test coverage for component functionality
- Proper mocking of dependencies
- Implementation of accessibility testing
- Test organization and structure
- Error handling and validation testing

---

## Assessment Guidelines

When evaluating candidates based on these coding exercises, consider the following criteria:

### Junior Level (0-2 years experience)
- **Basic Implementation:** Should be able to complete Exercise 1 with minimal guidance
- **Code Structure:** May have some organization issues but code should be functional
- **Testing Concepts:** Should demonstrate basic understanding of test assertions and locators
- **Expected Completion:** Exercise 1 fully, parts of Exercise 2

### Mid-Level (2-5 years experience)
- **Implementation Quality:** Should complete Exercises 1-3 with clean, well-structured code
- **Design Patterns:** Should implement Page Object Model effectively
- **Test Organization:** Should use proper test hooks and organization
- **Error Handling:** Should include proper error handling and validation testing
- **Expected Completion:** Exercises 1-3 fully, parts of Exercise 4

### Senior Level (5+ years experience)
- **Advanced Implementation:** Should complete all exercises with optimal solutions
- **Architecture:** Should demonstrate strong test architecture principles
- **Performance:** Should consider test performance and reliability
- **Best Practices:** Should follow all testing best practices
- **Accessibility:** Should implement proper accessibility testing
- **Expected Completion:** All exercises with additional improvements or suggestions

### Evaluation Process

1. **Code Review:**
   - Review the code for clarity, organization, and best practices
   - Check for proper use of Playwright's API
   - Evaluate test structure and organization
   - Look for error handling and edge cases

2. **Execution:**
   - Run the tests to verify they work as expected
   - Check for flakiness or reliability issues
   - Evaluate performance and execution time

3. **Discussion:**
   - Ask the candidate to explain their approach
   - Discuss alternative implementations
   - Explore how they would handle specific challenges
   - Discuss how they would integrate these tests into a CI/CD pipeline

4. **Scoring:**
   - Functionality (40%): Do the tests work correctly?
   - Structure (30%): Is the code well-organized and maintainable?
   - Best Practices (20%): Does the code follow testing best practices?
   - Innovation (10%): Did the candidate bring unique insights or improvements?

