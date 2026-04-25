#!/bin/bash

# Apply TresoWealth Design System v1.0 to all content pages

# Find all HTML files except index.html (Framer homepage)
find /Users/akshayrandeva/Treso/website_clone_working -name "*.html" -type f ! -name "index.html" | while read file; do
  echo "Processing: $file"

  # Check if file already has link to styles.css
  if grep -q 'href="styles.css"' "$file"; then
    echo "  ✓ Already has styles.css"
  else
    # Add styles.css link in head section
    sed -i '' 's|</head>|<link rel="stylesheet" href="/styles.css"></head>|' "$file"
    echo "  ✓ Added styles.css link"
  fi

  # Update header background color from #0D9488 to #15D786
  sed -i '' 's/background: #0D9488/background: #15D786/g' "$file"
  echo "  ✓ Updated header color"

  # Update all instances of #0D9488 to #15D786
  sed -i '' 's/#0D9488/#15D786/g' "$file"
  echo "  ✓ Updated primary color"

  # Update border color from #0D9488 to #15D786
  sed -i '' 's/border-left: 4px solid #15D786/border-left: 4px solid var(--color-primary)/g' "$file"
  echo "  ✓ Updated border colors"

  # Update CTA box background
  sed -i '' 's/background: #e0f2f1/background: rgba(21, 215, 134, 0.1)/g' "$file"
  echo "  ✓ Updated CTA backgrounds"

done

echo ""
echo "✅ Design System v1.0 applied to all content pages"
echo "Total pages updated: $(find /Users/akshayrandeva/Treso/website_clone_working -name "*.html" -type f ! -name "index.html" | wc -l)"
