# DiJones Business Solutions - Developer Training

Welcome to your development training journey! 🚀

This repository contains everything you need to learn Python, JavaScript, and HTML with AI assistance.

## 🎯 Your First Task: Fork and Clone This Repository

**Congratulations!** You've found the training materials. Your first exercise is to set up your own copy of this repository. This teaches you Git basics that you'll use throughout the course.

### Step 1: Fork This Repository

1. Click the "Fork" button at the top right of this page
2. This creates your personal copy under your GitHub account
3. You'll make all your changes in your fork (not this original repo)

**Why fork?** This gives you your own workspace where you can:
- Complete exercises
- Save your progress
- Push code without affecting others
- Keep everything organized

### Step 2: Clone Your Fork to Your Computer

Open your terminal/command prompt and run:

```bash
# Replace YOUR-USERNAME with your actual GitHub username
git clone https://github.com/YOUR-USERNAME/dijones-training-repo.git

# Navigate into the folder
cd dijones-training-repo

# Open in VS Code
code .
```

### Step 3: Verify Setup

Check that everything worked:

```bash
# You should see files listed
ls

# Check Git is working
git status

# Should show you're on the main branch with no changes
```

### Step 4: Create Your First Commit

Let's practice making changes:

1. Open `STUDENT_ROSTER.md` in VS Code
2. Add your name to the list
3. Save the file
4. Commit and push:

```bash
git add STUDENT_ROSTER.md
git commit -m "Add my name to roster"
git push origin main
```

5. Go to your GitHub fork - you should see your commit!

**🎉 Success!** You just completed your first Git workflow. This is exactly how you'll save your work throughout the course.

---

## 📚 Course Materials

### Documentation
- **[Course Curriculum](docs/COURSE.md)** - 6-week structured program
- **[Exercise Workbook](docs/EXERCISES.md)** - Hands-on practice
- **[Setup Guide](docs/SETUP.md)** - Initial setup instructions
- **[Team Lead Guide](docs/TEAM_LEAD.md)** - For instructors

### Weekly Exercises
- **[Week 1](exercises/week1/)** - Foundations & AI Tools
- **[Week 2](exercises/week2/)** - HTML & CSS
- **[Week 3](exercises/week3/)** - JavaScript
- **[Week 4](exercises/week4/)** - Python
- **[Week 5-6](exercises/week5-6/)** - Integration Projects

### Starter Templates
- **[starter-templates/](starter-templates/)** - Project templates with Copilot prompts

---

## 🎓 How to Use This Repository

### Your Workflow

1. **Read the module** in the course documentation
2. **Navigate to the exercise folder** for that week
3. **Complete the exercises** in VS Code
4. **Commit your work** regularly
5. **Push to GitHub** so it's saved and visible

### Repository Structure

```
dijones-training-repo/
├── README.md                    # You are here!
├── STUDENT_ROSTER.md            # Sign your name here
├── docs/                        # Course documentation
│   ├── COURSE.md                # Main curriculum
│   ├── EXERCISES.md             # Exercise workbook
│   ├── SETUP.md                 # Setup instructions
│   └── TEAM_LEAD.md             # Instructor guide
├── exercises/                   # Weekly exercises
│   ├── week1/                   # Week 1 exercises
│   │   ├── README.md            # Week 1 overview
│   │   └── exercises/           # Exercise files
│   ├── week2/                   # Week 2 exercises
│   ├── week3/                   # Week 3 exercises
│   ├── week4/                   # Week 4 exercises
│   └── week5-6/                 # Final projects
└── starter-templates/           # Template files
    ├── template.html
    ├── style.css
    ├── script.js
    └── starter.py
```

### Where to Put Your Work

Create folders for your completed exercises:

```
dijones-training-repo/
├── my-work/                     # Create this folder!
│   ├── week1/
│   │   ├── terminal-practice.md
│   │   └── first-commit.txt
│   ├── week2/
│   │   ├── my-profile.html
│   │   └── style.css
│   └── week3/
│       └── ticket-checker.html
```

**Important:** The `my-work/` folder is where YOU put your completed exercises. The `exercises/` folder contains instructions (don't edit those).

---

## 🚀 Getting Started Checklist

Before Week 1, make sure you have:

- [ ] Forked this repository to your GitHub account
- [ ] Cloned your fork to your computer
- [ ] Opened the repository in VS Code
- [ ] Added your name to STUDENT_ROSTER.md
- [ ] Made your first commit and push
- [ ] Can see your commit on GitHub
- [ ] Read the [Setup Guide](docs/SETUP.md)
- [ ] Verified GitHub Copilot is working
- [ ] Joined the team communication channel

**Once complete, you're ready to start [Week 1](exercises/week1/)!**

---

## 📞 Getting Help

### Resources in This Repo
- Check the [Exercise Workbook](docs/EXERCISES.md) for solutions
- Review the [Course Documentation](docs/COURSE.md) for explanations
- Use the starter templates as references

### Team Support
- **Team Channel:** [Insert Slack/Teams link]
- **Office Hours:** [Insert schedule]
- **Coding Buddy:** [Assigned in setup]
- **Mentors:** [See Setup Guide]

### When You're Stuck
1. Read the error message carefully
2. Ask GitHub Copilot Chat (`Ctrl+I` in VS Code)
3. Check the troubleshooting sections in docs
4. Ask your coding buddy
5. Post in the team channel
6. Attend office hours

---

## 🎯 Course Overview

**Duration:** 6 weeks, self-paced  
**Time Commitment:** 60-90 minutes daily  
**Tools:** VS Code, GitHub Copilot, Python, Git  
**Prerequisites:** None - beginners welcome!

### What You'll Learn

- **Week 1:** Development foundations, GitHub Copilot, Git/GitHub
- **Week 2:** HTML & CSS for building web interfaces  
- **Week 3:** JavaScript for interactivity
- **Week 4:** Python for automation and data processing
- **Week 5-6:** Integration projects and real applications

### What You'll Build

- Personal profile page
- FAQ page for your team
- Ticket status checker
- Report generator
- Complete helpdesk dashboard

---

## 💻 Using GitHub Copilot

This course is designed around GitHub Copilot as your AI pair programmer.

### Best Practices
- ✅ Write descriptive comments before code
- ✅ Use Copilot Chat to explain concepts
- ✅ Review all suggestions before accepting
- ✅ Test generated code thoroughly
- ✅ Ask "why" questions to learn patterns

### Copilot Chat Commands
- `Ctrl+I` (Windows) or `Cmd+I` (Mac) - Open Copilot Chat
- Right-click code → "Copilot: Explain This"
- Right-click code → "Copilot: Fix This"
- Type `/` in chat for special commands

---

## 🏆 Completion Certificate

Upon completing all exercises and the final project, you'll receive:
- Certificate of completion
- Skills badge for your profile
- Portfolio of projects on GitHub
- New opportunities on the team!

---

## 📜 License

This training material is provided for DiJones Business Solutions team members. Feel free to adapt for your personal learning journey.

---

## 🙏 Acknowledgments

This course was designed specifically for helpdesk professionals transitioning to development roles, with practical examples from IT support scenarios.

**Remember:** Every expert developer started exactly where you are now. The only difference is they didn't give up.

**You've got this! Now let's start coding! 🚀**

---

**Ready?** Go to [Week 1](exercises/week1/) to begin!
