import os

ticker_html = '''
<div class="ticker">
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

ticker_css = '''
    .ticker {
      background: var(--burgundy);
      padding: 0.85rem 0;
      overflow: hidden; white-space: nowrap;
      border-top: 1px solid rgba(255,255,255,0.05);
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .ticker-inner {
      display: inline-block;
      animation: ticker 30s linear infinite;
    }
    .ticker-inner span {
      font-size: 0.72rem; font-weight: 600;
      letter-spacing: 3px; text-transform: uppercase;
      color: #F4F1E8;
      padding: 0 2.5rem;
    }
    .ticker-dot {
      color: #C0392B; font-size: 0.5rem;
      vertical-align: middle;
    }
    @keyframes ticker { from { transform: translateX(0); } to { transform: translateX(-50%); } }'''

files = ['about.html', 'skills.html', 'portfolio.html', 'contact.html', 'media.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        if 'ticker' not in content:
            # Add CSS before </style>
            content = content.replace('</style>', ticker_css + '\n  </style>', 1)
            # Add ticker after <nav>...</nav>
            content = content.replace('</nav>', '</nav>' + ticker_html, 1)
            with open(f, 'w') as file:
                file.write(content)
            print(f"✅ Added ticker to {f}")
        else:
            print(f"⏭️ Already has ticker: {f}")
