# DiJones Business Solutions Team - Setup Guide
## AI-Assisted Development Training

Welcome to the DiJones Business Solutions development training program! This guide will get you set up and ready to start learning.

## 🏢 Your GitHub Team

**Organization:** DiJones Business Solutions  
**Team:** Business Solutions  
**Team Link:** https://github.com/orgs/DiJonesBusinessSolutions/teams/business-solutions

## 📋 Pre-Course Checklist

Complete these steps **before Day 1** of the course:

### Step 1: GitHub Account Setup
- [ ] Create GitHub account at https://github.com (if you don't have one)
- [ ] Accept the invitation to join DiJonesBusinessSolutions organization
- [ ] Verify you can access the Business Solutions team page
- [ ] Add a profile photo and bio to your GitHub profile

**To accept invitation:**
1. Check your email for GitHub invitation
2. Click the invitation link
3. Accept to join the organization
4. Navigate to the team page to confirm access

### Step 2: Install Required Software

#### VS Code (Required)
- [ ] Download from https://code.visualstudio.com
- [ ] Install VS Code
- [ ] Open VS Code and complete welcome tutorial

#### Python (Required)
- [ ] Download from https://python.org (get version 3.10 or newer)
- [ ] During installation, CHECK "Add Python to PATH"
- [ ] Verify installation: Open terminal and type `python --version`

#### Git (Required)
- [ ] Download from https://git-scm.com
- [ ] Install with default settings
- [ ] Verify installation: Open terminal and type `git --version`

### Step 3: Configure Git

Open terminal/command prompt and run:

```bash
# Set your name (use your real name)
git config --global user.name "Your Name"

# Set your email (use your GitHub email)
git config --global user.email "your.email@company.com"

# Verify settings
git config --global --list
```

### Step 4: VS Code Extensions

Install these extensions in VS Code:

**Required:**
- [ ] **GitHub Copilot** (should be provided by your organization)
- [ ] **Python** (by Microsoft)
- [ ] **Live Server** (by Ritwick Dey) - for testing HTML

**Recommended:**
- [ ] **GitLens** - enhanced Git features
- [ ] **Prettier** - code formatter
- [ ] **Error Lens** - better error visibility

**To install extensions:**
1. Open VS Code
2. Click Extensions icon (left sidebar) or press `Ctrl+Shift+X`
3. Search for extension name
4. Click Install

### Step 5: Verify GitHub Copilot

