import re

with open('backend/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace colors
html = html.replace('bg-[#0A1B3B]', 'bg-white')
html = html.replace('text-white', 'text-[#0D47A1]') # Wait, this might break a lot of things.

# Let's be more precise
html = re.sub(r'bg-\[\#0A1B3B\]/?\d*', 'bg-[#1565C0]', html) # Navbar
html = html.replace('bg-[#061024]', 'bg-white') # Tabs bg
html = html.replace('border-[#1E3A8A]', 'border-[#BBDEFB]')
html = html.replace('text-[#0F2557]', 'text-[#0D47A1]')
html = html.replace('bg-[#0F2557]', 'bg-[#0D47A1]')
html = html.replace('bg-[#183B88]', 'bg-[#1565C0]')
html = html.replace('text-[#183B88]', 'text-[#1565C0]')

# Replace Robot with Sparkles for Gemini feel
html = html.replace('fa-robot', 'fa-sparkles')

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
