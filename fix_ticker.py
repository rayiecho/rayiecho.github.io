import os

old = '.ticker-inner span {\n      font-size: 0.72rem; font-weight: 600;\n      letter-spacing: 3px; text-transform: uppercase;\n      color: #1A3320;\n      padding: 0 2.5rem;\n    }'
new = '.ticker-inner span {\n      font-size: 0.72rem; font-weight: 600;\n      letter-spacing: 3px; text-transform: uppercase;\n      color: #F4F1E8;\n      padding: 0 2.5rem;\n    }'

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    updated = content.replace(old, new)
    if updated != content:
        with open(f, 'w') as file:
            file.write(updated)
        print(f"✅ Fixed {f}")
    else:
        print(f"⏭️ No change: {f}")
