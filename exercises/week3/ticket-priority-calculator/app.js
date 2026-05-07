const form = document.getElementById('priorityForm');
const historyList = document.getElementById('historyList');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
const formErrors = document.getElementById('formErrors');
const resultCard = document.getElementById('resultCard');
const scoreValue = document.getElementById('scoreValue');
const priorityLevel = document.getElementById('priorityLevel');
const recommendedAction = document.getElementById('recommendedAction');

const history = [];
const keywordWeights = {
  outage: 40,
  down: 35,
  breach: 45,
  payment: 25,
  cannot: 20,
  unable: 20,
  data: 18,
  security: 40,
  failed: 15,
  crash: 30,
  error: 12,
  urgent: 35,
};

const urgencyWeights = {
  low: 10,
  medium: 25,
  high: 40,
  critical: 55,
};

function getPriorityDetails(score) {
  if (score >= 85) {
    return {
      level: 'Critical',
      toneClass: 'critical',
      action: 'Escalate immediately to incident response and alert on-call lead.',
    };
  }

  if (score >= 65) {
    return {
      level: 'High',
      toneClass: 'high',
      action: 'Assign within 15 minutes and update stakeholders with ETA.',
    };
  }

  if (score >= 40) {
    return {
      level: 'Medium',
      toneClass: 'medium',
      action: 'Queue for same-day handling and monitor for impact growth.',
    };
  }

  return {
    level: 'Low',
    toneClass: 'low',
    action: 'Schedule in normal support workflow and send acknowledgement.',
  };
}

function calculateKeywordScore(description) {
  const text = description.toLowerCase();
  let score = 0;

  Object.keys(keywordWeights).forEach((keyword) => {
    if (text.includes(keyword)) {
      score += keywordWeights[keyword];
    }
  });

  return Math.min(score, 55);
}

function calculateUserImpactScore(count) {
  if (count >= 100) {
    return 35;
  }

  if (count >= 25) {
    return 25;
  }

  if (count >= 10) {
    return 15;
  }

  return 6;
}

function validateForm(data) {
  const errors = [];

  if (!data.ticketTitle) {
    errors.push('Ticket title is required.');
  }

  if (!data.description) {
    errors.push('Description is required.');
  }

  if (!data.urgency) {
    errors.push('Urgency level is required.');
  }

  if (!Number.isInteger(data.affectedUsers) || data.affectedUsers < 1) {
    errors.push('Affected users count must be at least 1.');
  }

  return errors;
}

function renderErrors(errors) {
  if (errors.length === 0) {
    formErrors.textContent = '';
    return;
  }

  formErrors.textContent = errors.join(' ');
}

function updateResultUI(score, details) {
  scoreValue.textContent = String(score);
  priorityLevel.textContent = `${details.level} Priority`;
  recommendedAction.textContent = details.action;

  resultCard.classList.remove('neutral', 'low', 'medium', 'high', 'critical');
  resultCard.classList.add(details.toneClass);
}

function renderHistory() {
  historyList.innerHTML = '';

  if (history.length === 0) {
    const emptyItem = document.createElement('li');
    emptyItem.textContent = 'No calculations yet.';
    historyList.appendChild(emptyItem);
    return;
  }

  history.forEach((entry) => {
    const item = document.createElement('li');
    item.innerHTML = `
      <p class="history-meta">${entry.timeLabel}</p>
      <p class="history-title">${entry.ticketTitle}</p>
      <p class="history-score">Score ${entry.score} | ${entry.level}</p>
    `;
    historyList.appendChild(item);
  });
}

function addHistoryEntry(entry) {
  history.unshift(entry);
  if (history.length > 5) {
    history.pop();
  }
  renderHistory();
}

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const data = {
    ticketTitle: document.getElementById('ticketTitle').value.trim(),
    description: document.getElementById('description').value.trim(),
    urgency: document.getElementById('urgency').value,
    affectedUsers: Number.parseInt(document.getElementById('affectedUsers').value, 10),
  };

  const errors = validateForm(data);
  renderErrors(errors);

  if (errors.length > 0) {
    return;
  }

  const keywordScore = calculateKeywordScore(data.description);
  const urgencyScore = urgencyWeights[data.urgency] || 0;
  const impactScore = calculateUserImpactScore(data.affectedUsers);
  const totalScore = Math.min(keywordScore + urgencyScore + impactScore, 100);
  const details = getPriorityDetails(totalScore);

  updateResultUI(totalScore, details);
  addHistoryEntry({
    timeLabel: new Date().toLocaleString(),
    ticketTitle: data.ticketTitle,
    score: totalScore,
    level: details.level,
  });
});

clearHistoryBtn.addEventListener('click', () => {
  history.length = 0;
  renderHistory();
});

renderHistory();
