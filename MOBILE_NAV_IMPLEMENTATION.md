# Mobile Navigation Implementation Guide

## Overview
This document provides the complete HTML and CSS for implementing a pure CSS mobile hamburger menu that does NOT affect desktop navigation.

**Desktop (>= 768px):** Unchanged - works exactly as before  
**Mobile (< 768px):** New hamburger menu with slide-in drawer

---

## ✅ CSS Already Added
The CSS has been added to `MABA-modern.css`. No additional CSS files needed.

---

## 📝 HTML Structure to Replace

### Location
Replace the `<nav id="topnav">` section in ALL HTML files.

### Current Structure (to be replaced):
```html
<nav id="topnav">
<div class="container navbar">
<ul class="menu">
<li><a href="index.html">Home</a></li>
<li><a href="aboutus.html">About Us</a></li>
<li><a href="events.html">Events</a></li>
<li class="has-sub"><a href="positions.html">Positions</a>
<ul class="sub">
<li><a href="resolutions.html">Resolutions</a></li>
<li><a href="Manifesto/manifesto.html">Manifesto</a></li>
<li><a href="strategic_plan.html">Strategic Plan</a></li>
</ul>
</li>
<li class="has-sub"><a href="resources.html">Resources</a>
<ul class="sub">
<li><a href="articles.html">Articles</a></li>
<li><a href="blog.html">Blog</a></li>
<li><a href="links.html">Links</a></li>
<li><a href="news.html">News</a></li>
</ul>
</li>
<li class="spacer"></li>
<li><a class="btn-cta" href="volunteer.html">Join</a></li>
<li><a class="btn-cta" href="membership.html">Membership</a></li>
<li><a class="btn-cta" href="donate.html">Donate</a></li>
</ul>
</div>
</nav>
```

### New Structure (replace with this):
```html
<nav id="topnav">
  <!-- Hidden checkbox for mobile menu toggle -->
  <input type="checkbox" id="menu-toggle">
  
  <!-- Hamburger button (mobile only) -->
  <label for="menu-toggle" class="hamburger-label" aria-label="Open menu">
    <span></span>
    <span></span>
    <span></span>
  </label>
  
  <!-- Desktop navigation (unchanged) -->
  <div class="container navbar">
    <ul class="menu">
      <li><a href="index.html">Home</a></li>
      <li><a href="aboutus.html">About Us</a></li>
      <li><a href="events.html">Events</a></li>
      <li class="has-sub"><a href="positions.html">Positions</a>
        <ul class="sub">
          <li><a href="resolutions.html">Resolutions</a></li>
          <li><a href="Manifesto/manifesto.html">Manifesto</a></li>
          <li><a href="strategic_plan.html">Strategic Plan</a></li>
        </ul>
      </li>
      <li class="has-sub"><a href="resources.html">Resources</a>
        <ul class="sub">
          <li><a href="articles.html">Articles</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="links.html">Links</a></li>
          <li><a href="news.html">News</a></li>
        </ul>
      </li>
      <li class="spacer"></li>
      <li><a class="btn-cta" href="volunteer.html">Join</a></li>
      <li><a class="btn-cta" href="membership.html">Membership</a></li>
      <li><a class="btn-cta" href="donate.html">Donate</a></li>
    </ul>
  </div>
  
  <!-- Overlay (mobile only) -->
  <label for="menu-toggle" class="nav-overlay"></label>
  
  <!-- Mobile drawer menu (mobile only) -->
  <div class="mobile-drawer">
    <ul class="mobile-menu">
      <li><a href="index.html">Home</a></li>
      <li><a href="aboutus.html">About Us</a></li>
      <li><a href="events.html">Events</a></li>
      
      <!-- Positions submenu with accordion -->
      <li>
        <details>
          <summary>Positions</summary>
          <a href="positions.html">Positions</a>
          <ul class="submenu">
            <li><a href="resolutions.html">Resolutions</a></li>
            <li><a href="Manifesto/manifesto.html">Manifesto</a></li>
            <li><a href="strategic_plan.html">Strategic Plan</a></li>
          </ul>
        </details>
      </li>
      
      <!-- Resources submenu with accordion -->
      <li>
        <details>
          <summary>Resources</summary>
          <a href="resources.html">Resources</a>
          <ul class="submenu">
            <li><a href="articles.html">Articles</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="links.html">Links</a></li>
            <li><a href="news.html">News</a></li>
          </ul>
        </details>
      </li>
      
      <li><a class="btn-cta" href="volunteer.html">Join</a></li>
      <li><a class="btn-cta" href="membership.html">Membership</a></li>
      <li><a class="btn-cta" href="donate.html">Donate</a></li>
    </ul>
  </div>
</nav>
```

