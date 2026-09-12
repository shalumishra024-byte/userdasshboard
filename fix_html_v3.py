import re

with open('backend/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Force Cache Busting
html = re.sub(r'href="/static/css/style\.css[^"]*"', 'href="/static/css/style.css?v=5"', html)
html = re.sub(r'src="/static/js/app\.js[^"]*"', 'src="/static/js/app.js?v=5"', html)

# 2. Minimalist Professional UI (Calm, User Friendly)
# Header back to white with subtle shadow
html = html.replace('bg-[#0056b3] text-white shadow-md border-b border-[#004085]', 'bg-white shadow-sm border-b border-slate-200 text-slate-800')

# Logo Text
html = html.replace('text-blue-100', 'text-slate-600')
html = html.replace('text-white text-lg font-bold', 'text-[#0056b3] text-lg font-bold')

# Header Tabs
html = html.replace('bg-[#004085] p-0.5 sm:p-1 rounded-xl border border-[#003366]', 'bg-slate-100 p-0.5 sm:p-1 rounded-xl border border-slate-200')
html = html.replace('bg-white text-[#0056b3]', 'bg-white text-slate-800 shadow-sm')
html = html.replace('text-blue-200 hover:text-white', 'text-slate-500 hover:text-slate-800')

# Language Selector
html = html.replace('class="bg-[#004085] border border-[#003366] text-white', 'class="bg-white border border-slate-300 text-slate-700')
html = html.replace('text-blue-200 absolute right-2', 'text-slate-400 absolute right-2')

# SOS Button (Make it minimal but noticeable)
html = html.replace('bg-red-600 hover:bg-red-700 text-white', 'bg-rose-50 text-rose-600 hover:bg-rose-100 border border-rose-200')

# Body background
html = html.replace('bg-[#F8FAFC]', 'bg-[#F9FAFB]')

# Chat Bot Bubble Colors (Less aggressive blue, more calm)
html = html.replace('bg-[#0056b3]', 'bg-[#0056b3]') # Keep AI icon blue
# But maybe we can change the user icon if it was changed
html = html.replace('bg-[#0F2557]', 'bg-slate-700')

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
