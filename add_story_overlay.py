with open('about.html', 'r') as f:
    content = f.read()

old = '<div class="timeline-photo"><div class="timeline-photo-placeholder"></div></div>'

new = '''<div class="timeline-photo" style="position:relative;">
  <div style="width:100%;height:100%;min-height:500px;background:url(\'images/hero2.jpeg\') center top / cover no-repeat;position:relative;border-radius:4px;overflow:hidden;">
    <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(5,15,8,0.97) 0%, rgba(5,15,8,0.75) 50%, rgba(5,15,8,0.3) 100%);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;padding:2.5rem;z-index:2;">
      <div style="font-size:0.68rem;letter-spacing:3px;text-transform:uppercase;color:#D4A84B;font-weight:600;margin-bottom:1rem;">My Journey</div>
      <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;line-height:1.85;color:rgba(244,241,232,0.92);margin-bottom:1.5rem;">&ldquo;I was born in Kisumu, Kenya &mdash; to Erick N. Ayiecho, a man of boundless optimism, and Elizabeth Akinyi Ayiecho, a woman of quiet, unshakeable strength. Despite circumstances that were never quite in our favour, they never stopped believing. And so, neither did I.&rdquo;</p>
      <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;line-height:1.85;color:rgba(244,241,232,0.92);margin-bottom:1.5rem;">&ldquo;At Class 3, I was already dismantling old phones &mdash; not out of mischief, but out of hunger to understand. That curiosity has never left me. From St. Joseph Ng&rsquo;ula Primary School, I scored 350 out of 500. From that muddy school, it was enough.&rdquo;</p>
      <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;line-height:1.85;color:rgba(244,241,232,0.92);margin-bottom:1.5rem;">&ldquo;Secondary school almost did not happen. Mr. Ayubu Migwala chose to invest in a boy he did not have to. I finished with a B plain. Then the sponsorship ended. Before that day&rsquo;s sun set, I had raised KES 80,000 from well-wishers and enrolled at Egerton University. No fee paid. No laptop. Just will.&rdquo;</p>
      <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;line-height:1.85;color:rgba(244,241,232,0.92);margin-bottom:1.5rem;">&ldquo;Then in 2025, two full scholarships arrived &mdash; ALU and ALCHE. Africa does not need more potential. It needs solutions. YAN and AfriMeet are mine.&rdquo;</p>
      <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;line-height:1.85;color:rgba(244,241,232,0.92);margin-bottom:1.5rem;">&ldquo;The journey is long. There are thorns everywhere. But thorns do not stop growth &mdash; they only slow it. I am looking forward to a united Africa &mdash; one that owns its own systems, tells its own stories, and builds its own future. We keep pushing. We keep recovering. We keep building.&rdquo;</p>
      <div style="font-size:0.78rem;color:#D4A84B;font-weight:600;letter-spacing:1px;">— Regan Odhiambo Ayiecho, Kisumu &rarr; Kigali</div>
    </div>
  </div>
</div>'''

updated = content.replace(old, new)

with open('about.html', 'w') as f:
    f.write(updated)

print("✅ Story overlay added to about.html")
