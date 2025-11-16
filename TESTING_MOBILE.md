# Mobile Testing Guide

## How to Test the Site Locally in Chrome Before Pushing to GitHub

### Step 1: Start Local Server

Open Terminal and navigate to the staging directory:

```bash
cd /Users/julia/Desktop/susansites/MABA/staginghomepagesusanversion
python3 -m http.server 8000
```

The server will start and display: `Serving HTTP on :: port 8000...`

**Keep this terminal window open** - the server needs to keep running.

### Step 2: Open in Chrome

1. Open Google Chrome
2. Navigate to: `http://localhost:8000`
3. You should see the MABA homepage

### Step 3: Test Mobile Responsiveness

1. **Open Chrome DevTools:**
   - Press `Cmd + Option + I` (Mac) or `F12` (Windows/Linux)
   - Or: Right-click → "Inspect"

2. **Enable Device Toolbar:**
   - Press `Cmd + Shift + M` (Mac) or click the device icon in the toolbar
   - This simulates mobile devices

3. **Test Different Screen Sizes:**
   - Click the device dropdown (top-left of DevTools)
   - Select different devices:
     - **iPhone SE** (375px) - Smallest modern phone
     - **iPhone 12/13/14** (390px) - Standard phone
     - **iPhone 14 Pro Max** (430px) - Large phone
     - **Samsung Galaxy S20** (360px) - Android phone
     - **iPad** (768px) - Tablet
     - **iPad Pro** (1024px) - Large tablet
     - **Desktop** (1280px+) - Full desktop

4. **What to Check:**
   - ✅ Navigation menu stacks vertically on mobile (< 720px)
   - ✅ "Join", "Membership", "Donate" buttons are full-width and visible
   - ✅ No horizontal scrolling
   - ✅ Text is readable (not too small)
   - ✅ Images scale properly
   - ✅ Cards stack in single column on mobile
   - ✅ Sidebar (on article pages) appears above content on mobile
   - ✅ Dropdown menus work on mobile
   - ✅ Footer is readable

### Step 4: Test on Your Phone

1. **Find your Mac's IP address:**
   ```bash
   ipconfig getifaddr en0
   ```
   (Or check System Preferences → Network)

2. **On your phone (same Wi-Fi network):**
   - Open browser
   - Go to: `http://[YOUR_IP]:8000`
   - Example: `http://192.168.1.100:8000`

3. **Test navigation and all pages:**
   - Homepage
   - About Us
   - Articles (with sidebar)
   - Blog posts
   - Position statements
   - All navigation links

### Step 5: Stop the Server

When done testing, go back to Terminal and press `Ctrl + C` to stop the server.

---

## What Was Fixed

### Navigation
- ✅ CTA buttons (Join, Membership, Donate) now stack full-width on mobile
- ✅ Navigation menu stacks vertically below 720px
- ✅ Dropdown menus work on mobile (expand inline)

### Typography
- ✅ Headings scale down on mobile (h1: 1.8em → 2.4em)
- ✅ Tagline scales (18px → 22px)
- ✅ Recent blog text wraps properly

### Layout
- ✅ Container padding reduced on mobile (16px vs 20px)
- ✅ Sidebar removes min-width constraint on mobile
- ✅ Floated images clear on mobile
- ✅ Cards stack in single column on mobile

### Components
- ✅ Lightbox padding adjusted for mobile
- ✅ Footer font size scales
- ✅ Tables become card-style on mobile
- ✅ Partner logos remain responsive

### Prevention
- ✅ Horizontal scroll prevented
- ✅ All images/videos constrained to viewport width

---

## Breakpoints Used

- **Mobile**: < 640px (single column, stacked navigation)
- **Tablet**: 640px - 1000px (2-column grids, wrapped navigation)
- **Desktop**: 1000px+ (3-column grids, full navigation)

---

## Quick Test Checklist

Before pushing to GitHub, verify:

- [ ] Homepage loads correctly on mobile
- [ ] Navigation menu is accessible (no horizontal scroll)
- [ ] CTA buttons visible and clickable
- [ ] About Us page readable
- [ ] Articles page sidebar stacks on mobile
- [ ] Blog posts readable
- [ ] Position statements readable
- [ ] No horizontal scrolling anywhere
- [ ] Images don't overflow
- [ ] Footer is readable

---

## Troubleshooting

**Server won't start:**
- Check if port 8000 is in use: `lsof -i :8000`
- Try a different port: `python3 -m http.server 8080`

**Can't access from phone:**
- Ensure phone and Mac are on same Wi-Fi
- Check Mac firewall settings
- Try using `0.0.0.0` instead: `python3 -m http.server 8000 --bind 0.0.0.0`

**Styles not updating:**
- Hard refresh: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows)
- Clear browser cache
- Check CSS file path is correct