---

## 🔧 Implementation Steps

### Step 1: Update index.html
1. Open `index.html`
2. Find the `<nav id="topnav">` section (around line 71)
3. Replace the entire `<nav>` section with the new structure above
4. **Important:** Adjust paths if needed (e.g., `../` for subdirectory pages)

### Step 2: Update All Other HTML Files
Repeat Step 1 for ALL HTML files that have navigation:
- `aboutus.html`
- `articles.html`
- `blog.html`
- `events.html`
- `links.html`
- `membership.html`
- `news.html`
- `positions.html`
- `resolutions.html`
- `resources.html`
- `strategic_plan.html`
- `volunteer.html`
- `donate.html`
- All files in subdirectories (articles/, blog/, positions/, etc.)

**For subdirectory pages:** Adjust paths with `../` as needed:
- `href="../index.html"` instead of `href="index.html"`
- `href="../aboutus.html"` instead of `href="aboutus.html"`
- etc.

### Step 3: Test
1. Test on desktop (>= 768px) - should look identical to before
2. Test on mobile (< 768px):
   - Hamburger button appears
   - Clicking hamburger opens drawer from right
   - Overlay appears
   - Clicking overlay closes menu
   - Submenus expand/collapse with smooth animation
   - All links work correctly

---

## 📋 Key Features

### Desktop (>= 768px)
- ✅ **Unchanged** - exact same appearance and behavior
- ✅ Horizontal navigation bar
- ✅ Dropdown menus on hover
- ✅ CTA buttons inline on right

### Mobile (< 768px)
- ✅ Hamburger button (3 lines, animates to X when open)
- ✅ Slide-in drawer from right side
- ✅ Semi-transparent overlay
- ✅ Pure CSS accordions for submenus (`<details>`/`<summary>`)
- ✅ Smooth animations (CSS transitions)
- ✅ Full-width CTA buttons
- ✅ Accessible (keyboard navigation, ARIA labels)
- ✅ Sticky header remains sticky

---

## 🎨 Visual Details

### Mobile Menu
- **Drawer width:** 280px (max 85vw on very small screens)
- **Background:** Dark blue (`var(--nav)`)
- **Text color:** White
- **CTA buttons:** Yellow background (`var(--yellow)`), black text
- **Submenu background:** Slightly darker (rgba(0,0,0,0.2))
- **Animations:** 0.3s ease transitions

### Hamburger Icon
- **Size:** 30px × 24px
- **Color:** White
- **Animation:** Rotates to X when menu is open
- **Position:** Top-right of nav bar

---

## ♿ Accessibility

- ✅ `aria-label="Open menu"` on hamburger button
- ✅ `<details>`/`<summary>` provide native keyboard navigation
- ✅ All links are keyboard accessible
- ✅ Focus states visible
- ✅ Semantic HTML structure

---

## 🐛 Troubleshooting

### Menu doesn't open on mobile
- Check that `#menu-toggle` checkbox is present
- Verify `for="menu-toggle"` on hamburger label
- Check CSS media query is `@media(max-width:767px)`

### Desktop nav is hidden
- Check media query - should only hide on mobile
- Verify `.navbar` is not hidden on desktop

### Submenus don't expand
- Verify `<details>` and `<summary>` tags are correct
- Check that `.submenu` class is on the `<ul>` inside `<details>`

### Overlay doesn't close menu
- Verify overlay is a `<label for="menu-toggle">`
- Check z-index: overlay should be z-index:999, drawer z-index:1000

---

## 📝 Notes

- **No JavaScript required** - pure CSS solution
- **Works on GitHub Pages** - no build process needed
- **Lightweight** - minimal CSS additions
- **Maintainable** - clean, semantic HTML
- **Future-proof** - uses standard HTML5 elements

---

## ✅ Checklist

Before deploying:
- [ ] Updated `index.html` navigation
- [ ] Updated all other HTML files with navigation
- [ ] Adjusted paths for subdirectory pages
- [ ] Tested on desktop (>= 768px) - looks identical
- [ ] Tested on mobile (< 768px) - hamburger works
- [ ] Tested submenu accordions expand/collapse
- [ ] Tested overlay closes menu
- [ ] Tested all links work correctly
- [ ] Tested keyboard navigation
- [ ] Verified no JavaScript errors in console

---

## 🚀 Ready to Deploy

Once all HTML files are updated and tested, the mobile navigation is ready for GitHub Pages!

