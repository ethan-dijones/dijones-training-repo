# Contributing to Your Learning Journey

This guide helps you understand how to work with this repository as you learn.

## 🔄 Your Workflow

### Daily Work Cycle

1. **Start your day**
   ```bash
   cd dijones-training-repo
   git status  # Check what's changed
   ```

2. **Do your exercises**
   - Work in the `exercises/weekX/` folders
   - Save your work frequently (Ctrl+S)

3. **Commit your work**
   ```bash
   git add exercises/week1/my-file.html
   git commit -m "Complete exercise 1.2"
   git push origin main
   ```

4. **Repeat** - Make commits often!

## 📝 Commit Message Guidelines

### Good Commit Messages
- ✅ "Complete terminal navigation practice"
- ✅ "Add FAQ page styling"
- ✅ "Fix bug in ticket checker validation"
- ✅ "Update profile with new skills"

### Bad Commit Messages
- ❌ "update"
- ❌ "asdf"
- ❌ "fixed it"
- ❌ "day 2"

### Format
```
Action + What

Examples:
- "Add CSS styling to FAQ page"
- "Complete Week 1 exercises"
- "Fix typo in README"
- "Refactor JavaScript functions"
```

## 📁 Where to Put Your Work

### DO: Work in exercise folders
```
exercises/
├── week1/
│   ├── terminal-practice.md     ✅ Your work here
│   ├── copilot-test.js          ✅ Your work here
│   └── my-profile.html          ✅ Your work here
```

### DON'T: Edit course materials
```
docs/
├── COURSE.md           ❌ Don't edit (read-only)
├── EXERCISES.md        ❌ Don't edit (read-only)
└── SETUP.md            ❌ Don't edit (read-only)
```

## 🔀 Updating Your Fork

If the main course materials get updated:

```bash
# Add the original repo as upstream (one time only)
git remote add upstream https://github.com/DiJonesBusinessSolutions/dijones-training-repo.git

# Get updates from original repo
git fetch upstream

# Merge updates into your fork
git merge upstream/main

# Push to your fork
git push origin main
```

## ❓ Questions About Course Content?

If you find errors or have suggestions:

1. **First:** Ask in team channel - might be a misunderstanding
2. **Then:** Create an issue on the main repo (not your fork)
3. **Include:**
   - Which document/exercise
   - What seems wrong
   - What you expected

## 🎯 Best Practices

### Commit Often
- After each exercise
- After fixing a bug
- Before trying something risky
- End of each coding session

### Write Clear Messages
- Future you will thank you
- Team can see your progress
- Good practice for real projects

### Keep It Organized
- Use the folder structure
- Name files descriptively
- Add comments to your code
- Keep related files together

### Don't Commit
- Passwords or API keys
- Personal information
- Very large files (>10MB)
- node_modules or venv folders

## 🚫 What Not to Do

### DON'T:
- ❌ Work directly in `main` branch on a team project
- ❌ Commit sensitive information
- ❌ Delete the course materials
- ❌ Force push (`git push -f`) unless you know what you're doing
- ❌ Edit files in `docs/` folder

### DO:
- ✅ Work in your own fork
- ✅ Commit frequently
- ✅ Push to GitHub regularly
- ✅ Ask for help when stuck
- ✅ Review your own code before committing

## 🆘 Fixing Mistakes

### Undo last commit (before push)
```bash
git reset --soft HEAD~1
# Make changes
git add .
git commit -m "Better commit message"
```

### Committed wrong file
```bash
git rm --cached filename
git commit -m "Remove file from tracking"
```

### Messed everything up
Ask for help in team channel! We can fix it together.

## 📊 Viewing Your Progress

On GitHub, you can:
- View all your commits
- See what changed in each commit
- Browse your files online
- Share specific commits with mentors

## 🎓 Learning Git

Git is a skill in itself! Resources:
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- Ask Copilot Chat: "Explain git [command]"
- Practice with each exercise
- Ask teammates for help

---

**Remember:** Making mistakes is part of learning! Git lets you experiment safely because you can always go back.

**Questions?** Ask in the team channel or during office hours.

**Happy coding! 🚀**
