/**
 * Starter JavaScript File
 * 
 * Use GitHub Copilot to help write JavaScript!
 * 
 * Tips:
 * - Write comments describing what you want the function to do
 * - Let Copilot suggest the implementation
 * - Use Copilot Chat to understand concepts
 * - Test your code with console.log()
 */

// Wait for page to load before running JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded! Ready to start coding.');
    
    // Your code here
    init();
});

/**
 * Initialize the application
 * This function runs when the page loads
 */
function init() {
    // Try this Copilot prompt:
    // Add event listeners to all buttons on the page
    
}

/* 
 * Example Copilot prompts to try:
 * 
 * 1. Function to validate an email address format
 * 
 * 2. Function to format a date as "Month Day, Year"
 * 
 * 3. Function to toggle visibility of an element by ID
 * 
 * 4. Function to fetch data from an API endpoint
 * 
 * 5. Function to filter an array based on search text
 */

// Example: DOM manipulation
// Uncomment and modify these examples:

/*
function handleButtonClick() {
    // What should happen when button is clicked?
}

function updateDisplay(data) {
    // How should we show the data on the page?
}

function validateForm(formData) {
    // Check if form data is valid
    // Return array of error messages
}
*/

// Utility functions you might need

/**
 * Get element by ID
 * @param {string} id - Element ID
 * @returns {HTMLElement} The element
 */
function getElement(id) {
    return document.getElementById(id);
}

/**
 * Get all elements matching a selector
 * @param {string} selector - CSS selector
 * @returns {NodeList} List of elements
 */
function getElements(selector) {
    return document.querySelectorAll(selector);
}

// Debugging tips:
// - Use console.log() to check values
// - Use console.error() for errors
// - Check browser DevTools console (F12)
// - Ask Copilot Chat: "Why isn't this working?"
