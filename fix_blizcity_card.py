with open('portfolio.html', 'r') as f:
    content = f.read()

old = '''    <div class="project-card">
      <div class="project-num">02</div>
      <div class="project-card-category">Web Development &middot; 2026</div>
      <div class="project-card-title">Blizcity Music Platform</div>
      <p class="project-card-desc">Full multi-page music label website for an African music platform. Features music catalogue, artist gallery, fan message board and contact system. Built with HTML, CSS and JavaScript using AI-assisted development.</p>
      <div class="project-tags">
        <span class="project-tag">HTML</span>
        <span class="project-tag">CSS</span>
        <span class="project-tag">JavaScript</span>
        <span class="project-tag">Multi-Page</span>
      </div>
      <a href="https://rayiecho.github.io/blizcity/" target="_blank" class="project-link">View Live Site&rarr;</a>
      <div class="project-card-accent"></div>
    </div>'''

new = '''    <div class="project-card">
      <div class="project-num">02</div>
      <img src="https://moonkhidmusic.com/images/poster.jpg" alt="MoonkhidMusic" style="width:100%;height:160px;object-fit:cover;border-radius:4px;margin-bottom:1rem;">
      <div class="project-card-category">Web Development &middot; 2026</div>
      <div class="project-card-title">Moonkhid Music Platform</div>
      <p class="project-card-desc">Full multi-page music label website for MoonkhidMusic — an Afrobeats & Afropop artist from Benin City, Nigeria. Features music catalogue, artist gallery, fan message board and contact system.</p>
      <div class="project-tags">
        <span class="project-tag">HTML</span>
        <span class="project-tag">CSS</span>
        <span class="project-tag">JavaScript</span>
        <span class="project-tag">Multi-Page</span>
      </div>
      <a href="https://moonkhidmusic.com" target="_blank" class="project-link">View Live Site &rarr;</a>
      <div class="project-card-accent"></div>
    </div>'''

updated = content.replace(old, new)

with open('portfolio.html', 'w') as f:
    f.write(updated)

print("✅ Moonkhid Music card updated in portfolio.html")
