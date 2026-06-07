import os

old = '<a href="index.html" class="nav-logo">Regan Ayiecho</a>'
new = '<a href="index.html" class="nav-logo" style="display:flex;align-items:center;gap:10px;"><img src="images/hero1.jpeg" alt="Regan Ayiecho" style="width:36px;height:36px;border-radius:50%;object-fit:cover;object-position:center 15%;border:2px solid #C0392B;flex-shrink:0;">Regan Ayiecho</a>'

files = ['index.html', 'about.html', 'skills.html', 'portfolio.html', 'contact.html', 'media.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        updated = content.replace(old, new)
        with open(f, 'w') as file:
            file.write(updated)
        print(f"✅ Updated {f}")
    else:
        print(f"⚠️ Not found: {f}")
