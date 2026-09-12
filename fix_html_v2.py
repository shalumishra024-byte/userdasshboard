import re

with open('backend/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fonts
html = html.replace('Plus Jakarta Sans', 'Inter')
html = html.replace('"Plus Jakarta Sans", "Noto Sans Devanagari", sans-serif', '"Inter", "Noto Sans Devanagari", sans-serif')

# 2. Header Colors (Mygov.in style)
html = re.sub(r'bg-white/95[^"]*', 'bg-[#0056b3] text-white shadow-md border-b border-[#004085]', html)

# The brand logo text and colors in header
html = html.replace('text-[#0D47A1]', 'text-white')
html = html.replace('text-[#1976D2]', 'text-blue-100')
html = html.replace('bg-gradient-to-br from-[#1976D2]/30 to-[#42A5F5]/10 border border-[#42A5F5]/40 text-[#1976D2]', 'bg-white/20 border border-white/30 text-white')

# Tabs in Header
html = html.replace('bg-white p-0.5 sm:p-1 rounded-xl border border-[#BBDEFB]', 'bg-[#004085] p-0.5 sm:p-1 rounded-xl border border-[#003366]')
html = html.replace('bg-[#1976D2] text-white', 'bg-white text-[#0056b3]') # Active tab
html = html.replace('text-slate-500 hover:text-[#0D47A1]', 'text-blue-200 hover:text-white') # Inactive tab

# Language Selector
html = html.replace('class="bg-white border border-[#BBDEFB] text-[#0D47A1]', 'class="bg-[#004085] border border-[#003366] text-white')
html = html.replace('text-[#1976D2] absolute right-2', 'text-blue-200 absolute right-2')

# Chat Layout sizes
html = html.replace('lg:col-span-5', 'lg:col-span-4')
html = html.replace('lg:col-span-7', 'lg:col-span-8')

# Ensure chat bubble and icons use the standard blue
html = html.replace('bg-[#1976D2]', 'bg-[#0056b3]')
html = html.replace('text-[#1976D2]', 'text-[#0056b3]')

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
