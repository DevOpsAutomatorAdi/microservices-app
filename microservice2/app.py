from flask import Flask, render_template_string
import socket
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Microservice 2 | Payments Service</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: "Segoe UI", Roboto, Arial, sans-serif;
            background: #f8fafc;
            color: #1f2937;
        }

        header {
            background: #020617;
            color: white;
            padding: 20px 40px;
        }

        header h1 {
            margin: 0;
            font-size: 24px;
        }

        header p {
            margin-top: 6px;
            color: #c7d2fe;
            font-size: 14px;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            padding: 40px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }

        .card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 8px 18px rgba(0,0,0,0.08);
        }

        .card h3 {
            margin-top: 0;
            color: #7c3aed;
        }

        .status {
            display: inline-block;
            padding: 6px 12px;
            font-size: 13px;
            border-radius: 20px;
            background: #dcfce7;
            color: #166534;
            font-weight: 500;
        }

        .info {
            font-size: 14px;
            color: #4b5563;
            line-height: 1.6;
        }

        .btn {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 18px;
            background: #7c3aed;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
        }

        .btn:hover {
            background: #6d28d9;
        }

        footer {
            margin-top: 50px;
            background: #020617;
            color: #cbd5e1;
            text-align: center;
            padding: 18px;
            font-size: 13px;
        }

        footer span {
            color: white;
        }
    </style>
</head>

<body>

<header>
    <h1>💳 Payments Microservice</h1>
    <p>Secure payment processing | Flask | Apache Reverse Proxy</p>
</header>

<div class="container">

    <div class="grid">

        <div class="card">
            <h3>Service Overview</h3>
            <p class="info">
                This microservice handles payment processing logic.
                It is isolated, independently deployable, and scalable.
            </p>
            <span class="status">Service Healthy</span>
        </div>

        <div class="card">
            <h3>Runtime Information</h3>
            <p class="info">
                <strong>Service Name:</strong> payments-service<br>
                <strong>Environment:</strong> Production<br>
                <strong>Host:</strong> {{ hostname }}<br>
                <strong>Version:</strong> v1.0.0<br>
                <strong>Last Checked:</strong> {{ time }}
            </p>
        </div>

        <div class="card">
            <h3>DevOps Details</h3>
            <p class="info">
                • Reverse proxied using Apache<br>
                • Designed for container orchestration<br>
                • Health endpoint enabled<br>
                • CI/CD & monitoring ready
            </p>
        </div>

    </div>

    <a class="btn" href="http://aditechsphere.publicvm.com/">⬅ Back to Platform Dashboard</a>

</div>

<footer>
    <p>
        © 2026 <span>AdiTechSphere</span> |
        DevOps Microservices Project
    </p>
</footer>

</body>
</html>
"""

@app.route("/")
def service2():
    return render_template_string(
        HTML,
        hostname=socket.gethostname(),
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

# ✅ DevOps Health Endpoint
@app.route("/health")
def health():
    return {
        "service": "payments-service",
        "status": "UP",
        "version": "v1.0.0"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

