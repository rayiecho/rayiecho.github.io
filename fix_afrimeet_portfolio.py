with open('portfolio.html', 'r') as f:
    content = f.read()

old = '      <span class="coming-badge">In Development</span>\n      <div class="project-card-accent"></div>\n    </div>'
new = '      <a href="https://afrimeet-lake.vercel.app" target="_blank" class="project-link">Visit Site &rarr;</a>\n      <div class="project-card-accent"></div>\n    </div>'

# Also update the category and badge
content = content.replace(
    '<div class="project-card-category">Startup &middot; In Development</div>\n      <div class="project-card-title">AfriMeet</div>',
    '<div class="project-live-badge">Live</div>\n      <div class="project-card-category">Startup &middot; 2026</div>\n      <div class="project-card-title">AfriMeet</div>'
)
content = content.replace(old, new)

with open('portfolio.html', 'w') as f:
    f.write(content)

print("✅ AfriMeet updated in portfolio.html")
