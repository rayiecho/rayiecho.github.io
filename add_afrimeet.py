import os

old = '<div class="project-card">\n      <div class="project-card-label">Startup &middot; In Development</div>\n      <div class="project-card-title">AfriMeet</div>\n      <p class="project-card-desc">Africa\'s own video conferencing platform. Built for African internet, priced in African currencies. Replacing Zoom for 500K+ African NGOs.</p>\n      <a href="portfolio.html" class="project-link">Read More &rarr;</a>\n      <div class="project-card-accent"></div>\n    </div>'

new = '<div class="project-card">\n      <div class="project-live-badge">Live</div>\n      <div class="project-card-label">Startup &middot; 2026</div>\n      <div class="project-card-title">AfriMeet</div>\n      <p class="project-card-desc">Africa\'s own video conferencing platform. Built for African internet, priced in African currencies. Replacing Zoom for 500K+ African NGOs. 54 countries. $0 to start.</p>\n      <div class="project-tags"><span class="project-tag">WebRTC</span><span class="project-tag">JavaScript</span><span class="project-tag">Africa-First</span></div>\n      <a href="https://afrimeet-lake.vercel.app" target="_blank" class="project-link">Visit Site &rarr;</a>\n      <div class="project-card-accent"></div>\n    </div>'

files = ['index.html', 'portfolio.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        updated = content.replace(old, new)
        if updated != content:
            with open(f, 'w') as file:
                file.write(updated)
            print(f"✅ Updated {f}")
        else:
            print(f"⏭️ No change: {f}")