- [ ] Open VS Code
- [ ] Look for Copilot icon in bottom right status bar
- [ ] If not visible, check Extensions and ensure Copilot is installed
- [ ] Sign in with your GitHub account when prompted
- [ ] Create a new JavaScript file and type: `// function to add two numbers`
- [ ] Press Enter and watch Copilot suggest code (if it works, you're ready!)

**Troubleshooting Copilot:**
- Ensure you're signed into GitHub in VS Code (bottom left account icon)
- Check your organization has granted you Copilot access
- Restart VS Code after installing Copilot
- Contact team lead if Copilot still doesn't work

### Step 6: Clone Course Materials

1. **Create a workspace folder:**
   ```bash
   # Windows
   mkdir C:\Dev\dijones-training
   cd C:\Dev\dijones-training

   # Mac/Linux
   mkdir ~/Dev/dijones-training
   cd ~/Dev/dijones-training
   ```

2. **Clone the course repository:**
   ```bash
   # Your team lead will provide the repository URL
   git clone [REPOSITORY_URL]
   ```

3. **Open in VS Code:**
   ```bash
   code .
   ```

## 🎯 Your First Week Goals

### Day 1: Orientation
- [ ] Complete all setup steps above
- [ ] Join team communication channel (Slack/Teams)
- [ ] Introduce yourself to the team
- [ ] Meet your coding buddy
- [ ] Read Week 1 of the main course document

### Day 2-3: Development Environment
- [ ] Complete Terminal Navigation Challenge (Exercise Workbook)
- [ ] Practice basic terminal commands
- [ ] Create your first file in VS Code
- [ ] Get comfortable with VS Code shortcuts

### Day 4-5: GitHub Copilot & Git
- [ ] Complete Copilot practice exercises
- [ ] Create your first repository
- [ ] Make your first commit
- [ ] Push code to GitHub
- [ ] View your work on GitHub.com

## 👥 Team Structure

### Coding Buddies
You'll be paired with a buddy to:
- Work through exercises together
- Help each other when stuck
- Review each other's code
- Celebrate wins together

**Your buddy:** [To be assigned]

### Mentors
Experienced team members available for help:
- [Mentor name and contact]
- [Mentor name and contact]

### Communication Channels
- **Team Channel:** [Slack/Teams link]
- **Office Hours:** [Schedule]
- **Weekly Show & Tell:** [Day/Time]

## 📚 Course Structure Overview

### Week 1: Foundations
**What you'll learn:** Terminal basics, Copilot mastery, Git
**Project:** None yet - focus on tools
**Time:** 60-90 min/day

### Week 2: HTML & CSS
**What you'll learn:** Build web pages, styling
**Project:** Create a team FAQ page
**Time:** 60-90 min/day + 2-3 hours project

### Week 3: JavaScript
**What you'll learn:** Make pages interactive
**Project:** Ticket status checker
**Time:** 60-90 min/day + 2-3 hours project

### Week 4: Python
**What you'll learn:** Automation, data processing
**Project:** Report generator
**Time:** 60-90 min/day + 2-3 hours project

### Week 5-6: Integration
**What you'll learn:** Build complete applications
**Project:** Helpdesk dashboard
**Time:** 90 min/day + 1 week final project

## 🗓️ Recommended Schedule

### Daily Routine (Choose your time!)

**Option 1: Morning Learner (Start of day)**
- 8:00-8:15 AM: Review yesterday's concepts
- 8:15-9:00 AM: New module exercises
- 9:00-9:20 AM: Free practice with Copilot
- 9:20-9:30 AM: Document learnings

**Option 2: Lunch Learner (Midday)**
- 12:00-12:15 PM: Review yesterday's concepts
- 12:15-1:00 PM: New module exercises
- 1:00-1:20 PM: Free practice with Copilot
- 1:20-1:30 PM: Document learnings

**Option 3: Afternoon Learner (End of day)**
- 3:30-3:45 PM: Review yesterday's concepts
- 3:45-4:30 PM: New module exercises
- 4:30-4:50 PM: Free practice with Copilot
- 4:50-5:00 PM: Document learnings

### Weekly Schedule

**Monday-Friday:** Daily exercises (60-90 min)  
**Saturday OR Sunday:** Weekly project (2-3 hours)  
**Weekly Team Meeting:** Show & tell and Q&A

## 📁 Repository Structure

Your team's training repositories will be organized like this:

```
DiJonesBusinessSolutions/
├── training-materials/          # Course content (read-only)
│   ├── course/
│   ├── exercises/
│   └── starter-projects/
│
├── yourname-practice/           # Your personal practice repo
│   ├── week1/
│   ├── week2/
│   ├── week3/
│   └── final-project/
│
└── team-projects/               # Shared team projects
    ├── faq-page/
    ├── dashboard/
    └── knowledge-base/
```

## 🔐 Repository Best Practices

### Creating Your Practice Repository

1. **Go to your GitHub organization:**
   https://github.com/DiJonesBusinessSolutions

2. **Create new repository:**
   - Click "New repository"
   - Name: `yourname-dev-training` (e.g., `john-smith-dev-training`)
   - Description: "My development training practice projects"
   - Visibility: **Private** (unless team lead specifies otherwise)
   - Check "Add a README file"
   - Click "Create repository"

3. **Add to Business Solutions team:**
   - Settings → Manage access
   - Add team: Business Solutions (Read access)
   - This lets mentors see your work and help

### Repository Naming Convention
- Personal practice: `firstname-lastname-dev-training`
- Team projects: `team-project-name`
- Use lowercase and hyphens (not underscores or spaces)

### Commit Message Guidelines
Write clear commit messages:
- ✅ "Add ticket validation function"
- ✅ "Fix bug in date calculation"
- ✅ "Complete Week 2 CSS exercise"
- ❌ "updates"
- ❌ "fix"
- ❌ "asdfasdf"

### What NOT to Commit
Never commit to Git:
- ❌ Passwords or API keys
- ❌ Personal information
- ❌ Large files (>100MB)
- ❌ node_modules/ or venv/ folders
- ❌ .env files with secrets

## 🆘 Getting Help

### When You're Stuck

**Try this order:**

1. **Read the error message completely** (most errors tell you what's wrong!)

2. **Ask GitHub Copilot Chat:**
   - Press `Ctrl+I` in VS Code
   - Paste error and ask: "What does this error mean and how do I fix it?"

3. **Check the course materials:**
   - Exercise workbook has common solutions
   - Course document has troubleshooting section

4. **Ask your coding buddy:**
   - Share your screen
   - Explain what you're trying to do
   - Two heads are better than one!

5. **Search online:**
   - Google the exact error message
   - Check Stack Overflow
   - MDN Web Docs for web questions

6. **Post in team channel:**
   - Describe what you're trying to do
   - Share the error message
   - Show relevant code
   - Someone will help!

7. **Contact a mentor:**
   - Schedule office hours
   - Prepare specific questions

### Office Hours
**When:** [Day/Time]  
**Where:** [Meeting link]  
**Format:** Drop-in, ask anything

## ✅ Pre-Flight Checklist

Before starting Day 1, verify you can:

### Software & Accounts
- [ ] Open VS Code successfully
- [ ] Run `python --version` in terminal (shows 3.10+)
- [ ] Run `git --version` in terminal (shows version)
- [ ] Access your GitHub organization
- [ ] See GitHub Copilot icon in VS Code

### GitHub Setup
- [ ] Can view Business Solutions team page
- [ ] Created personal practice repository
- [ ] Cloned repository to your computer
- [ ] Made test commit and pushed to GitHub
- [ ] Can view commit on GitHub.com

### Copilot Working
- [ ] Created new .js file
- [ ] Typed comment: `// function to add two numbers`
- [ ] Copilot suggested code
- [ ] Can open Copilot Chat with `Ctrl+I`

### Team Connection
- [ ] Joined team communication channel
- [ ] Know your coding buddy
- [ ] Know who mentors are
- [ ] Added training time to your calendar

## 🎉 You're Ready!

If you've completed all the steps above, you're ready to start the course!

### Your First Assignment

1. Open the main course document: `ai_dev_training_course.md`
2. Read the introduction and Week 1 overview
3. Start Module 1.1: Introduction to Development Concepts
4. Post in the team channel: "Starting Week 1! 🚀"

### Team Contact Info

**Team Lead:** [Name]  
**Email:** [Email]  
**Team Channel:** [Link]  

**Mentors:**
- [Name] - [Contact]
- [Name] - [Contact]

### Important Links

- Team GitHub: https://github.com/orgs/DiJonesBusinessSolutions/teams/business-solutions
- Course Materials: [Repository URL]
- Team Channel: [Slack/Teams link]
- Office Hours: [Meeting link]
- Progress Tracker: [Spreadsheet/tool link]

## 💪 Motivational Note

You're about to learn skills that will:
- Make you more valuable to the team
- Open new career opportunities
- Let you build tools to solve real problems
- Connect you with the wider tech community

**Remember:** Every expert was once a beginner. The only difference is they didn't give up.

Your helpdesk experience gives you unique insight into user problems. Combined with development skills, you'll be able to build solutions that directly address issues you've seen firsthand.

**The team is behind you. Your buddy is with you. Copilot is your AI assistant. You've got this!**

Now let's get started! 🚀

---

## 📞 Questions?

If you have any questions about setup or the course:

1. Check the troubleshooting sections above
2. Ask in the team channel
3. Contact your team lead
4. Attend office hours

**Welcome to the Business Solutions development team!**

---

*Setup Guide v1.0 - DiJones Business Solutions*  
*Last Updated: [Date]*
