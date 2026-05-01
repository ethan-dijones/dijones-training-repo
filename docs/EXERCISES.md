# Hands-On Exercise Workbook
## Companion to AI-Assisted Development Training Course

This workbook provides structured exercises for each week of the course. Each exercise includes starter files, clear objectives, and hints for using GitHub Copilot effectively.

---

## Week 1 Exercises

### Exercise 1.1: Terminal Navigation Challenge
**Objective:** Get comfortable with command line basics

**Tasks:**
1. Create this folder structure:
```
my-first-project/
├── docs/
│   └── notes.txt
├── src/
│   ├── html/
│   └── css/
└── README.md
```

2. Navigate to each folder using `cd`
3. List contents with `ls` (Mac/Linux) or `dir` (Windows)
4. Create a file in each folder using `touch` or `echo`

**Commands to practice:**
```bash
mkdir my-first-project
cd my-first-project
mkdir docs src
cd src
mkdir html css
cd ..
echo "My First Project" > README.md
```

### Exercise 1.2: Copilot Prompt Practice
**Objective:** Learn to write effective comments that get good Copilot suggestions

**Create a file:** `practice.js`

**Try these prompts:**
```javascript
// 1. Function that converts temperature from Celsius to Fahrenheit
// (Let Copilot complete, then use Chat to explain the formula)

// 2. Function that checks if a ticket ID is valid (must be 5 digits)
// (Accept suggestion, then ask Copilot Chat: "Is there a better way?")

// 3. Array of 5 helpdesk ticket statuses
// (See what Copilot suggests)

// 4. Function that returns a random element from an array
// (After accepting, ask Copilot to add error handling)
```

**Reflection questions:**
- Which comments triggered better suggestions?
- When did you need to be more specific?
- How did you know if the code was correct?

### Exercise 1.3: Your First Git Commit
**Objective:** Practice basic Git workflow

**Tasks:**
1. Initialize a Git repository
2. Create a simple text file about yourself
3. Stage and commit the file
4. Push to GitHub
5. View your commit on GitHub.com

**Steps:**
```bash
git init
# Create file: about-me.txt
git add about-me.txt
git commit -m "Add personal introduction"
git remote add origin YOUR_GITHUB_URL
git push -u origin main
```

---

## Week 2 Exercises

### Exercise 2.1: HTML Structure Practice
**Objective:** Build a page from scratch using Copilot

**Project:** Create `my-skills.html`

**Requirements:**
- Proper HTML5 structure (<!DOCTYPE>, <html>, <head>, <body>)
- Header with your name
- Section listing technical skills
- Section listing soft skills
- Footer with current date

**Copilot approach:**
```html
<!-- Step 1: Let Copilot create the structure -->
<!-- Create a basic HTML5 page structure -->

<!-- Step 2: Add content with Copilot's help -->
<!-- Add a header section with centered h1 containing my name -->

<!-- Step 3: Use Copilot Chat -->
"Explain what the meta charset tag does"
"Why do we need a viewport meta tag?"
```

### Exercise 2.2: CSS Styling Challenge
**Objective:** Transform an unstyled page into a professional-looking page

**Starting HTML** (provided):
```html
<!DOCTYPE html>
<html>
<head>
    <title>Support Team</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>IT Support Team</h1>
    <p>We're here to help!</p>
    <ul>
        <li>Password resets</li>
        <li>Software installation</li>
        <li>Hardware troubleshooting</li>
    </ul>
    <button>Contact Us</button>
</body>
</html>
```

**Your task:** Create `style.css` with:
- Custom color scheme
- Nice typography
- Styled list items
- Button hover effect
- Responsive spacing

**Copilot prompts to try:**
```css
/* Apply a modern blue color scheme to the page */

/* Style the list items with custom bullet points */

/* Create a button hover effect with smooth transition */

/* Add responsive padding and margins */
```

### Exercise 2.3: Build a Team Page
**Objective:** Combine HTML and CSS skills

**Requirements:**
- Team name header with description
- At least 4 team member cards showing:
  - Name
  - Role
  - Email
  - Photo placeholder
- Responsive grid layout
- Professional styling

**Copilot workflow:**
1. Comment: `<!-- Create a grid layout for team member cards -->`
2. Let Copilot suggest structure
3. Ask Copilot Chat: "How can I make this responsive?"
4. Style with CSS using descriptive comments

