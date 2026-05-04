// 1. Function that checks if a number is even or odd
function isEvenOrOdd(num) {
  if (num % 2 === 0) {
    return "even";
  } else {
    return "odd";
  }
}

// 2. Function that converts temperature from Celsius to Fahrenheit
function celsiusToFahrenheit(celsius) {
  return (celsius * 9/5) + 32;
}

// 3. Function to validate an email address format
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// 4. Array of 5 ticket statuses for a helpdesk system
const ticketStatuses = ["open", "in-progress", "on-hold", "resolved", "closed"];

// 5. Function that takes a ticket ID and formats it as "TKT-00000"
function formatTicketId(id) {
  return "TKT-" + String(id).padStart(5, "0");
}

