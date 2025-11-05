# MABA Website Technical Documentation

## Overview

This document provides a comprehensive guide to the Madison Area Bus Advocates (MABA) website structure, CSS architecture, accessibility features, and maintenance procedures. The site is a modern, responsive website built with HTML5 and CSS3, designed for deployment on GitHub Pages and later https://www.busadvocates.org/.

---

## Table of Contents

1. [Site Architecture](#site-architecture)
2. [CSS File Structure](#css-file-structure)
3. [HTML Structure & Patterns](#html-structure--patterns)
4. [Accessibility Features](#accessibility-features)
5. [Design System](#design-system)
6. [How-To Guides](#how-to-guides)
   - [Implementing the Lightbox Effect](#implementing-the-lightbox-effect)
   - [Implementing Quote/Blockquote Styling](#implementing-quoteblockquote-styling)
   - [Implementing Section Styling](#implementing-section-styling)
   - [Implementing Card Styling](#implementing-card-styling)
   - [Adding a Hero Banner](#adding-a-hero-banner)
   - [Adding a Page to Top-Level Navigation](#adding-a-page-to-top-level-navigation)
   - [Adding a Page to Navigation Submenu](#adding-a-page-to-navigation-submenu)
   - [Ensuring Navigation Works Across the Site](#ensuring-navigation-works-across-the-site)
8. [Responsive Design](#responsive-design)
9. [SEO & Geo-Optimization](#seo--geo-optimization)
10. [Maintenance & Updates](#maintenance--updates)

---

## Site Architecture

### Directory Structure

- **Root Directory**: Contains main pages (`index.html`, `aboutus.html`, `events.html`, etc.)
- **`articles/`**: Contains organized article content by topic
- **`blog/`**: Blog posts and entries
- **`positions/`**: Position statements and resolutions
- **`Manifesto/`**: Transit manifesto content
- **`Images/`**: All image assets
- **`misc/`**: Miscellaneous and archive files
- **`index_pages/`**: Old homepage versions (archived)

### Key Files

- **`index.html`**: Homepage (GitHub Pages automatically serves this)
- **`MABA-modern.css`**: Single stylesheet for entire site (295 lines)

---

## CSS File Structure

### CSS Variables (Design Tokens)

The site uses CSS custom properties (variables) defined in `:root` for consistent theming:

```css
:root {
  --blue: #1C6B8F;      /* Primary brand blue */
  --nav: #0F3D53;      /* Darker blue for navigation */
  --yellow: #E1E31B;    /* Accent yellow for CTAs */
  --text: #222;         /* Main text color */
  --muted: #F6F7F8;     /* Light gray backgrounds */
  --container: 1280px;  /* Max content width */
  --radius: 14px;       /* Border radius for cards */
  --shadow: 0 8px 24px rgba(0,0,0,.08); /* Standard shadow */
}
```

**Why Variables?** Changing colors or spacing site-wide requires updating only these values.

### Typography

- **Font Family**: Open Sans (Google Fonts), with system font fallbacks
- **Font Weights**: 400 (regular), 700 (bold), 800 (extra-bold)
- **Base Line Height**: 1.55 for readability

### Key CSS Sections

#### 1. Layout System
- **`.container`**: Centered container with max-width of 1280px, 20px padding
- **`main.container`**: Same container with 30px vertical padding for content pages
- **Grid System**: CSS Grid for responsive layouts (3 columns → 2 → 1 on mobile)

#### 2. Navigation (`#topnav`)
- **Sticky Navigation**: Uses `position: sticky` when `body.sticky` class is present
- **Dropdown Menus**: CSS-only dropdowns using `:hover` and `:focus-within`
- **Spacer Element**: `.spacer` uses `flex: 1` to push action buttons right

#### 3. Components

**Cards** (`.card`):
- White background with shadow
- Responsive grid (3 → 2 → 1 columns)
- Images: 220px height, object-fit: cover

**Buttons** (`.btn-cta`):
- Yellow background (`--yellow`)
- Black text
- Rounded corners
- Used for "Join", "Membership", "Donate"

**Lightbox** (`.lightbox`):
- CSS-only image lightbox (no JavaScript)
- Uses `:target` pseudo-class
- Accessible via `aria-label` attributes

#### 4. Page Sections

**`.about-page-section`**:
- Standard styling for content pages
- Headings: h1/h2 (1.8em), h3 (1.4em)
- Paragraph spacing and typography
- List styling with custom bullets
- Blockquote styling with yellow accent border

---

## HTML Structure & Patterns

### Standard Page Template

Every formatted page follows this structure with SEO meta tags and full navigation:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="[Unique 150-160 character description for this page]"/>
  <meta name="keywords" content="[Relevant keywords for this page, Madison bus, public transit, etc.]"/>
  <meta name="geo.region" content="US-WI"/>
  <meta name="geo.placename" content="Madison"/>
  <meta name="geo.position" content="43.0731;-89.4012"/>
  <meta name="ICBM" content="43.0731, -89.4012"/>
  <link rel="canonical" href="https://www.busadvocates.org/[page.html]"/>
  
  <!-- Open Graph Tags -->
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://www.busadvocates.org/[page.html]"/>
  <meta property="og:title" content="[Page Title] | Madison Area Bus Advocates"/>
  <meta property="og:description" content="[Description for social sharing]"/>
  <meta property="og:image" content="https://www.busadvocates.org/Images/MABAlogo.png"/>
  
  <!-- Twitter Card Tags -->
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="[Page Title] | Madison Area Bus Advocates"/>
  <meta name="twitter:description" content="[Description for Twitter]"/>
  <meta name="twitter:image" content="https://www.busadvocates.org/Images/MABAlogo.png"/>
  
  <title>[Page Title] | Madison Area Bus Advocates</title>
  <link href="MABA-modern.css" rel="stylesheet"/>
</head>
<body class="sticky">
  <!-- Header -->
  <header class="top-header">
    <div class="container wrap">
      <div class="row-1">
        <img alt="MABA logo" class="logo" src="Images/MABAlogo.png"/>
        <span class="org">Madison Area Bus Advocates</span>
      </div>
      <div class="row-2">Buses for People. People for Buses.</div>
    </div>
  </header>
  
  <!-- Navigation -->
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
  
  <!-- Main Content -->
  <main class="container">
    <section class="about-page-section">
      <!-- Page content -->
    </section>
  </main>
  
  <!-- Footer -->
  <footer class="footer">
    Madison Area Bus Advocates | P.O. Box 260156, Madison, WI 53726 | info@busadvocates.org
  </footer>
</body>
</html>
```

**Note**: For pages in subdirectories, adjust paths accordingly:
- Root pages: `href="index.html"`, `href="Images/MABAlogo.png"`
- 1 level deep: `href="../index.html"`, `href="../Images/MABAlogo.png"`
- 2 levels deep: `href="../../index.html"`, `href="../../Images/MABAlogo.png"`

### Navigation Paths

The navigation uses relative paths based on directory depth:

- **Root pages**: `href="index.html"`, `href="aboutus.html"`
- **Subdirectories** (e.g., `positions/`): `href="../index.html"`, `href="../aboutus.html"`
- **Deep subdirectories** (e.g., `articles/parking/`): `href="../../index.html"`

### Homepage Link Standard

**All pages link to the homepage as `index.html`** (not `MABA-index.html`). This ensures GitHub Pages serves the correct file automatically.

---

## Accessibility Features

### WCAG 2.1 Compliance

The site implements multiple accessibility best practices:

#### 1. Semantic HTML
- Proper use of `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- Heading hierarchy (h1 → h2 → h3)
- Lists use `<ul>` and `<ol>` appropriately

#### 2. Image Accessibility
- **Alt Text**: All images have descriptive `alt` attributes
- **Decorative Images**: Use `alt=""` when image is purely decorative
- **Contextual Images**: Alt text describes content and purpose

Example:
```html
<img alt="Regional transit concept map" src="Images/transit2020_bussystem.png"/>
```

#### 3. Keyboard Navigation
- All links and buttons are keyboard accessible
- Tab order follows logical content flow
- Dropdown menus work with `:focus-within` for keyboard users

#### 4. ARIA Labels
- Lightbox images: `aria-label="Enlarge image"`
- Close buttons: `aria-label="Close"`
- Dialog roles: `role="dialog"` on lightboxes

#### 5. Color Contrast
- Text color (`#222`) on white background: **16.77:1** (AAA compliant)
- White text on blue background (`#1C6B8F`): **4.5:1+** (AA compliant)
- Yellow buttons (`#E1E31B`) with black text: High contrast

#### 6. Responsive Design
- Mobile-first approach
- No horizontal scrolling
- Touch-friendly button sizes (minimum 44×44px)

#### 7. Viewport Meta Tag
Every page includes:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```


## Design System

### Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Blue | `#1C6B8F` | Header background, links, accents |
| Navigation Blue | `#0F3D53` | Navigation bar, headings |
| Accent Yellow | `#E1E31B` | Call-to-action buttons |
| Text | `#222` | Body text |
| Muted | `#F6F7F8` | Blockquote backgrounds |

### Typography Scale

- **H1/H2**: 1.8em (28.8px), weight 800
- **H3**: 1.4em (22.4px), weight 800
- **Body**: 1em (16px), weight 400
- **Recent Blog**: 1.25em (20px), weight 800

### Spacing System

- **Container Padding**: 20px horizontal, 30px vertical for content
- **Section Padding**: 30-36px vertical
- **Card Padding**: 16-18px
- **Grid Gap**: 24px

### Component Styles

**Cards**:
- White background
- 12px border radius
- Box shadow for depth
- 220px image height

**Buttons**:
- Yellow background (`--yellow`)
- Black text
- 10px padding
- 10px border radius
- Hover: slight brightness reduction

---

## How-To Guides

### Implementing the Lightbox Effect

The site uses a **CSS-only lightbox** (no JavaScript required) that displays full-size images in a modal overlay when clicked. This is implemented using CSS `:target` pseudo-class.

#### How It Works

1. **Anchor Link**: The image is wrapped in an anchor tag that links to a unique ID (e.g., `#img-example`)
2. **Lightbox Container**: A hidden `<div>` with the matching ID serves as the lightbox overlay
3. **CSS Activation**: When the anchor is clicked, the URL hash changes to `#img-example`, and the CSS `:target` selector activates the lightbox
4. **Close Mechanism**: Clicking the backdrop or close button removes the hash, hiding the lightbox

#### Step-by-Step Implementation

**Step 1: Wrap your image in an anchor tag**

```html
<a aria-label="Enlarge [image description]" href="#img-example">
  <img alt="Your image description" src="Images/your-image.jpg"/>
</a>
```

**Step 2: Add the lightbox container before the footer**

```html
<!-- CSS-only Lightbox (no JS) -->
<div aria-label="Image preview" class="lightbox" id="img-example" role="dialog">
  <a aria-label="Close" class="backdrop" href="#"></a>
  <img alt="Your image description full size" src="Images/your-image.jpg"/>
  <a aria-label="Close preview" class="lb-close" href="#">Close ✕</a>
</div>
```

**Important Notes:**
- The `href` in the anchor must match the `id` of the lightbox (e.g., `#img-example` → `id="img-example"`)
- Use unique IDs for each image on the same page
- The lightbox should be placed **after** `</main>` and **before** `<footer>`
- Include `aria-label` attributes for accessibility

#### Example: Full Implementation

```html
<!-- In your content section -->
<main class="container">
  <section class="about-page-section">
    <h1>My Page</h1>
    <a aria-label="Enlarge board photo" href="#img-board">
      <img alt="Board Members" src="Images/board.jpg"/>
    </a>
  </section>
</main>

<!-- Lightbox (before footer) -->
<div aria-label="Image preview" class="lightbox" id="img-board" role="dialog">
  <a aria-label="Close" class="backdrop" href="#"></a>
  <img alt="Board Members full size" src="Images/board.jpg"/>
  <a aria-label="Close preview" class="lb-close" href="#">Close ✕</a>
</div>
<footer class="footer">...</footer>
```

#### CSS Styling (Already in MABA-modern.css)

The lightbox styling is handled by these CSS rules:

```css
.lightbox {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.8);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
  z-index: 2000;
}
.lightbox:target {
  display: flex; /* Shows when URL hash matches ID */
}
.lightbox img {
  max-width: min(1200px, 95vw);
  max-height: 90vh;
  border-radius: 10px;
  box-shadow: 0 12px 40px rgba(0,0,0,.5);
}
```

**No additional CSS needed** - all styling is already in `MABA-modern.css`.

---

### Implementing Quote/Blockquote Styling

The site uses a consistent blockquote style for quotations, emphasizing important text with a yellow accent border and light gray background.

#### Standard Blockquote Pattern

```html
<blockquote>
  <p><em>"Your quote text here" - Attribution</em></p>
</blockquote>
```

#### HTML Structure

The blockquote should be placed within a `.about-page-section`:

```html
<section class="about-page-section">
  <h2>Section Title</h2>
  <p>Regular paragraph content...</p>
  
  <blockquote>
    <p><em>"The most important function of transportation is to move us from being strangers towards becoming friends" - Hans Noeldner</em></p>
  </blockquote>
</section>
```

#### CSS Styling (Already in MABA-modern.css)

Blockquotes are automatically styled with:

```css
.about-page-section blockquote {
  margin: 25px 0;
  padding: 20px;
  border-left: 4px solid var(--yellow);
  background: var(--muted);
}
.about-page-section blockquote p {
  margin: 0;
  font-style: italic;
  color: var(--text);
}
```

**No additional CSS needed** - the styling is automatic when using `<blockquote>` within `.about-page-section`.

#### Homepage Blockquote (Special Styling)

For blockquotes on the homepage (outside `.about-page-section`), use the `.homepage-blockquote` wrapper:

```html
<section class="homepage-blockquote">
  <blockquote>
    <p><em>"We'll be the first generation in the history of the planet that drove to the poorhouse in an automobile" - Will Rogers, 1931</em></p>
  </blockquote>
</section>
```

#### Best Practices

1. **Use `<em>` tags** inside the quote paragraph for italic styling
2. **Include attribution** (author, date) within the quote
3. **Keep quotes concise** - long quotes may need to be split into multiple paragraphs
4. **Accessibility**: Screen readers will identify `<blockquote>` as a quotation

---

### Implementing Section Styling

The site uses `.about-page-section` for consistent content page styling. This provides standardized typography, spacing, and layout for all main content sections.

#### Standard Section Pattern

```html
<main class="container">
  <section class="about-page-section">
    <h1>Section Title</h1>
    <p>Your content here...</p>
  </section>
</main>
```

#### HTML Structure

Sections should be placed within `<main class="container">`:

```html
<main class="container">
  <!-- First Section -->
  <section class="about-page-section">
    <h1>About Us</h1>
    <p>Content for the first section...</p>
    <ul>
      <li>List items</li>
    </ul>
  </section>

  <!-- Second Section -->
  <section class="about-page-section">
    <h2>Mission</h2>
    <p>Content for the second section...</p>
  </section>
</main>
```

#### Multiple Sections on One Page

For pages with multiple sections, simply add more `<section class="about-page-section">` elements:

```html
<main class="container">
  <section class="about-page-section">
    <h1>Main Title</h1>
    <p>Introduction...</p>
  </section>

  <section class="about-page-section">
    <h2>Subsection</h2>
    <p>More content...</p>
  </section>
</main>
```

#### Two-Column Grid Layout

For side-by-side content (like "Mission" and "Additional Documents"), use `.about-page-grid`:

```html
<main class="container">
  <div class="about-page-grid">
    <section class="about-page-section">
      <h1>Mission</h1>
      <p>Mission content...</p>
    </section>

    <section class="about-page-section">
      <h1>Additional Documents</h1>
      <div class="doc-links">
        <a href="file.pdf">Document 1 (PDF)</a>
        <a href="file2.pdf">Document 2 (PDF)</a>
      </div>
    </section>
  </div>
</main>
```

**Responsive Behavior**: The grid automatically switches from 2 columns (desktop) to 1 column (mobile).

#### CSS Styling (Already in MABA-modern.css)

Sections are automatically styled with:
- Consistent typography (h1: 1.8em, h2: 1.8em, h3: 1.4em)
- Proper spacing (margins and padding)
- List styling with custom bullets
- Link colors matching site theme
- Blockquote styling

**No additional CSS needed** - all styling is automatic when using `.about-page-section`.

---

### Implementing Card Styling

Cards are used on the homepage to display feature content in a responsive grid layout. Each card can contain an image, heading, text, and a "Read more" link.

#### Basic Card Structure

```html
<section class="cards">
  <div class="container">
    <div class="grid">
      <article class="card">
        <div class="content">
          <h3>Card Title</h3>
          <p>Card description text...</p>
          <a class="more" href="page.html">Read more</a>
        </div>
      </article>
    </div>
  </div>
</section>
```

#### Card with Image

```html
<article class="card">
  <a aria-label="Enlarge image" href="#img-example">
    <img alt="Image description" src="Images/image.jpg"/>
  </a>
  <div class="content">
    <h3><a href="page.html" style="text-decoration:none;color:inherit">Card Title</a></h3>
    <p>Card description text...</p>
    <a class="more" href="page.html">Read more</a>
  </div>
</article>
```

#### Multiple Cards in Grid

The grid automatically creates responsive columns:

```html
<section class="cards">
  <div class="container">
    <div class="grid">
      <article class="card">
        <!-- Card 1 content -->
      </article>
      <article class="card">
        <!-- Card 2 content -->
      </article>
      <article class="card">
        <!-- Card 3 content -->
      </article>
    </div>
  </div>
</section>
```

**Responsive Behavior**:
- **Desktop (1000px+)**: 3 columns
- **Tablet (640px-1000px)**: 2 columns
- **Mobile (<640px)**: 1 column

#### Card Content Guidelines

1. **Image** (optional): Should be 220px height, will be cropped with `object-fit: cover`
2. **Title** (`<h3>`): Link optional, inherits dark blue color
3. **Description** (`<p>`): Keep concise, 2-3 sentences
4. **Read More Link** (`<a class="more">`): Optional, styled consistently across site

#### CSS Styling (Already in MABA-modern.css)

Cards are automatically styled with:
- White background with shadow
- 12px border radius
- Responsive grid layout
- Proper spacing and padding
- Hover effects on links

**No additional CSS needed** - all styling is automatic.

---

### Adding a Hero Banner

Hero banners are large, full-width images displayed prominently at the top of pages (typically the homepage). They provide visual impact and set the tone for the page.

#### Basic Hero Structure

```html
<!-- Hero -->
<section class="hero">
  <img alt="Descriptive image text" class="photo" src="Images/hero-image.jpg"/>
</section>
```

#### Placement

Hero banners should be placed **after the navigation** and **before other content**:

```html
<nav id="topnav">
  <!-- Navigation content -->
</nav>

<!-- Hero -->
<section class="hero">
  <img alt="Metro Rapid on State Street" class="photo" src="Images/BRT_Launch-51.jpg"/>
</section>

<!-- Tagline or other content -->
<section class="tagline-section">
  <!-- Content -->
</section>
```

#### Image Guidelines

- **Aspect Ratio**: 16:6 (recommended) - automatically maintained by CSS
- **Width**: Full viewport width (100%)
- **Format**: Optimized JPG or PNG
- **Size**: Recommended max 2400px width for retina displays
- **Alt Text**: Always include descriptive alt text

#### CSS Styling (Already in MABA-modern.css)

Hero images are automatically styled with:
- Full width (100%)
- 16:6 aspect ratio (maintained automatically)
- `object-fit: cover` (ensures image fills space without distortion)

**No additional CSS needed** - all styling is automatic.

---

### Adding a Page to Top-Level Navigation

To add a new top-level navigation item (e.g., "Contact", "News", "Events"), you need to update the navigation in **every HTML file** on the site.

#### Step 1: Create the HTML Page

First, create your new page file (e.g., `contact.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Contact - MABA</title>
  <link href="MABA-modern.css" rel="stylesheet"/>
</head>
<body class="sticky">
  <!-- Header, Navigation, Content, Footer -->
</body>
</html>
```

#### Step 2: Add Navigation Item to All Pages

You need to add the navigation link to **every HTML file**. Here's the pattern:

**For root-level pages** (e.g., `index.html`, `aboutus.html`):

```html
<nav id="topnav">
  <div class="container navbar">
    <ul class="menu">
      <li><a href="index.html">Home</a></li>
      <li><a href="aboutus.html">About Us</a></li>
      <li><a href="contact.html">Contact</a></li> <!-- NEW ITEM -->
      <!-- ... other items ... -->
    </ul>
  </div>
</nav>
```

**For subdirectory pages** (e.g., `positions/resolutions.html`):

```html
<ul class="menu">
  <li><a href="../index.html">Home</a></li>
  <li><a href="../aboutus.html">About Us</a></li>
  <li><a href="../contact.html">Contact</a></li> <!-- NEW ITEM with ../ -->
  <!-- ... other items ... -->
</ul>
```

#### Step 3: Update Navigation Order

The standard order is:
1. Home
2. About Us
3. Events
4. Positions (with submenu)
5. Resources (with submenu)
6. [Spacer]
7. Join
8. Membership
9. Donate

Place your new item in the appropriate location.

#### Step 4: Verify Across All Pages

**Important**: Navigation must be updated in:
- All root-level HTML files
- All files in subdirectories (using `../` for relative paths)
- Template files (if using templates)

**Quick Check**: Use your code editor's "Find and Replace" feature to search for the navigation structure and update all instances.

---

### Adding a Page to Navigation Submenu

To add a page to an existing submenu (e.g., adding "Newsletter" under "Resources"), follow these steps:

#### Step 1: Create the HTML Page

Create your new page file (e.g., `newsletter.html`) in the appropriate location.

#### Step 2: Add to Submenu in All Pages

Find the submenu you want to add to. For example, the "Resources" submenu:

**For root-level pages**:

```html
<li class="has-sub"><a href="resources.html">Resources</a>
  <ul class="sub">
    <li><a href="articles.html">Articles</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="links.html">Links</a></li>
    <li><a href="news.html">News</a></li>
    <li><a href="newsletter.html">Newsletter</a></li> <!-- NEW ITEM -->
  </ul>
</li>
```

**For subdirectory pages** (e.g., `articles/parking/index.html`):

```html
<li class="has-sub"><a href="../../resources.html">Resources</a>
  <ul class="sub">
    <li><a href="../../articles.html">Articles</a></li>
    <li><a href="../../blog.html">Blog</a></li>
    <li><a href="../../links.html">Links</a></li>
    <li><a href="../../news.html">News</a></li>
    <li><a href="../../newsletter.html">Newsletter</a></li> <!-- NEW ITEM with ../../ -->
  </ul>
</li>
```

#### Step 3: Update All Pages

**Critical**: You must update the submenu in **every HTML file** on the site. The relative path will vary:
- Root pages: `href="newsletter.html"`
- 1 level deep: `href="../newsletter.html"`
- 2 levels deep: `href="../../newsletter.html"`
- 3 levels deep: `href="../../../newsletter.html"`

#### Step 4: Create New Submenu (Advanced)

If you need to create a **new submenu** (not adding to existing), you need to:

1. Add `class="has-sub"` to the parent `<li>`
2. Add the dropdown arrow (handled by CSS automatically)
3. Create the nested `<ul class="sub">` structure

Example:

```html
<li class="has-sub"><a href="programs.html">Programs</a>
  <ul class="sub">
    <li><a href="program1.html">Program 1</a></li>
    <li><a href="program2.html">Program 2</a></li>
  </ul>
</li>
```

---

### Ensuring Navigation Works Across the Site

Navigation consistency is critical for user experience. Follow these steps to ensure navigation works correctly on all pages.

#### Relative Path Rules

The key is understanding **relative paths** based on directory depth:

| Page Location | Path to `index.html` | Path to `aboutus.html` |
|--------------|----------------------|------------------------|
| Root (`index.html`) | `index.html` | `aboutus.html` |
| 1 level (`positions/`) | `../index.html` | `../aboutus.html` |
| 2 levels (`articles/parking/`) | `../../index.html` | `../../aboutus.html` |
| 3 levels (`articles/parking/archive/`) | `../../../index.html` | `../../../aboutus.html` |

#### Step-by-Step Verification Process

**Step 1: Update Navigation Template**

1. Choose a representative page (e.g., root `aboutus.html`)
2. Update the navigation structure
3. Copy the complete `<nav>` block

**Step 2: Apply to All Files**

Use your code editor's find/replace feature:

1. **Find**: The old navigation structure
2. **Replace**: The new navigation structure
3. **Adjust paths** for each directory level

**Step 3: Test Navigation Links**

Manually verify:
- [ ] All top-level links work from root pages
- [ ] All top-level links work from subdirectory pages
- [ ] All submenu links work from root pages
- [ ] All submenu links work from subdirectory pages
- [ ] Dropdown menus appear on hover
- [ ] Links are accessible via keyboard (Tab navigation)

**Step 4: Verify Relative Paths**

For each directory level, check:
- Root pages: `href="page.html"`
- Subdirectory pages: `href="../page.html"`
- Deep subdirectory pages: `href="../../page.html"`

#### Common Mistakes to Avoid

1. **Mixing absolute and relative paths**: Always use relative paths
2. **Forgetting to update subdirectory pages**: They need `../` or `../../`
3. **Inconsistent navigation**: All pages should have identical navigation structure
4. **Missing spacer element**: The `.spacer` class pushes action buttons right
5. **Breaking dropdown structure**: Ensure `class="has-sub"` and nested `<ul class="sub">` are correct

#### Automated Testing Tips

1. **Search for navigation patterns**: Use grep/search to find all `<nav id="topnav">` instances
2. **Check for broken links**: Use a link checker tool after updates
3. **Test responsive behavior**: Verify dropdown menus work on mobile
4. **Verify accessibility**: Test with keyboard navigation and screen readers

#### Template System (Future Enhancement)

Consider creating a navigation template or using a build process to:
- Generate navigation automatically
- Ensure consistency
- Reduce manual updates

For now, manual updates are required, but being systematic will prevent errors.

---

## Responsive Design

### Breakpoints

The site uses media queries for responsive layouts:

1. **Mobile**: Default (< 640px)
   - Single column layouts
   - Stacked navigation elements
   - Full-width images

2. **Tablet**: 640px - 1000px
   - 2-column grid for cards
   - Adjusted font sizes

3. **Desktop**: 1000px+
   - 3-column grid for cards
   - Larger font sizes in header
   - Optimal spacing

### Responsive Patterns

**Grid System**:
```css
.grid {
  grid-template-columns: repeat(3, minmax(0, 1fr)); /* Desktop */
}
@media(max-width:1000px) {
  .grid { grid-template-columns: 1fr 1fr; } /* Tablet */
}
@media(max-width:640px) {
  .grid { grid-template-columns: 1fr; } /* Mobile */
}
```

**Images**:
- `max-width: 100%` ensures images scale
- `height: auto` maintains aspect ratio
- Responsive image sizing via CSS

---


### Requirements

- All navigation links use relative paths
- CSS file referenced correctly from all directories
- Images use relative paths from page location
- No absolute system paths

### Pre-Deployment Checklist

- ✅ `index.html` exists (homepage)
- ✅ All pages reference `MABA-modern.css`
- ✅ Navigation links point to `index.html` 
- ✅ All images have alt text
- ✅ Viewport meta tag present on all pages
- ✅ Footer consistent across all pages

---

## Maintenance & Updates

### Adding New Pages

1. **Create HTML file** using the standard template structure or Templates/template_no_sidebar.html
2. **Include navigation** (copy from existing page, adjust paths)
3. **Wrap content** in `<main class="container"><section class="about-page-section">`
4. **Add to navigation menu** if it should appear in main nav
5. **Test relative paths** (especially CSS and image references)

### Modifying Styles

**To change site-wide colors**:
1. Open `MABA-modern.css`
2. Update variables in `:root` section (lines 6-15)
3. Changes apply automatically to entire site

**To add new components**:
1. Add CSS rules in appropriate section
2. Use existing variables for consistency
3. Test responsive behavior at all breakpoints

### Updating Navigation

Navigation structure is in each HTML file. To add a new top-level menu item:

1. Add `<li>` to `<ul class="menu">` in all pages
2. For submenus, add `class="has-sub"` and nested `<ul class="sub">`
3. Update relative paths for subdirectory pages

### Image Guidelines

- **Format**: Use optimized JPG or PNG
- **Naming**: Descriptive names (e.g., `transit2020_bussystem.png`)
- **Alt Text**: Always include descriptive alt attribute
- **Size**: Optimize for web (max 1200px width recommended)

### Content Updates

**Article Formatting**:
- Author/publication/date in `<h4>` tags with bold
- Body text in `<p>` tags (not bold)
- Line break between date and body text

**Position Statements**:
- Main heading: `<h2>` centered
- PDF links: Centered below heading
- Body text: Standard paragraph styling

---

## SEO & Geo-Optimization

### What We've Implemented

All pages now include essential SEO meta tags:

**Essential Meta Tags** (Required for new pages):
- `meta name="description"` - Unique 150-160 character description
- `meta name="keywords"` - Relevant keywords (Madison bus, public transit, etc.)
- `meta name="geo.region"` - `US-WI`
- `meta name="geo.placename"` - `Madison`
- `meta name="geo.position"` - `43.0731;-89.4012`
- `link rel="canonical"` - Canonical URL for the page
- `lang="en"` attribute on `<html>` tag

**Social Media Tags** (Open Graph & Twitter):
- Open Graph tags for Facebook/LinkedIn sharing
- Twitter Card tags for better Twitter previews
- All use the MABA logo as the default image

**Structured Data**:
- Organization schema on homepage (`index.html`)
- Article schema on blog posts with publication dates and author names

**Technical SEO**:
- Enhanced title tags: `[Page Title] | Madison Area Bus Advocates`
- `robots.txt` file for search engine crawling
- `sitemap.xml` with all HTML pages

### What's Important for New Pages

When creating new pages, **always include**:

1. **Meta description** - Unique description (150-160 chars)
2. **Title tag** - Format: `[Page Title] | Madison Area Bus Advocates`
3. **Canonical URL** - Absolute URL: `https://www.busadvocates.org/[page.html]`
4. **Geo-location tags** - Copy from existing pages
5. **Open Graph tags** - Update URL and title/description
6. **Twitter Card tags** - Update URL and title/description
7. **lang="en"** - On the `<html>` tag

**Example for new page**:
```html
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <meta name="description" content="[Unique description]"/>
  <meta name="keywords" content="[Keywords]"/>
  <meta name="geo.region" content="US-WI"/>
  <meta name="geo.placename" content="Madison"/>
  <meta name="geo.position" content="43.0731;-89.4012"/>
  <link rel="canonical" href="https://www.busadvocates.org/new-page.html"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://www.busadvocates.org/new-page.html"/>
  <meta property="og:title" content="New Page | Madison Area Bus Advocates"/>
  <meta property="og:description" content="[Description]"/>
  <meta property="og:image" content="https://www.busadvocates.org/Images/MABAlogo.png"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="New Page | Madison Area Bus Advocates"/>
  <meta name="twitter:description" content="[Description]"/>
  <title>New Page | Madison Area Bus Advocates</title>
</head>
```

### Future Enhancements (Optional)

- **Article schema** for blog posts (already done for all blog posts)
- **Image alt text optimization** - Ensure all images have descriptive alt text
- **Internal linking** - Link related pages together
- **Update sitemap.xml** when adding new pages
- **Monitor Google Search Console** for indexing and performance

### Current Status

✅ **43 blog posts** - All have article schema with dates and authors  
✅ **22 position statements** - All have meta tags  
✅ **All main pages** - Homepage, About, Events, Articles, Blog, Links, etc.  
✅ **Organization schema** - On homepage  
✅ **robots.txt** and **sitemap.xml** - Created and configured

---

## File Organization

### Active Files (Deployed)
- All `.html` files in root and subdirectories
- `MABA-modern.css`
- `Images/` directory
- Content directories (`articles/`, `blog/`, `positions/`, etc.)

### Archive Files (Not Deployed)
- `python/` directory: Python formatting scripts
- `index_pages/` directory: Old homepage versions
- `MABA-index.html`: Original homepage backup

---

## Browser Compatibility

The site is designed for modern browsers:

- **Chrome/Edge**: ✅ Full support
- **Firefox**: ✅ Full support
- **Safari**: ✅ Full support
- **Mobile browsers**: ✅ Responsive design tested

**CSS Features Used**:
- CSS Grid
- CSS Variables (Custom Properties)
- Flexbox
- `:target` pseudo-class (lightbox)
- `position: sticky`

---

## Performance Considerations

### Optimization

- **Single CSS file**: Reduces HTTP requests
- **CSS Variables**: Minimal file size impact
- **No JavaScript**: Faster page loads
- **Responsive images**: Proper sizing prevents wasted bandwidth

### Loading Strategy

- CSS loaded in `<head>` (render-blocking, but small file)
- Images lazy-loaded via `max-width: 100%`
- Fonts loaded from Google Fonts CDN

---

## Security & Best Practices

### HTML Security

- No inline JavaScript (XSS protection)
- External links use `target="_blank"` when appropriate
- No user input forms (no SQL injection risk)

### Content Management

- All content is static HTML
- No server-side processing
- Safe for GitHub Pages hosting

---

## Troubleshooting

### Common Issues

**Navigation not showing**:
- Check that `<nav id="topnav">` exists
- Verify CSS file path is correct
- Ensure `body.sticky` class is present

**Styles not applying**:
- Check CSS file path (relative to page location)
- Verify file is named `MABA-modern.css`
- Clear browser cache

**Links broken**:
- Verify relative path depth (`../` for each directory level)
- Check file exists at target location
- Use `index.html` 

**Images not displaying**:
- Check image path relative to page location
- Verify image file exists
- Check file permissions

---

## Contact & Support

For technical questions or updates:
- Review this documentation
- Check existing pages for pattern examples
- Test changes locally before deploying
- email julia.tanenbaum@gmail.com

---

## Version History

- **Current Version**: Modern responsive redesign
- **CSS File**: `MABA-modern.css` (295 lines)
- **Total Pages**: ~755 HTML files

---

*Last Updated: November 2025*