---

## Week 3 Exercises

### Exercise 3.1: JavaScript Functions
**Objective:** Write functions that solve real problems

**Create:** `helpdesk-utils.js`

**Functions to build:**
```javascript
// 1. Function that calculates time since ticket was created
// Input: ticket creation date string
// Output: "X hours ago" or "X days ago"

// 2. Function that prioritizes tickets based on keywords
// Input: ticket description string
// Output: "high", "medium", or "low"
// Keywords: "urgent", "critical", "asap" → high priority

// 3. Function that validates email addresses
// Input: email string
// Output: true or false

// 4. Function that formats ticket ID for display
// Input: number like 12345
// Output: string like "TKT-12345"
```

**Testing approach:**
```javascript
// Test each function with console.log
console.log(calculateTimeSince("2024-05-01")); // Should show time difference
console.log(prioritizeTicket("URGENT: Server down")); // Should return "high"
```

### Exercise 3.2: Interactive Elements
**Objective:** Make a webpage respond to user actions

**Project:** Create `ticket-form.html` and `ticket-form.js`

**Requirements:**
- Form with fields: Name, Email, Issue Description
- Submit button
- Display area showing submitted data
- Clear button to reset form

**JavaScript tasks:**
```javascript
// 1. Get form values when submit button is clicked

// 2. Validate that all fields are filled out

// 3. Display formatted ticket information

// 4. Clear all fields when clear button is clicked

// 5. Show error message if validation fails
```

**Copilot prompts:**
```javascript
// Add event listener to submit button that prevents default form submission

// Function to validate form fields and return array of error messages

// Function to display ticket information in a formatted div
```

### Exercise 3.3: Build a Mini App
**Objective:** Create a complete interactive application

**Project:** Ticket Priority Calculator

**Features:**
1. User inputs ticket details
2. App calculates priority based on:
   - Keywords in description
   - User-selected urgency level
   - Affected users count
3. Displays priority score and recommended action
4. Shows color-coded result

**Bonus:** Add a "History" section showing last 5 calculations

---

## Week 4 Exercises

### Exercise 4.1: Python Basics
**Objective:** Get comfortable with Python syntax

**Create:** `ticket_processor.py`

**Tasks:**
```python
# 1. Create a list of 10 ticket IDs

# 2. Create a dictionary representing a ticket with:
#    - id, status, priority, description, created_date

# 3. Function to print ticket information in readable format

# 4. Function to filter tickets by status

# 5. Function to count tickets by priority level
```

**Use Copilot to:**
- Generate realistic sample data
- Explain list comprehensions
- Suggest improvements

### Exercise 4.2: File Operations
**Objective:** Read and write data files

**Project:** Log File Analyzer

**Create:** `log_analyzer.py`

**Sample log file** (create `sample.log`):
```
2024-05-01 09:15:23 INFO User login successful
2024-05-01 09:16:45 ERROR Database connection failed
2024-05-01 09:17:12 WARNING Low disk space
2024-05-01 09:18:30 INFO File uploaded
2024-05-01 09:19:05 ERROR Authentication failed
```

**Your script should:**
1. Read the log file
2. Count each log level (INFO, ERROR, WARNING)
3. Extract all ERROR messages
4. Save summary to `log_summary.txt`

**Copilot prompts:**
```python
# Function to read log file and return list of lines

# Function to count occurrences of each log level

# Function to extract all lines containing ERROR

# Function to write summary report to file
```

### Exercise 4.3: CSV Data Processing
**Objective:** Work with structured data

**Project:** Ticket Statistics Generator

**Sample CSV** (create `tickets.csv`):
```csv
ticket_id,status,priority,assigned_to,created_date
1001,open,high,John,2024-04-15
1002,closed,low,Sarah,2024-04-16
1003,open,medium,John,2024-04-17
1004,closed,high,Mike,2024-04-18
1005,open,low,Sarah,2024-04-19
```

**Your script should:**
1. Load CSV data
2. Calculate:
   - Total tickets
   - Open vs closed count
   - Tickets per person
   - Average by priority
3. Generate formatted report
4. Save as HTML table

**Bonus:** Create a chart using text characters

---

## Week 5 Exercises

### Exercise 5.1: API Practice
**Objective:** Fetch and use external data

**Project:** Weather-Aware Helpdesk

