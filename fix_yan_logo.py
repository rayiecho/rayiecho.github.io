with open('portfolio.html', 'r') as f:
    content = f.read()

old = '''    <div class="featured-visual">
      <div class="featured-visual-bg"></div>
      <div class="featured-visual-text">
        <div class="featured-visual-title">YAN</div>
        <div class="featured-visual-sub">youngafricansnetwork.org</div>
      </div>
    </div>'''

new = '''    <div class="featured-visual">
      <div class="featured-visual-bg"></div>
      <div class="featured-visual-text">
        <img src="https://youngafricansnetwork.org/images/logo.jpeg" alt="Young Africans Network" style="width:140px;height:140px;border-radius:50%;object-fit:cover;border:3px solid rgba(255,255,255,0.2);margin-bottom:1rem;">
        <div class="featured-visual-sub">youngafricansnetwork.org</div>
      </div>
    </div>'''

updated = content.replace(old, new)

with open('portfolio.html', 'w') as f:
    f.write(updated)

print("✅ YAN logo added to portfolio.html")
