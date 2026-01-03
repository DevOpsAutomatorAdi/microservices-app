from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AdiTechSphere | DevOps Microservices Platform</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: "Segoe UI", Roboto, Arial, sans-serif;
            background: #f4f6f9;
            color: #333;
        }

        header {
            background: #1f2937;
            color: #fff;
            padding: 20px 40px;
        }

        header h1 {
            margin: 0;
            font-size: 26px;
        }

        header p {
            margin-top: 5px;
            color: #cbd5e1;
        }

        .container {
            padding: 40px;
            max-width: 1100px;
            margin: auto;
        }

        .section-title {
            font-size: 22px;
            margin-bottom: 20px;
            color: #111827;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }

        .card {
            background: #ffffff;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
            transition: transform 0.2s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card h3 {
            margin-top: 0;
            color: #1e40af;
        }

        .card p {
            font-size: 14px;
            color: #4b5563;
        }

        .status {
            display: inline-block;
            margin-top: 10px;
            padding: 4px 10px;
            font-size: 12px;
            border-radius: 20px;
            background: #dcfce7;
            color: #166534;
        }

        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 18px;
            background: #2563eb;
            color: #fff;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
        }

        .btn:hover {
            background: #1d4ed8;
        }

        footer {
            margin-top: 60px;
            background: #1f2937;
            color: #cbd5e1;
            padding: 20px;
            text-align: center;
            font-size: 13px;
        }

        footer span {
            color: #fff;
        }
    </style>
</head>

<body>

<header>
    <h1>AdiTechSphere</h1>
    <p>DevOps Microservices Platform • Apache • Flask • AWS EC2</p>
</header>

<div class="container">
    <div class="section-title">Available Services</div>

    <div class="services">

        <div class="card">
            <h3>🏠 Homepage Service</h3>
            <p>Central gateway service running behind Apache reverse proxy. Acts as an entry point to all internal microservices.</p>
            <div class="status">Running</div><br>
            <a class="btn" href="/">View Service</a>
        </div>

        <div class="card">
            <h3>🛒 Microservice 1</h3>
            <p>Independent backend service deployed as a standalone microservice. Accessible via subdomain routing.</p>
            <div class="status">Running</div><br>
            <a class="btn" href="http://microservice2.aditechsphere.publicvm.com/">Open Service</a>
        </div>

        <div class="card">
            <h3>💳 Microservice 2</h3>
            <p>Second microservice demonstrating service isolation, scalability, and independent deployment.</p>
            <div class="status">Running</div><br>
            <a class="btn" href="http://microservice2.aditechsphere.publicvm.com/">Open Service</a>
        </div>

    </div>
</div>

<footer>
    <p>
        Built by <span>Aditya Sirsam</span> |
        DevOps Engineer Project |
        Flask • Apache • Linux • AWS
    </p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

