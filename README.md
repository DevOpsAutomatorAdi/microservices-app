DevOps Microservices Platform
🔐 HTTP → HTTPS with Apache Reverse Proxy on AWS EC2
✨ What This Project Shows (At a Glance)

✅ Production-style microservices architecture
✅ Apache Reverse Proxy with subdomain routing
✅ HTTP → HTTPS migration using Let’s Encrypt
✅ Secure SSL termination at proxy level
✅ Real DevOps deployment on AWS EC2

🎯 Built to reflect real-world DevOps responsibilities, not just demos.

🧠 Architecture Overview
User Browser
   |
   | HTTPS (443)
   v
Apache Reverse Proxy (AWS EC2)
   |
   ├── aditechsphere.publicvm.com
   |      → Homepage (127.0.0.1:5000)
   |
   ├── microservice1.aditechsphere.publicvm.com
   |      → Orders Service (127.0.0.1:5001)
   |
   └── microservice2.aditechsphere.publicvm.com
          → Payments Service (127.0.0.1:5002)

🧩 Microservices
Service	Purpose	Port
🏠 Homepage	Main dashboard	5000
🛒 Orders	Order management	5001
💳 Payments	Payment processing	5002
🧰 Tech Stack
Layer	Technology
Language	Python 3
Framework	Flask
Web Server	Apache
Security	Let’s Encrypt (Certbot)
Cloud	AWS EC2 (Ubuntu)
Routing	Reverse Proxy + Subdomains
📁 Project Structure
microservices-app/
├── homepage/
│   └── app.py
├── microservice1/
│   └── app.py
├── microservice2/
│   └── app.py
└── README.md

🌐 Live Subdomain Routing
URL	Service
aditechsphere.publicvm.com	Homepage
microservice1.aditechsphere.publicvm.com	Orders
microservice2.aditechsphere.publicvm.com	Payments

🔁 All HTTP traffic → HTTPS automatically

⚙️ Deployment Flow (Simple View)

1️⃣ Launch EC2 (Ubuntu)
2️⃣ Run Flask apps on localhost
3️⃣ Apache routes traffic via subdomains
4️⃣ Certbot enables HTTPS
5️⃣ Apache handles SSL termination

🔐 HTTPS Strategy (Real Production Model)
Browser
  ↓ HTTPS
Apache (SSL Termination)
  ↓ HTTP (internal)
Flask Microservices


✔ Secure external traffic
✔ Internal services remain isolated
✔ Standard enterprise architecture

🔒 Security Highlights

🔐 SSL certificates auto-renewed

🔒 Flask apps bound to 127.0.0.1

🚪 Apache as single public entry point

🔥 Internal ports can be firewalled

🧱 Clear separation of edge & app layer

🌟 Why Recruiters Like This Project

✅ Not a tutorial — real infra setup
✅ Reverse proxy + SSL = core DevOps skill
✅ Subdomain-based microservices
✅ Clean, production-ready documentation
✅ Easily extendable to Docker / Kubernetes / ALB

🚀 Possible Extensions

🐳 Docker & Docker Compose

☸️ Kubernetes (EKS)

🔁 CI/CD (GitHub Actions / Jenkins)

📊 Monitoring (Prometheus + Grafana)

⚖️ Load Balancing with ALB

👨‍💻 Author

Aditya Sirsam
DevOps Engineer | AWS | Linux | Docker | Kubernetes

📌 GitHub: https://github.com/DevOpsAutomatorAdi
