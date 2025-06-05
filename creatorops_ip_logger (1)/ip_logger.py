from flask import Flask, request
from datetime import datetime
import requests

app = Flask(__name__)

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()
        country = data.get("country", "Unknown")
        region = data.get("region", "Unknown")
        city = data.get("city", "Unknown")
        return f"{city}, {region}, {country}"
    except Exception:
        return "Location lookup failed"

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    location = get_ip_info(ip)
    log_entry = f"[{now}] IP: {ip} - Location: {location}"
    print(f"[+] {log_entry}")
    with open("logged_ips.txt", "a") as log:
        log.write(log_entry + "\n")
    return '''
        <h1>Welcome to CreatorOps Test Page</h1>
        <p>Your IP has been logged ethically for demo/testing purposes.</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
