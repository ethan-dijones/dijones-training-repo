# Week 2: HTML & CSS Fundamentals

Welcome to Week 2! This week you'll build web pages and make them look professional.

## 🎯 Week 2 Goals

By the end of this week, you will:
- ✅ Understand HTML structure and common tags
- ✅ Build complete web pages from scratch
- ✅ Style pages with CSS
- ✅ Create responsive layouts
- ✅ Build a team FAQ page project

## 📚 Prerequisites

Before starting Week 2:
- Completed Week 1 exercises
- Comfortable with Git (add, commit, push)
- GitHub Copilot working in VS Code

## 📅 This Week's Exercises

### Day 1-2: HTML Basics

**Read:** [Course docs](../../docs/COURSE.md) - Week 2, Module 2.1

**Exercise 1: Build Your First Page**

Create: `exercises/week2/first-page.html`

Build a page with:
- Proper HTML5 structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Title in the `<head>`
- Heading (`<h1>`)
- Paragraph (`<p>`)
- Unordered list (`<ul>` with `<li>`)
- Link (`<a>`)
- Image placeholder (`<img>`)

**Use Copilot:**
```html
<!-- Create a basic HTML5 page structure -->

<!-- Add a main heading with "My Helpdesk Team" -->

<!-- Create a paragraph describing what we do -->

<!-- Add an unordered list of our services -->
```

**Commit:**
```bash
git add exercises/week2/first-page.html
git commit -m "Create first HTML page"
git push origin main
```

**Exercise 2: HTML Elements Practice**

Create: `exercises/week2/elements-practice.html`

Practice these elements:
- Different heading levels (`<h1>` through `<h6>`)
- Bold (`<strong>`) and italic (`<em>`)
- Line break (`<br>`)
- Horizontal rule (`<hr>`)
- Ordered list (`<ol>`)
- Link that opens in new tab
- Multiple paragraphs

**Commit your work!**

---

### Day 3-4: CSS Styling

**Read:** Course docs - Week 2, Module 2.2

**Exercise 3: Add Basic Styles**

Create: `exercises/week2/styled-page.html` and `exercises/week2/styles.css`

HTML file:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Styled Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>My Styled Page</h1>
    </header>
    <main>
        <p>This page has custom styling!</p>
    </main>
</body>
</html>
```

In `styles.css`, add:
```css
/* Use Copilot with these comments: */

/* Style the header with dark background and white text */

/* Add padding and margins to the main content */

/* Style all paragraphs with a custom font and color */

/* Create a hover effect for links */
```

**Test:** Open `styled-page.html` in your browser (Right-click → Open with Live Server)

**Exercise 4: CSS Practice**

Create: `exercises/week2/css-practice/` folder with:
- `index.html` - A page with various elements
- `style.css` - Styles for different selectors

Practice:
- Element selectors (`h1`, `p`, `a`)
- Class selectors (`.highlight`, `.button`)
- ID selectors (`#header`, `#main`)
- Colors (names, hex codes, RGB)
- Fonts and sizes
- Spacing (margin, padding)
- Borders

**Commit all files!**

---

### Day 5: Week 2 Project - FAQ Page

**Project:** Build a Helpdesk FAQ Page

Create: `exercises/week2/faq-project/` folder with:
- `index.html`
- `style.css`

**Requirements:**

**HTML Structure:**
- Header with team name and tagline
- At least 5 FAQ items (question + answer)
- Each FAQ has a heading (question) and paragraph (answer)
- Footer with contact info

**CSS Styling:**
- Custom color scheme
- Nice typography (Google Fonts optional)
- Spacing between FAQ items
- Hover effects on questions
- Responsive design (looks good on mobile)
- Professional appearance

**Use Copilot to help you:**

```html
<!-- Create a header section with centered team name and tagline -->

<!-- Create FAQ section with 5 question-answer pairs -->

<!-- Add a footer with email and phone contact info -->
```

```css
/* Create a modern color scheme with primary and accent colors */

/* Style FAQ questions as clickable-looking elements with hover effect */

/* Add box shadow to FAQ items for depth */

/* Make layout responsive for mobile devices */
```

