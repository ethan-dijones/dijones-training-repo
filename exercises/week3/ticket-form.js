const form = document.getElementById('ticketForm');
const submitBtn = document.getElementById('submitBtn') || document.querySelector('#ticketForm button[type="submit"]');
const clearBtn = document.getElementById('clearBtn');

function getFieldValue(...ids) {
  for (let i = 0; i < ids.length; i += 1) {
    const field = document.getElementById(ids[i]);
    if (field) {
      return field.value.trim();
    }
  }
  return '';
}

// Function to validate form fields and return array of error messages
function validateFormFields(ticketData) {
  const errors = [];

  if (!ticketData.name) {
    errors.push('Name is required.');
  }

  if (!ticketData.email) {
    errors.push('Email is required.');
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(ticketData.email)) {
    errors.push('Email format is invalid.');
  }

  if (!ticketData.issue) {
    errors.push('Issue description is required.');
  }

  return errors;
}

function getErrorContainer() {
  let errorEl = document.getElementById('errorMessage');
  if (!errorEl && form) {
    errorEl = document.createElement('div');
    errorEl.id = 'errorMessage';
    errorEl.style.color = '#b00020';
    errorEl.style.marginTop = '12px';
    form.insertAdjacentElement('afterend', errorEl);
  }
  return errorEl;
}

function showErrors(errors) {
  const errorEl = getErrorContainer();
  if (!errorEl) {
    return;
  }

  if (errors.length === 0) {
    errorEl.textContent = '';
    return;
  }

  errorEl.innerHTML = `<ul>${errors.map((err) => `<li>${err}</li>`).join('')}</ul>`;
}

// Function to display ticket information in a formatted div
function displayTicketInformation(ticketData) {
  const displayArea = document.getElementById('ticketInfo') || document.getElementById('displayArea');

  if (!displayArea) {
    return;
  }

  displayArea.innerHTML = `
    <h3>Ticket Information</h3>
    <p><strong>Name:</strong> ${ticketData.name}</p>
    <p><strong>Email:</strong> ${ticketData.email}</p>
    <p><strong>Issue:</strong> ${ticketData.issue}</p>
    <p><strong>Priority:</strong> ${ticketData.priority || 'Not set'}</p>
  `;

  displayArea.classList.add('active');
  if (displayArea.style.display === 'none') {
    displayArea.style.display = 'block';
  }
}

// Add event listener to submit button that prevents default form submission
if (submitBtn) {
  submitBtn.addEventListener('click', function (event) {
    event.preventDefault();

    const ticketData = {
      name: getFieldValue('name'),
      email: getFieldValue('email'),
      issue: getFieldValue('issue', 'description'),
      priority: getFieldValue('priority'),
    };

    const errors = validateFormFields(ticketData);
    showErrors(errors);

    if (errors.length > 0) {
      return;
    }

    displayTicketInformation(ticketData);
  });
}

function clearForm() {
  if (form) {
    form.reset();
  }

  const displayArea = document.getElementById('ticketInfo') || document.getElementById('displayArea');
  if (displayArea) {
    displayArea.innerHTML = '';
    displayArea.classList.remove('active');
  }

  showErrors([]);
}

if (clearBtn) {
  clearBtn.addEventListener('click', clearForm);
}
