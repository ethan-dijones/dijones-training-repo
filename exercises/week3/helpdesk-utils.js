// 1. Function that calculates time since ticket was created
// Input: ticket creation date string
// Output: "X hours ago" or "X days ago"

// Week 3 data type examples
const ticketTitle = 'Printer is offline'; // string
const ticketIdNumber = 12345; // number
const isVipCustomer = true; // boolean
const ticketDetails = { issueType: 'hardware', assignedTeam: 'support' }; // object
const ticketStatuses = ['new', 'in progress', 'waiting on customer', 'resolved']; // array
const noAssignedAgent = null; // null

function getTimeSinceCreated(createdDateString) {
  const createdDate = new Date(createdDateString);
  const now = new Date();
  const diffMs = now - createdDate;
  const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

  if (diffDays > 0) {
    return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
  } else {
    return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  }
}

// 2. Function that prioritizes tickets based on keywords
// Input: ticket description string
// Output: "high", "medium", or "low"
// Keywords: "urgent", "critical", "asap" → high priority
function prioritizeTicket(description) {
  const lowerDescription = description.toLowerCase();
  const highPriorityKeywords = ['urgent', 'critical', 'asap'];
  
  if (highPriorityKeywords.some(keyword => lowerDescription.includes(keyword))) {
    return 'high';
  }
  
  return 'medium';
}

// 3. Function that validates email addresses
// Input: email string
// Output: true or false
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// 4. Function that formats ticket ID for display
// Input: number like 12345
// Output: string like "TKT-12345"
function formatTicketId(ticketId) {
  return `TKT-${ticketId}`;
}

// 5. Function that calculates ticket priority with if/else urgency rules
// Inputs: issue type and customer tier
// Output: "high", "medium", or "low"
function calculateTicketPriority(issueType, customerTier) {
  const normalizedIssueType = issueType.toLowerCase();
  const normalizedCustomerTier = customerTier.toLowerCase();

  if (normalizedIssueType === 'outage' || normalizedIssueType === 'security') {
    return 'high';
  } else if (normalizedIssueType === 'billing' && normalizedCustomerTier === 'vip') {
    return 'high';
  } else if (normalizedIssueType === 'billing' || normalizedIssueType === 'performance') {
    return 'medium';
  } else {
    return 'low';
  }
}

// 6. Loop through array of ticket statuses and return display lines
function listTicketStatuses(statuses) {
  const lines = [];

  for (let i = 0; i < statuses.length; i += 1) {
    lines.push(`Step ${i + 1}: ${statuses[i]}`);
  }

  return lines;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    ticketTitle,
    ticketIdNumber,
    isVipCustomer,
    ticketDetails,
    ticketStatuses,
    noAssignedAgent,
    getTimeSinceCreated,
    prioritizeTicket,
    validateEmail,
    formatTicketId,
    calculateTicketPriority,
    listTicketStatuses,
  };
}

if (typeof window !== 'undefined') {
  window.helpdeskUtils = {
    ticketTitle,
    ticketIdNumber,
    isVipCustomer,
    ticketDetails,
    ticketStatuses,
    noAssignedAgent,
    getTimeSinceCreated,
    prioritizeTicket,
    validateEmail,
    formatTicketId,
    calculateTicketPriority,
    listTicketStatuses,
  };
}

