import os

ticker = '''<div class="ticker">
  <div class="ticker-inner">
    <span>Software Engineering</span><span class="ticker-dot">&bull;</span>
    <span>Young Africans Network</span><span class="ticker-dot">&bull;</span>
    <span>AfriMeet</span><span class="ticker-dot">&bull;</span>
    <span>Mastercard Foundation Scholar</span><span class="ticker-dot">&bull;</span>
    <span>ALU Kigali</span><span class="ticker-dot">&bull;</span>
    <span>AI Specialist</span><span class="ticker-dot">&bull;</span>
    <span>Building for Africa</span><span class="ticker-dot">&bull;</span>
    <span>Kisumu &rarr; Kigali</span><span class="ticker-dot">&bull;</span>
    <span>Software Engineering</span><span class="ticker-dot">&bull;</span>
    <span>Young Africans Network</span><span class="ticker-dot">&bull;</span>
    <span>AfriMeet</span><span class="ticker-dot">&bull;</span>
    <span>Mastercard Foundation Scholar</span><span class="ticker-dot">&bull;</span>
    <span>ALU Kigali</span><span class="ticker-dot">&bull;</span>
    <span>AI Specialist</span><span class="ticker-dot">&bull;</span>
    <span>Building for Africa</span><span class="ticker-dot">&bull;</span>
    <span>Kisumu &rarr; Kigali</span><span class="ticker-dot">&bull;</span>
  </div>
</div>'''

pages = {
    'about.html': '<div class="story">',
    'skills.html': '<div class="skills-section">',
    'portfolio.html': '<div class="featured">',
    'contact.html': '<div class="services-strip">',
    'media.html': '<div class="media',
}

for f, marker in pages.items():
    with open(f, 'r') as file:
        content = file.read()
    if '<div class="ticker">' not in content:
        content = content.replace(marker, ticker + '\n' + marker, 1)
        with open(f, 'w') as file:
            file.write(content)
        print(f"✅ Ticker inserted in {f}")
    else:
        print(f"⏭️ Already has ticker: {f}")
