🚀 DevOps Microservices Platform
HTTP → HTTPS with Apache Reverse Proxy on AWS EC2
📌 Project Overview

This repository demonstrates a production-style DevOps microservices platform deployed on AWS EC2:

✔ Microservices in Python (Flask)
✔ Apache as a reverse proxy
✔ Subdomain routing for services
✔ HTTPS enabled via Let’s Encrypt / Certbot
✔ Clean HTTP → HTTPS redirection

The platform is designed to reflect real-world tasks that DevOps engineers handle—secure traffic routing, SSL termination, and scalable service isolation.

🧠 High-Level Architecture
User Browser
     |
     | HTTPS (443)
     v
Apache Reverse Proxy (AWS EC2)
     |
     |– aditechsphere.publicvm.com
     |     → Homepage Service (127.0.0.1:5000)
     |
     |– microservice1.aditechsphere.publicvm.com
     |     → Orders Service (127.0.0.1:5001)
     |
     |– microservice2.aditechsphere.publicvm.com
           → Payments Service (127.0.0.1:5002)

🧩 Project Components
Service	Description	Local Port
Homepage Service	Main dashboard	📍 5000
Orders Service	Orders microservice	📍 5001
Payments Service	Payments microservice	📍 5002
🚀 Tech Stack

Python 3 & Flask

Apache HTTP Server

AWS EC2 (Ubuntu)

DNS Subdomains

Let’s Encrypt + Certbot

Reverse Proxy & SSL Termination

📂 Repository Structure
microservices-app/
│
├── homepage/
│   └── app.py
├── microservice1/
│   └── app.py
├── microservice2/
│   └── app.py
└── README.md

🌐 Live Domain Mapping
Domain	Service
aditechsphere.publicvm.com	Homepage
microservice1.aditechsphere.publicvm.com	Orders Service
microservice2.aditechsphere.publicvm.com	Payments Service

All HTTP requests are redirected permanently to HTTPS.

🛠️ Deployment Guide
1️⃣ Launch EC2 Instance

✔ Ubuntu Server
✔ Open Inbound Ports:

80 (HTTP)

443 (HTTPS)

✔ Assign Elastic IP (recommended)

2️⃣ Install Packages
sudo apt update
sudo apt install python3 python3-pip python3-venv apache2 -y


Enable required Apache modules:

sudo a2enmod proxy proxy_http headers rewrite ssl
sudo systemctl restart apache2

3️⃣ Setup Python Environment
mkdir ~/microservices-app
cd ~/microservices-app
python3 -m venv venv
source venv/bin/activate
pip install flask

4️⃣ Run Each Flask Microservice
# Homepage
python homepage/app.py

# Orders Service
python microservice1/app.py

# Payments Service
python microservice2/app.py

5️⃣ DNS Configuration

Add DNS A records:

aditechsphere.publicvm.com              → EC2_IP
microservice1.aditechsphere.publicvm.com → EC2_IP
microservice2.aditechsphere.publicvm.com → EC2_IP

6️⃣ Apache Reverse Proxy (HTTP → HTTPS)
Homepage – HTTP Config
<VirtualHost *:80>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

Orders – HTTP Config
<VirtualHost *:80>
    ServerName microservice1.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5001/
    ProxyPassReverse / http://127.0.0.1:5001/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

Payments – HTTP Config
<VirtualHost *:80>
    ServerName microservice2.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5002/
    ProxyPassReverse / http://127.0.0.1:5002/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>


Enable sites & reload Apache:

sudo a2ensite *.conf
sudo apachectl configtest
sudo systemctl reload apache2

🔐 Enable HTTPS with Let’s Encrypt
Install Certbot
sudo apt install certbot python3-certbot-apache -y

Run Certbot
sudo certbot --apache -d aditechsphere.publicvm.com


This will:
✔ Validate DNS
✔ Issue SSL cert
✔ Configure Apache SSL settings
✔ Set up auto-renewal

Example HTTPS VirtualHost
<VirtualHost *:443>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    SSLCertificateFile /etc/letsencrypt/live/aditechsphere.publicvm.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/aditechsphere.publicvm.com/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>


Repeat for other subdomains.

🔁 HTTP & HTTPS Flow
Flask (internal HTTP) 
    ↓
Apache (SSL Termination)
    ↓
HTTPS Served to Browser


✔ Flask stays on HTTP internally
✔ SSL is terminated at Apache
✔ HTTP requests auto-redirect to HTTPS

🔒 Security Best Practices

✔ Bind Flask apps to localhost
✔ Firewall block internal ports
✔ Use strong SSL configuration
✔ Certbot auto-renews certificates
✔ Apache as single trusted entry point

🌟 Why This Project Matters for DevOps

Real-world reverse proxy implementation

HTTPS enablement without downtime

Integration of DNS, Apache, certbot, and EC2

Microservices with isolated service routing

Can be extended to Docker, Kubernetes, ALB, etc.
