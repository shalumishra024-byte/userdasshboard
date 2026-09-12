import os
import sys
import time
import re
import subprocess
import webbrowser
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUDFLARED = r'C:\Users\ACER\.gemini\antigravity\scratch\cloudflared.exe'
SERVER_SCRIPT = os.path.join(BASE_DIR, 'run_server.py')

print('=' * 75)
print('       SAMVEDNA AI (संवेदना) - STARTING LIVE SYSTEM & GLOBAL LINK')
print('=' * 75)

# 1. Start backend server if not running
try:
    urllib.request.urlopen('http://127.0.0.1:8000/docs', timeout=2)
    print(' [OK] Backend server is already running on port 8000.')
except Exception:
    print(' [*] Launching backend server on port 8000...')
    subprocess.Popen([sys.executable, SERVER_SCRIPT], cwd=BASE_DIR, creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(3)

# 2. Start Cloudflare Tunnel
print(' [*] Establishing global public tunnel...')
tunnel_proc = subprocess.Popen(
    [CLOUDFLARED, 'tunnel', '--url', 'http://127.0.0.1:8000'],
    cwd=BASE_DIR,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1,
    encoding='utf-8',
    errors='ignore'
)

public_url = None
start_time = time.time()
while time.time() - start_time < 30:
    line = tunnel_proc.stdout.readline()
    if not line:
        continue
    match = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
    if match:
        public_url = match.group(0)
        break

if public_url:
    print('\n' + '=' * 75)
    print('  SUCCESS! SAMVEDNA AI IS NOW LIVE WORLDWIDE')
    print('=' * 75)
    print(f'  PUBLIC HTTPS URL:  {public_url}')
    print(f'  LOCAL ACCESS:      http://127.0.0.1:8000')
    print('=' * 75)
    print('  You can copy and open this link on ANY phone or laptop anywhere in the world!')
    print('  (Keep this window open while using the website)')
    print('=' * 75 + '\n')
    webbrowser.open(public_url)
    try:
        tunnel_proc.wait()
    except KeyboardInterrupt:
        print('\nShutting down tunnel...')
        tunnel_proc.terminate()
else:
    print(' [!] Could not detect tunnel URL automatically. Please check your internet connection.')
