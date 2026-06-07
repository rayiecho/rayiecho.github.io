import os

old = '<link rel="icon" type="image/jpeg" href="images/hero1.jpeg">'
new = '<link rel="icon" type="image/jpeg" href="https://rayiecho.github.io/images/hero1.jpeg">'

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    updated = content.replace(old, new)
    with open(f, 'w') as file:
        file.write(updated)
    print(f"✅ Updated {f}")
