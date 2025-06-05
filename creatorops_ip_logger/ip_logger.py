from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[+] {now} - Visitor IP: {ip}")
    with open("logged_ips.txt", "a") as log:
        log.write(f"[{now}] IP: {ip}\n")
    return '''
        <h1>Welcome to CreatorOps Test Page</h1>
        <p>This IP has been logged ethically for demo/testing purposes.</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
