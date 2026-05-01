# Week 1: Foundations & AI Tools

Welcome to Week 1! This week you'll learn the basics of development tools and master GitHub Copilot.

## 🎯 Week 1 Goals

By the end of this week, you will:
- ✅ Navigate using terminal commands
- ✅ Use GitHub Copilot effectively in VS Code
- ✅ Make Git commits and push to GitHub
- ✅ Write code comments that trigger good Copilot suggestions
- ✅ Ask Copilot Chat to explain code

## 📅 Daily Schedule

### Day 1: Terminal & Git Basics (Your First Day!)

**You've already started this!** By forking and cloning this repository, you completed your first exercise.

**Today's Tasks:**
1. ✅ Fork this repository (you did this!)
2. ✅ Clone to your computer (done!)
3. ✅ Add your name to STUDENT_ROSTER.md (if not done, do it now!)
4. Complete terminal practice exercises below

**Terminal Navigation Practice:**

Create this exercise file: `exercises/week1/terminal-practice.md`

```bash
# Navigate to week1 exercises folder
cd exercises/week1

# Create a new file
touch terminal-practice.md

# Open in VS Code
code terminal-practice.md
```

In that file, document these commands as you try them:

```markdown
# Terminal Practice Exercise

## Commands I practiced:

### pwd (Print Working Directory)
- What it does: Shows where I am in the file system
- Example output: [paste your output here]

### ls (List)
- What it does: Shows files and folders in current directory
- Example output: [paste your output here]

### cd (Change Directory)
- What it does: Moves to a different folder
- Commands I tried:
  - cd exercises
  - cd ..
  - cd week1

### mkdir (Make Directory)
- What it does: Creates a new folder
- Folder I created: [name]

### touch (Create File)
- What it does: Creates a new empty file
- File I created: [name]
```

**Commit Your Work:**
```bash
git add exercises/week1/terminal-practice.md
git commit -m "Complete terminal navigation practice"
git push origin main
```

---

### Day 2: VS Code & Copilot Setup

**Verify Your Tools:**

Create: `exercises/week1/copilot-test.js`

```javascript
// Type this comment and let Copilot complete it:
// Function to add two numbers together

// After Copilot suggests code, press Tab to accept
// Then test it works:
console.log(add(5, 3)); // Should output 8
```

**Copilot Chat Practice:**

1. Highlight the function Copilot created
2. Press `Ctrl+I` (or `Cmd+I` on Mac) to open Copilot Chat
3. Ask: "Explain this function line by line"
4. Document what you learned

Create: `exercises/week1/copilot-learnings.md`

Document:
- What Copilot explained about the function
- 3 things you learned about JavaScript syntax
- Any questions you still have

**Commit:**
```bash
git add exercises/week1/copilot-test.js exercises/week1/copilot-learnings.md
git commit -m "Practice using GitHub Copilot"
git push origin main
```

---

### Day 3: Copilot Prompt Writing

**Exercise: Write Comments that Get Good Suggestions**

Create: `exercises/week1/prompt-practice.js`

Try these prompts (type as comments, let Copilot suggest):

```javascript
// 1. Function that checks if a number is even or odd

// 2. Function that converts temperature from Celsius to Fahrenheit

// 3. Function to validate an email address format

// 4. Array of 5 ticket statuses for a helpdesk system

// 5. Function that takes a ticket ID and formats it as "TKT-00000"
```

**Reflection:**
Create: `exercises/week1/prompt-reflection.md`

Answer:
1. Which prompts got better suggestions?
2. When did you need to be more specific?
3. What makes a "good" Copilot prompt?
4. Did you have to fix any of Copilot's suggestions?

**Commit:**
```bash
git add exercises/week1/prompt-practice.js exercises/week1/prompt-reflection.md
git commit -m "Practice writing effective Copilot prompts"
git push origin main
```

---

### Day 4: Git Workflow Practice

**Exercise: Multiple Commits**

Today, practice the full Git workflow multiple times:

1. **Create a file:** `exercises/week1/git-practice.md`
2. **Add content about what you learned so far**
3. **Save, add, commit, push:**
   ```bash
   git add exercises/week1/git-practice.md
   git commit -m "Add Week 1 learnings"
   git push origin main
   ```
