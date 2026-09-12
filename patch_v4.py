import re

# 1. Update index.html
with open('backend/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Cache bust
html = html.replace('app.js?v=5', 'app.js?v=6')
html = html.replace('style.css?v=5', 'style.css?v=6')

# Insert Response Length Selector right before the input container
input_container_start = r'<div class="flex items-center space-x-2">'
selector_html = """
              <!-- Response Length Selector -->
              <div class="mb-2 flex justify-end">
                <select id="responseLength" class="text-xs border border-slate-200 bg-slate-50 text-slate-600 rounded-md px-2 py-1 focus:outline-none focus:border-slate-300">
                  <option value="brief">Shorter Response</option>
                  <option value="normal" selected>Normal Response</option>
                  <option value="descriptive">Descriptive Response</option>
                </select>
              </div>
              <div class="flex items-center space-x-2">"""

html = re.sub(re.escape(input_container_start), selector_html, html, count=1)

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update app.js
with open('backend/static/js/app.js', 'r', encoding='utf-8') as f:
    appjs = f.read()

# Update send payload to include response length
send_payload = """  formData.append('channel', 'Web_Chat');
  formData.append('text_content', text);
  
  const responseLength = document.getElementById('responseLength') ? document.getElementById('responseLength').value : 'normal';
  formData.append('response_length', responseLength);"""
appjs = appjs.replace("  formData.append('channel', 'Web_Chat');\n  formData.append('text_content', text);", send_payload)

# Replace the AI avatar in handleCheckinResponse
old_avatar = """<div class="w-7 h-7 rounded-full bg-[#1976D2] flex items-center justify-center text-white flex-shrink-0 text-xs shadow-2xs">
        <i class="fa-solid fa-sparkles"></i>
      </div>"""
new_avatar = """<div class="w-7 h-7 flex-shrink-0">
        <img src="/static/img/ai-avatar.png" alt="AI" class="w-full h-full object-cover rounded-md shadow-sm" />
      </div>"""
appjs = appjs.replace(old_avatar, new_avatar)

with open('backend/static/js/app.js', 'w', encoding='utf-8') as f:
    f.write(appjs)

# 3. Update gemini_service.py
with open('backend/app/services/gemini_service.py', 'r', encoding='utf-8') as f:
    gemini = f.read()

system_prompt_update = """            "7. **Medical Safety Constraint:** NEVER provide medical advice, diagnosis, or mention specific medicines or disease names. Ensure your tone remains comforting but non-medical."
"""
if "Medical Safety Constraint" not in gemini:
    gemini = gemini.replace('"6. Guide them towards coping strategies."', '"6. Guide them towards coping strategies."\n' + system_prompt_update)

with open('backend/app/services/gemini_service.py', 'w', encoding='utf-8') as f:
    f.write(gemini)