**API:** JSONPlaceholder (https://jsonplaceholder.typicode.com/)

**Tasks:**
```python
# 1. Fetch user data from API

# 2. Display user information formatted

# 3. Handle network errors gracefully

# 4. Save API response to JSON file

# 5. Load saved data and display
```

**Use Copilot to:**
- Import requests library
- Parse JSON responses
- Add error handling
- Format output

### Exercise 5.2: Integration Project
**Objective:** Connect Python backend with HTML frontend

**Project:** Dynamic FAQ System

**Components:**
1. **Python** (`generate_faqs.py`):
   - Read FAQ data from JSON
   - Generate HTML file with FAQs
   - Include styling

2. **HTML/CSS Template**:
   - Professional layout
   - Collapsible sections
   - Search functionality

3. **JavaScript** (`faq.js`):
   - Search/filter FAQs
   - Expand/collapse answers
   - Highlight matches

**Workflow:**
1. Run Python script to generate HTML
2. Open HTML in browser
3. JavaScript makes it interactive

### Exercise 5.3: Complete Dashboard
**Objective:** Build a real-world application

**Project:** Helpdesk Dashboard

**Features:**
- Display ticket statistics (cards)
- Show recent tickets (table)
- Filter by status
- Search by ID or description
- Responsive design

**Files needed:**
- `generate_data.py` - Creates mock ticket data
- `dashboard.html` - Main page structure
- `dashboard.css` - Styling
- `dashboard.js` - Interactivity
- `tickets.json` - Data file

**Success criteria:**
- All features work without errors
- Professional appearance
- Code is well-commented
- Responsive on mobile
- Uses Git for version control

---

## Debugging Challenges

Practice fixing broken code:

### Challenge 1: JavaScript Bug Hunt
```javascript
// This code has 5 bugs. Find and fix them with Copilot's help.

function calculatTicketAge(createDate) {
    const now = new Date()
    const created = new Date(createDate)
    const diffTime = now - created
    const diffDays = diffTime / (1000 * 60 * 60 * 24)
    return diffDays + " days old"
}

// Test it:
console.log(calculatTicketAge("2024-04-01))
```

**Bugs:** Typo in function name, missing semicolons, missing quote, no Math.floor for days

### Challenge 2: Python Logic Error
```python
# This function should return True if ticket is overdue (>3 days old)
# But it's not working correctly. Use Copilot Chat to debug.

def is_overdue(ticket_date):
    from datetime import datetime
    today = datetime.now()
    ticket = datetime.strptime(ticket_date, "%Y-%m-%d")
    days_old = (today - ticket).days
    return days_old > 3

# Test cases:
print(is_overdue("2024-04-25"))  # Should be True (if run in May)
print(is_overdue("2024-05-01"))  # Should be False
```

**Ask Copilot Chat:** "Why might this function give incorrect results?"

---

## Progress Tracking

Use this checklist to track your completion:

### Week 1:
- [ ] Completed terminal navigation challenge
- [ ] Practiced 10+ Copilot prompts
- [ ] Made first Git commit
- [ ] Comfortable with VS Code shortcuts

### Week 2:
- [ ] Built HTML page from scratch
- [ ] Applied CSS styling confidently
- [ ] Created team page project
- [ ] Used Copilot for HTML/CSS

### Week 3:
- [ ] Wrote 5+ JavaScript functions
- [ ] Created interactive form
- [ ] Built ticket calculator app
- [ ] Debugged JavaScript with Copilot

### Week 4:
- [ ] Wrote Python scripts successfully
- [ ] Processed log files
- [ ] Worked with CSV data
- [ ] Generated HTML from Python

### Week 5:
- [ ] Made API requests
- [ ] Built integration project
- [ ] Created complete dashboard
- [ ] All components working together

---

## Tips for Success

**When stuck:**
1. Read error message completely
2. Ask Copilot Chat: "Explain this error"
3. Simplify the problem
4. Search for examples
5. Ask a teammate
6. Take a break

**Copilot Chat questions to ask frequently:**
- "Explain this code line by line"
- "What are potential bugs in this code?"
- "How can I improve this function?"
- "Why isn't this working as expected?"
- "What's a better way to do this?"

**Remember:** The goal isn't perfect code - it's understanding how code works and building problem-solving skills. Copilot is your learning assistant, not a replacement for learning.

---

**Keep this workbook handy and refer to it often. Good luck!** 🚀
