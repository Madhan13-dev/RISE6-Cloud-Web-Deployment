from flask import Flask, jsonify, render_template_string
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RISE 6.0 Cloud App</title>
  <style>
    body{font-family:Arial,sans-serif;background:#f5f7fb;margin:0;color:#172033}
    .wrap{max-width:900px;margin:70px auto;padding:30px}
    .card{background:#fff;border-radius:18px;padding:35px;box-shadow:0 12px 35px rgba(0,0,0,.08)}
    h1{margin-top:0;color:#2457d6}.badge{display:inline-block;padding:8px 12px;border-radius:20px;background:#eaf0ff}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:15px;margin-top:25px}
    .item{padding:18px;background:#f7f8fb;border-radius:12px}
  </style>
</head>
<body>
<div class="wrap"><div class="card">
  <span class="badge">RISE 6.0 • Cloud Computing</span>
  <h1>Industry-Oriented Cloud Web Application</h1>
  <p>This application is deployed on AWS with a load balancer, auto scaling, security controls and monitoring.</p>
  <div class="grid">
    <div class="item"><b>Instance</b><br>{{ hostname }}</div>
    <div class="item"><b>Time (UTC)</b><br>{{ time }}</div>
    <div class="item"><b>Status</b><br>Healthy</div>
  </div>
</div></div>
</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(
        HTML,
        hostname=socket.gethostname(),
        time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.get("/health")
def health():
    return jsonify(status="UP", hostname=socket.gethostname()), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
