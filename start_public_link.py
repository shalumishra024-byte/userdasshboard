import os
import sys
import time
import socket
import subprocess
import threading

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def print_banner(local_ip, port):
    print("\n" + "=" * 75)
    print(" 🛡️  SAMVEDNA AI (संवेदना) - LIVE SERVER & SHARING LINKS")
    print("=" * 75)
    print(f" 💻 Local Access (This PC):     http://127.0.0.1:{port}")
    print(f" 📱 Mobile / Wi-Fi Access:      http://{local_ip}:{port}")
    print(f" 📚 Swagger API Docs:          http://127.0.0.1:{port}/docs")
    print("=" * 75)
    print(" 🌐 TO SHARE WORLDWIDE VIA FREE PUBLIC HTTPS LINK:")
    print("   Open a new PowerShell terminal and run ONE of the following commands:")
    print("   Option 1 (Pinggy):       ssh -p 443 -R0:localhost:8000 a.pinggy.io")
    print("   Option 2 (Localhost.run): ssh -R 80:localhost:8000 nokey@localhost.run")
    print("   Option 3 (Ngrok):        ngrok http 8000")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    sys.path.insert(0, backend_dir)
    
    local_ip = get_local_ip()
    port = 8000
    print_banner(local_ip, port)
    
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
