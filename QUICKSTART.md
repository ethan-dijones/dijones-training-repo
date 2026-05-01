# Quick Start Guide

**New to coding?** Start here! This guide gets you from zero to your first commit in under 30 minutes.

## ✅ Step-by-Step Setup

### 1. Create GitHub Account (5 minutes)

1. Go to https://github.com
2. Click "Sign up"
3. Choose username (use your real name or professional nickname)
4. Verify email
5. Done!

### 2. Accept Team Invitation (2 minutes)

1. Check your email for GitHub invitation
2. Click the link
3. Accept to join DiJones Business Solutions
4. Confirm you're in the team

### 3. Install Software (15 minutes)

**VS Code:**
1. Go to https://code.visualstudio.com
2. Download for your OS (Windows/Mac/Linux)
3. Install with default settings
4. Open VS Code

**Python:**
1. Go to https://python.org
2. Download latest version (3.10+)
3. **IMPORTANT:** Check "Add Python to PATH" during install
4. Install

**Git:**
1. Go to https://git-scm.com
2. Download for your OS
3. Install with default settings

### 4. Verify Installation (3 minutes)

Open Terminal (Mac) or Command Prompt (Windows):

```bash
# Check Python
python --version
# Should show: Python 3.10.x or higher

# Check Git  
git --version
# Should show: git version 2.x.x
```

If either doesn't work, restart your computer and try again.

### 5. Configure Git (2 minutes)

In terminal:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use your real name and the email associated with GitHub.

### 6. Install VS Code Extensions (3 minutes)

In VS Code:
1. Click Extensions icon (left sidebar) or press `Ctrl+Shift+X`
2. Search and install:
   - "GitHub Copilot"
   - "Python" (by Microsoft)
   - "Live Server" (by Ritwick Dey)

### 7. Fork and Clone Repository (5 minutes)

1. **Fork:**
   - Go to https://github.com/DiJonesBusinessSolutions/dijones-training-repo
   - Click "Fork" button (top right)
   - Wait for it to create your copy

2. **Clone:**
   - On YOUR fork page, click green "Code" button
   - Copy the URL
   - In terminal:
   ```bash
   # Navigate to where you want the folder
   cd Documents  # or wherever you want it
   
   # Clone (paste your URL)
   git clone https://github.com/YOUR-USERNAME/dijones-training-repo.git
   
   # Enter the folder
   cd dijones-training-repo
   
   # Open in VS Code
   code .
   ```

### 8. Make Your First Commit (5 minutes)

1. In VS Code, open `STUDENT_ROSTER.md`
2. Add your name following the format
3. Save (Ctrl+S or Cmd+S)
4. In terminal:
   ```bash
   git add STUDENT_ROSTER.md
   git commit -m "Add my name to roster"
   git push origin main
   ```
5. Go to YOUR GitHub fork - you should see your change!

## 🎉 You're Ready!

You just:
- ✅ Created a GitHub account
- ✅ Installed all tools
- ✅ Forked and cloned a repository
- ✅ Made your first commit
- ✅ Pushed to GitHub

## 📖 What's Next?

1. Read the [full Setup Guide](docs/SETUP.md)
2. Join the team communication channel
3. Meet your coding buddy
4. Start [Week 1 exercises](exercises/week1/)

## 🆘 Troubleshooting

**"Command not found"**
- Restart your computer
- Check software installed correctly
- Try closing and reopening terminal

**"Permission denied"**
- Make sure you cloned YOUR fork (with YOUR username)
- Check you're signed into GitHub in VS Code

**"Can't push"**
- Make sure you committed first: `git status`
- Check you're in the right folder: `pwd`
- Verify remote: `git remote -v` should show YOUR username

**Still stuck?**
- Post in team channel with:
  - What you're trying to do
  - What error you see
  - Screenshot if helpful

## 💡 Terminal Basics

If you're new to the terminal:

```bash
# Where am I?
pwd

# What's in this folder?
ls        # Mac/Linux
dir       # Windows

# Go into a folder
cd folder-name

# Go back up one level
cd ..

# Go to your home folder
cd ~      # Mac/Linux
cd %USERPROFILE%    # Windows
```

## 🎯 First Day Checklist

- [ ] GitHub account created
- [ ] VS Code installed and opened
- [ ] Python installed (verified with `python --version`)
- [ ] Git installed (verified with `git --version`)
- [ ] Git configured with name and email
- [ ] VS Code extensions installed
- [ ] Repository forked and cloned
- [ ] Name added to STUDENT_ROSTER.md
- [ ] First commit made and pushed
- [ ] Can see commit on GitHub

**All checked?** You're ready to start learning! 🚀

---

**Remember:** Everyone was a beginner once. You've got this!

**Questions?** Ask in the team channel - we're here to help!