**Testing:**
1. Open in browser (use Live Server extension)
2. Test on different window sizes
3. Check all links work
4. Verify hover effects work

**Commit your project:**
```bash
git add exercises/week2/faq-project/
git commit -m "Complete Week 2 project: FAQ page"
git push origin main
```

---

## 💡 Tips & Best Practices

### HTML Tips
- Always use proper structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Use semantic tags (`<header>`, `<main>`, `<footer>`, `<nav>`)
- Add `alt` text to images
- Indent your code properly
- Close all tags

### CSS Tips
- Use external stylesheet (separate .css file)
- Comment your CSS to remember what each section does
- Group related styles together
- Use consistent spacing
- Test in browser frequently

### Copilot Tips
- Describe what you want in comments
- Let Copilot suggest structure, then customize
- Ask Copilot Chat to explain CSS properties
- Use Copilot to generate color schemes
- Request responsive design patterns

---

## 🎨 Design Resources

### Color Schemes
Ask Copilot: "Suggest a professional color scheme for an IT helpdesk website"

Or try:
- **Professional:** #2C3E50 (dark blue), #3498DB (blue), #ECF0F1 (light gray)
- **Friendly:** #16A085 (teal), #27AE60 (green), #F39C12 (orange)
- **Corporate:** #34495E (navy), #95A5A6 (gray), #FFFFFF (white)

### Google Fonts
Add to your HTML `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

Then in CSS:
```css
body {
    font-family: 'Inter', sans-serif;
}
```

---

## ✅ Week 2 Completion Checklist

Before moving to Week 3:

### HTML Skills
- [ ] Can write proper HTML5 structure
- [ ] Know common tags (h1-h6, p, a, img, ul, ol, li)
- [ ] Understand semantic HTML
- [ ] Can link CSS files
- [ ] Can create forms and inputs

### CSS Skills
- [ ] Can write CSS rules
- [ ] Understand selectors (element, class, ID)
- [ ] Can style text (font, color, size)
- [ ] Can add spacing (margin, padding)
- [ ] Can create hover effects
- [ ] Understand box model

### Projects
- [ ] `first-page.html` - Basic HTML practice
- [ ] `elements-practice.html` - HTML elements
- [ ] `styled-page.html` + `styles.css` - Basic styling
- [ ] `css-practice/` - CSS selectors practice
- [ ] `faq-project/` - Complete FAQ page
- [ ] All files committed and pushed to GitHub

### Copilot Usage
- [ ] Used comments to generate HTML structure
- [ ] Used Copilot for CSS styling
- [ ] Asked Copilot Chat to explain properties
- [ ] Customized Copilot's suggestions

---

## 🆘 Common Issues

**"My CSS isn't loading"**
- Check the `<link>` tag in HTML
- Verify CSS filename matches exactly
- Check both files are in same folder
- Hard refresh browser (Ctrl+Shift+R)

**"Page looks different in browser"**
- Clear browser cache
- Check for CSS typos
- Use browser DevTools (F12)
- Try different browser

**"Can't see my changes"**
- Save the file (Ctrl+S)
- Refresh browser (F5)
- Check you're editing the right file

**"Layout not working"**
- Use browser DevTools to inspect
- Ask Copilot Chat for help with layout
- Check for typos in CSS properties
- Verify selectors are correct

---

## 🎉 Finished Week 2?

Great work! You can now:
- Build web pages from scratch
- Style them professionally
- Use HTML and CSS together
- Create responsive layouts

**Next:** [Week 3](../week3/) - Add interactivity with JavaScript!

**Before moving on:**
- [ ] All exercises completed
- [ ] FAQ project finished and looks good
- [ ] Everything committed to GitHub
- [ ] Shared your FAQ page with team

---

**Pro tip for Week 3:** The JavaScript you'll learn next will make your pages interactive. Keep your Week 2 FAQ page - we'll add JavaScript to it in Week 3!

**You're crushing it! 🎨 See you in Week 3! 🚀**
