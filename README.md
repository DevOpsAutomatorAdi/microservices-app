🚀 DevOps Microservices Platform
HTTP → HTTPS Migration using Apache Reverse Proxy on AWS EC2
📌 Project Overview

This project demonstrates a production-grade DevOps microservices architecture deployed on AWS EC2, using Python (Flask) microservices exposed securely via an Apache Reverse Proxy with HTTPS enabled using Let’s Encrypt.

Each microservice runs independently on internal HTTP ports and is accessed externally through subdomain-based routing. Apache acts as a single secure entry point, handling SSL termination, routing, and redirection.

A core objective of this project is to showcase a real-world HTTP → HTTPS migration, a critical responsibility of DevOps engineers in production environments.

🏗️ Architecture – Logical View
User Browser
     |
     |  HTTPS (443)
     v
Apache Reverse Proxy (AWS EC2)
     |
     |-- aditechsphere.publicvm.com
     |      → Homepage Service (127.0.0.1:5000)
     |
     |-- microservice1.aditechsphere.publicvm.com
     |      → Orders Service (127.0.0.1:5001)
     |
     |-- microservice2.aditechsphere.publicvm.com
            → Payments Service (127.0.0.1:5002)

🧩 Microservices in This Project
Service Name	Description	Internal Port
Homepage Service	Central dashboard / landing page	5000
Orders Service	Independent backend microservice	5001
Payments Service	Independent backend microservice	5002
🚀 Tech Stack

Python 3

Flask

Apache HTTP Server

Reverse Proxy & SSL Termination

AWS EC2 (Ubuntu Linux)

DNS & Subdomain Routing

Let’s Encrypt (Certbot)

📂 Project Structure
microservices-app/
│
├── homepage/
│   └── app.py
│
├── microservice1/
│   └── app.py
│
├── microservice2/
│   └── app.py
│
└── README.md

🌐 Domain Mapping
Public URL	Service
http://aditechsphere.publicvm.com
	Homepage
http://microservice1.aditechsphere.publicvm.com
	Orders Service
http://microservice2.aditechsphere.publicvm.com
	Payments Service

All HTTP traffic is permanently redirected to HTTPS.

🛠️ Step-by-Step Deployment Guide
🔹 Step 1: Launch EC2 Instance

Launch Ubuntu EC2

Allow inbound traffic:

80 (HTTP)

443 (HTTPS)

Attach Elastic IP (recommended for stable DNS)

🔹 Step 2: Install Required Packages
sudo apt update
sudo apt install python3 python3-pip python3-venv apache2 -y


Enable Apache modules:

sudo a2enmod proxy proxy_http headers rewrite
sudo systemctl restart apache2

🔹 Step 3: Setup Python Virtual Environment
mkdir ~/microservices-app
cd ~/microservices-app
python3 -m venv venv
source venv/bin/activate
pip install flask

🔹 Step 4: Run Flask Microservices

Each service runs internally on localhost.

# Homepage
python homepage/app.py

# Orders Service
python microservice1/app.py

# Payments Service
python microservice2/app.py


Internal ports:

127.0.0.1:5000

127.0.0.1:5001

127.0.0.1:5002

🔹 Step 5: Configure DNS

Create A records pointing to the EC2 public IP:

aditechsphere.publicvm.com               → EC2_IP
microservice1.aditechsphere.publicvm.com → EC2_IP
microservice2.aditechsphere.publicvm.com → EC2_IP


Wildcard records can also be used but are not required.

🔄 Apache Reverse Proxy Configuration (HTTP → HTTPS)

Apache exposes each microservice via subdomains and forces HTTPS redirection.

🏠 Homepage – HTTP VirtualHost
<VirtualHost *:80>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

🛒 Orders Service – HTTP VirtualHost
<VirtualHost *:80>
    ServerName microservice1.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5001/
    ProxyPassReverse / http://127.0.0.1:5001/

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

💳 Payments Service – HTTP VirtualHost
<VirtualHost *:80>
    ServerName microservice2.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5002/
    ProxyPassReverse / http://127.0.0.1:5002/

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>


Enable sites and reload Apache:

sudo a2ensite *.conf
sudo apachectl configtest
sudo systemctl reload apache2

🔐 Enable HTTPS with Let’s Encrypt
Install Certbot
sudo apt install certbot python3-certbot-apache -y

Generate SSL Certificate
sudo certbot --apache -d aditechsphere.publicvm.com


Certbot:

Verifies DNS ownership

Issues SSL certificates

Auto-configures Apache

Enables auto-renewal

HTTPS VirtualHost Example
<VirtualHost *:443>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    SSLCertificateFile /etc/letsencrypt/live/aditechsphere.publicvm.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/aditechsphere.publicvm.com/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>


(Same pattern applies to other microservices.)

🔁 How HTTP Still Works Internally

Flask services run on HTTP (localhost)

Apache performs SSL termination

External HTTP → HTTPS redirection

Internal traffic remains unencrypted (trusted network)

Browser → HTTPS → Apache → HTTP → Flask


✔ This is standard production architecture

🔒 Security Best Practices

Flask services bound to 127.0.0.1

Apache is the only public entry point

SSL auto-renewal via Certbot

Internal ports (5000–5002) can be firewalled

Clear separation of edge and application layers

🎯 Why This Project Is Strong for DevOps Roles

Real Apache reverse-proxy configuration

HTTPS migration without downtime

Subdomain-based microservices routing

Production-grade documentation

Easily extendable to Docker, Kubernetes, ALB, CI/CD

👨‍💻 Author

Aditya Sirsam
DevOps Engineer | AWS | Linux | Docker | Kubernetes
