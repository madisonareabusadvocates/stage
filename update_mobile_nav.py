#!/usr/bin/env python3
"""
Script to update all HTML files with mobile navigation menu.
Replaces old nav structure with new mobile-friendly hamburger menu.
"""

import os
import re
from pathlib import Path

# Mobile nav template for root-level pages
MOBILE_NAV_ROOT = '''  <!-- Hidden checkbox for mobile menu toggle -->
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
  </div>'''

def count_directory_levels(file_path):
    """Count how many directories deep the file is from project root.

    Example:
      "index.html" -> depth 0
      "positions/ted2025_MABA_Res.html" -> depth 1
      "articles/regionaltransit/region2/index.html" -> depth 2
    """
    parts = Path(file_path).parts
    # depth = number of directories (all parts except the filename)
    depth = max(len(parts) - 1, 0)
    return depth

def adjust_paths(nav_html, depth):
    """Adjust navigation paths based on directory depth."""
    if depth == 0:
        return nav_html  # Root level, no changes needed
    
    # Add ../ for each directory level
    prefix = '../' * depth
    
    # Explicitly update known nav links to avoid double-prefix issues
    replacements = {
        'href="index.html"':            f'href="{prefix}index.html"',
        'href="aboutus.html"':          f'href="{prefix}aboutus.html"',
        'href="events.html"':           f'href="{prefix}events.html"',
        'href="positions.html"':        f'href="{prefix}positions.html"',
        'href="resolutions.html"':      f'href="{prefix}resolutions.html"',
        'href="strategic_plan.html"':   f'href="{prefix}strategic_plan.html"',
        'href="resources.html"':        f'href="{prefix}resources.html"',
        'href="articles.html"':         f'href="{prefix}articles.html"',
        'href="blog.html"':             f'href="{prefix}blog.html"',
        'href="links.html"':            f'href="{prefix}links.html"',
        'href="news.html"':             f'href="{prefix}news.html"',
        'href="volunteer.html"':        f'href="{prefix}volunteer.html"',
        'href="membership.html"':       f'href="{prefix}membership.html"',
        'href="donate.html"':           f'href="{prefix}donate.html"',
        'href="Manifesto/manifesto.html"': f'href="{prefix}Manifesto/manifesto.html"',
    }
    for old, new in replacements.items():
        nav_html = nav_html.replace(old, new)
    
    return nav_html

def extract_old_nav(html_content):
    """Extract the old nav section from HTML."""
    # Pattern to match <nav id="topnav"> ... </nav>
    pattern = r'<nav id="topnav">.*?</nav>'
    match = re.search(pattern, html_content, re.DOTALL)
    return match

def update_file(file_path):
    """Update a single HTML file with mobile navigation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has nav
        if '<nav id="topnav">' not in content:
            print(f"  - No nav found: {file_path}")
            return False
        
        # Calculate directory depth
        depth = count_directory_levels(file_path)
        
        # Get mobile nav with adjusted paths
        mobile_nav = adjust_paths(MOBILE_NAV_ROOT, depth)
        
        # Extract old nav
        old_nav_match = extract_old_nav(content)
        if not old_nav_match:
            print(f"  - Could not extract nav: {file_path}")
            return False
        
        # Replace old nav with new nav
        new_content = content[:old_nav_match.start()] + '<nav id="topnav">\n' + mobile_nav + '\n</nav>' + content[old_nav_match.end():]
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ Updated: {file_path}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files."""
    base_dir = Path('.')
    html_files = list(base_dir.rglob('*.html'))
    
    # Exclude certain directories
    exclude_dirs = {'backups', 'backupsbeforemobile', '__pycache__', '.git'}
    html_files = [f for f in html_files if not any(exclude in str(f) for exclude in exclude_dirs)]
    
    print(f"Found {len(html_files)} HTML files to process...\n")
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        if update_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1
    
    print(f"\n✓ Updated: {updated_count} files")
    print(f"- Skipped: {skipped_count} files")
    print(f"\nDone!")

if __name__ == '__main__':
    main()

