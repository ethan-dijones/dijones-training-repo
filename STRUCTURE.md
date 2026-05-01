# Repository Structure Guide

This document explains what every file and folder in this repository is for.

## 📁 Root Level Files

```
dijones-training-repo/
├── README.md                 ⭐ START HERE - Main landing page
├── QUICKSTART.md             🚀 For absolute beginners (30-min setup)
├── STUDENT_ROSTER.md         📝 First exercise: Add your name!
├── CONTRIBUTING.md           📖 How to use Git properly
├── LICENSE                   ⚖️  MIT License (free to use)
├── .gitignore               🚫 Files Git should ignore
└── REPOSITORY_SETUP.sh      🛠️  Setup script (for team lead)
```

### Which File Should I Read First?

**If you're a student:**
1. `QUICKSTART.md` - Get set up in 30 minutes
2. `README.md` - Understand the program
3. `STUDENT_ROSTER.md` - Add your name (first exercise!)
4. `docs/SETUP.md` - Detailed setup guide
5. `exercises/week1/` - Start learning!

**If you're the team lead:**
1. `docs/TEAM_LEAD.md` - Your implementation guide
2. `REPOSITORY_SETUP.sh` - How to set up this repo on GitHub
3. `README.md` - What students will see
4. `docs/COURSE.md` - Full curriculum

## 📚 Documentation Folder

```
docs/
├── COURSE.md              📖 Complete 6-week curriculum
├── EXERCISES.md           ✏️  Exercise workbook with solutions
├── SETUP.md               ⚙️  Detailed setup instructions
└── TEAM_LEAD.md           👨‍🏫 Implementation guide for instructors
```

**What's in each:**

- **COURSE.md** - The main curriculum with weekly modules, learning objectives, examples, and resources
- **EXERCISES.md** - Hands-on exercises with step-by-step instructions
- **SETUP.md** - Setup guide customized for DiJones Business Solutions
- **TEAM_LEAD.md** - How to run the program, communication templates, tracking progress

## 🎯 Exercises Folder

```
exercises/
├── week1/
│   └── README.md          Week 1: Foundations & Git
├── week2/
│   └── README.md          Week 2: HTML & CSS
├── week3/
│   └── README.md          Week 3: JavaScript
├── week4/
│   └── README.md          Week 4: Python
└── week5-6/
    └── README.md          Week 5-6: Integration & Final Project
```

**How to use:**
1. Read the weekly README
2. Follow the daily exercises
3. Create your work files IN these folders
4. Commit and push regularly

**Your work should look like:**
```
exercises/
├── week1/
│   ├── README.md              (provided - don't edit)
│   ├── terminal-practice.md   (you create)
│   ├── copilot-test.js        (you create)
│   └── my-profile.html        (you create)
```

## 🎨 Starter Templates

```
starter-templates/
├── template.html          Basic HTML structure with Copilot prompts
├── style.css              CSS template with common patterns
├── script.js              JavaScript template with utilities
└── starter.py             Python template with examples
```

**How to use:**
1. Copy templates to your exercise folder
2. Rename for your project
3. Use comments to trigger Copilot
4. Customize for your needs

**Example:**
```bash
# Copy template for Week 2 project
cp starter-templates/template.html exercises/week2/my-page.html
cp starter-templates/style.css exercises/week2/my-style.css
```

## 🗂️ Typical Student's Repository

After a few weeks, your fork should look like:

```
your-fork/
├── README.md                   (original, unmodified)
├── STUDENT_ROSTER.md           (has your name!)
├── exercises/
│   ├── week1/
│   │   ├── README.md           (original)
│   │   ├── terminal-practice.md     ← Your work
│   │   ├── copilot-test.js          ← Your work
│   │   ├── copilot-learnings.md     ← Your work
│   │   └── my-profile.html          ← Your work
│   ├── week2/
│   │   ├── README.md           (original)
│   │   ├── first-page.html          ← Your work
│   │   ├── styled-page.html         ← Your work
│   │   ├── styles.css               ← Your work
│   │   └── faq-project/             ← Your project
│   │       ├── index.html
│   │       └── style.css
│   └── week3/
│       └── ...
```

## 📊 What Changes, What Doesn't

### ✏️ You WILL Edit/Create:
- `STUDENT_ROSTER.md` - Add your name
- Everything in `exercises/weekX/` folders - Your work
- Files copied from `starter-templates/` - Your projects

### 🚫 You SHOULD NOT Edit:
- Main `README.md` - Course landing page
- `QUICKSTART.md` - Setup guide
- `CONTRIBUTING.md` - Git guidelines
- Files in `docs/` - Course documentation
- Weekly `README.md` files in exercises folders

### ❓ Why Not Edit Course Materials?
- They're reference materials
- Updates come from main repository
- Your changes would conflict with updates
- Your work goes in exercise files, not docs

## 🔄 Repository Workflow

### Daily Work:
```bash
1. cd dijones-training-repo
2. Read exercises/weekX/README.md
3. Create your work files
4. git add your-files
5. git commit -m "Descriptive message"
6. git push origin main
```

### Weekly:
```bash
1. Complete all daily exercises
2. Build weekly project
3. Commit and push everything
4. Share with team in show & tell
```

### If Main Repo Updates:
```bash
git fetch upstream
git merge upstream/main
git push origin main
```

## 🎯 File Naming Conventions

**Good names:**
- `terminal-practice.md` - Descriptive, lowercase, hyphens
- `ticket-checker.html` - Clear purpose
- `week2-styles.css` - Shows which week

**Bad names:**
- `file1.html` - Not descriptive
- `My New Project.html` - Spaces cause problems
- `test.js` - Too generic
- `asdf.py` - Meaningless

## 📈 Tracking Your Progress

Your Git history shows your learning journey:

```bash
# See all your commits
git log --oneline

# See what changed in each commit
git show COMMIT_HASH

# See your progress on GitHub
# Go to your fork → Insights → Commits
```

## 🆘 Getting Help

**File-related questions:**

- "Where should I put my work?" → `exercises/weekX/` folders
- "Can I edit COURSE.md?" → No, that's reference material
- "Where are the templates?" → `starter-templates/` folder
- "How do I update my fork?" → See CONTRIBUTING.md

**Course questions:**

- Check weekly README first
- Review docs/COURSE.md
- Ask in team channel
- Attend office hours

## 🎓 After Course Completion

Your repository becomes your portfolio:

- Shows what you built
- Demonstrates Git skills
- Proves you completed course
- Reference for future projects

Keep it public (or share link) to show employers!

## 📞 Questions?

- **About structure:** See CONTRIBUTING.md
- **About setup:** See QUICKSTART.md or docs/SETUP.md
- **About course:** See docs/COURSE.md
- **About exercises:** See weekly README files
- **Still confused:** Ask in team channel!

---

**Remember:** This structure is designed to help you learn. Don't stress about organization - just follow the weekly READMEs and put your work in the right folders.

**You've got this! 🚀**