4. **Add more content to the same file**
5. **Commit again with a different message**
6. **View your commits on GitHub**

**Challenge:** Make 5 separate commits today, each with a clear message

**Good commit messages:**
- ✅ "Add notes on terminal commands"
- ✅ "Document Copilot best practices"
- ✅ "Fix typo in git-practice.md"
- ❌ "update"
- ❌ "stuff"
- ❌ "asdfjkl"

---

### Day 5: Week 1 Mini-Project

**Project: Create Your Developer Profile**

Create: `exercises/week1/my-profile.html`

Use the starter template and Copilot to build a simple HTML page with:
- Your name as a heading
- Paragraph about why you're learning to code
- List of 3 goals for this course
- List of skills you want to learn

**Use Copilot:**
```html
<!-- Type comments like these and let Copilot help: -->

<!-- Create a header section with my name and title -->

<!-- Add a section about my background in IT support -->

<!-- Create an unordered list of my learning goals -->
```

**Style it (optional):**
Create: `exercises/week1/profile-style.css`

Add basic styling:
- Background color
- Text color
- Center the content
- Nice font

**Commit Your Project:**
```bash
git add exercises/week1/my-profile.html exercises/week1/profile-style.css
git commit -m "Complete Week 1 project: developer profile"
git push origin main
```

---

## ✅ Week 1 Completion Checklist

Before moving to Week 2, make sure you have:

### Git & GitHub
- [ ] Forked the training repository
- [ ] Cloned to your computer
- [ ] Added name to STUDENT_ROSTER.md
- [ ] Made multiple commits with clear messages
- [ ] Pushed all work to GitHub
- [ ] Can view your commits on GitHub.com

### Terminal
- [ ] Comfortable with `cd`, `ls`, `pwd`, `mkdir`
- [ ] Can navigate to different folders
- [ ] Can create files and folders
- [ ] Documented commands in terminal-practice.md

### VS Code
- [ ] VS Code installed and opened
- [ ] Know keyboard shortcuts (Ctrl+P, Ctrl+`)
- [ ] Can open folders and files
- [ ] Comfortable with the interface

### GitHub Copilot
- [ ] Copilot is working in VS Code
- [ ] Can trigger suggestions with comments
- [ ] Can use Copilot Chat (Ctrl+I)
- [ ] Understand when to accept/reject suggestions
- [ ] Practiced with 10+ different prompts

### Deliverables
- [ ] `terminal-practice.md` - Documented commands
- [ ] `copilot-test.js` - Function tests
- [ ] `copilot-learnings.md` - What you learned
- [ ] `prompt-practice.js` - Various prompts
- [ ] `prompt-reflection.md` - Reflections
- [ ] `git-practice.md` - Git workflow notes
- [ ] `my-profile.html` - Week 1 project
- [ ] All committed and pushed to GitHub

---

## 🆘 Getting Help

**Stuck on something?**

1. Check the error message
2. Ask Copilot Chat: "Why am I getting this error?"
3. Review the [Setup Guide](../../docs/SETUP.md)
4. Ask your coding buddy
5. Post in the team channel

**Common Issues:**

**"Git commands not working"**
- Check Git is installed: `git --version`
- Make sure you're in the repository folder: `pwd`
- Check status: `git status`

**"Copilot not suggesting"**
- Look for Copilot icon in bottom right of VS Code
- Try restarting VS Code
- Make sure you're signed into GitHub
- Write more descriptive comments

**"Can't push to GitHub"**
- Check you cloned YOUR fork (not the original)
- Verify: `git remote -v` should show YOUR username
- Make sure you committed first: `git status`

---

## 🎉 Finished Week 1?

**Celebrate!** You've learned:
- Terminal navigation
- Git version control
- VS Code basics
- GitHub Copilot usage
- How to learn by doing

**Next:** Head to [Week 2](../week2/) to start building web pages with HTML and CSS!

**Before you go:**
- [ ] All files committed and pushed
- [ ] Completed the checklist above
- [ ] Shared progress in team channel
- [ ] Ready to build web pages!

---

**Tips for Week 2:**
- Keep practicing Git - commit often!
- Use Copilot Chat when confused
- Reference your Week 1 files
- Help your coding buddy

**You're doing great! See you in Week 2! 🚀**
