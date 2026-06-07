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
    'about.html': '</div>\n</div>\n<div class="story">',
    'skills.html': '</div>\n</div>\n<div class="skills-section">',
    'portfolio.html': '</div>\n</div>\n<div class="featured">',
    'contact.html': '</div>\n</div>\n<div class="contact',
    'media.html': '</div>\n</div>\n<div class="media',
}

import re, os

for f, marker in pages.items():
    with open(f, 'r') as file:
        content = file.read()
    # Remove old ticker first
    content = re.sub(r'<div class="ticker">.*?</div>\n</div>', '', content, flags=re.DOTALL)
    # Insert ticker after page-hero closing
    content = content.replace(marker, '</div>\n</div>\n' + ticker + '\n' + marker.split('\n')[-1], 1)
    with open(f, 'w') as file:
        file.write(content)
    print(f"✅ Fixed {f}")
