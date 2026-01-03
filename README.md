DevOps Microservices Platform
HTTP → HTTPS with Apache Reverse Proxy on AWS EC2
📌 Project Overview

This project demonstrates a production-grade DevOps microservices architecture deployed on AWS EC2, using Python (Flask), Apache Reverse Proxy, subdomain-based routing, and HTTPS enablement with Let’s Encrypt.

Multiple independent microservices run on internal HTTP ports and are securely exposed to users via Apache, which performs SSL termination and traffic routing.

A key focus of this project is the real-world migration from HTTP to HTTPS, a critical responsibility of DevOps engineers.

🏗️ Architecture (Logical View)
User Browser
     |
     | HTTPS (443)
     v
Apache Reverse Proxy (EC2)
     |
     |-- aditechsphere.publicvm.com              → Homepage Service (5000)
     |-- microservice1.aditechsphere.publicvm.com → Orders Service (5001)
     |-- microservice2.aditechsphere.publicvm.com → Payments Service (5002)

🧩 Microservices in This Project
Service Name	Description	Internal Port
Homepage Service	Central platform dashboard	5000
Orders Service	Independent backend microservice	5001
Payments Service	Independent backend microservice	5002
🚀 Tech Stack Used

Python 3

Flask

Apache HTTP Server

Reverse Proxy & SSL Termination

AWS EC2 (Ubuntu Linux)

DNS & Subdomains

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
🛠️ Step-by-Step Setup Guide
🔹 Step 1: Launch EC2 Instance

Launch Ubuntu EC2

Open inbound ports:

80 (HTTP)

443 (HTTPS)

Attach an Elastic IP (recommended)

🔹 Step 2: Install Required Packages
sudo apt update
sudo apt install python3 python3-pip python3-venv apache2 -y


Enable required Apache modules:

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

Create A records pointing to EC2 public IP:

aditechsphere.publicvm.com              → EC2_IP
microservice1.aditechsphere.publicvm.com → EC2_IP
microservice2.aditechsphere.publicvm.com → EC2_IP


(Wildcard * record can also be used.)

🔄 Step 6: Configure Apache Reverse Proxy (HTTP)

Apache exposes each microservice via subdomains and forwards traffic to internal Flask ports.

All HTTP traffic is configured to redirect permanently to HTTPS.

🏠 Homepage – HTTP Config

File:
/etc/apache2/sites-available/aditechsphere.publicvm.com.conf

<VirtualHost *:80>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    ErrorLog ${APACHE_LOG_DIR}/home_error.log
    CustomLog ${APACHE_LOG_DIR}/home_access.log combined

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

🛒 Microservice 1 – HTTP Config
<VirtualHost *:80>
    ServerName microservice1.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5001/
    ProxyPassReverse / http://127.0.0.1:5001/

    ErrorLog ${APACHE_LOG_DIR}/ms1_error.log
    CustomLog ${APACHE_LOG_DIR}/ms1_access.log combined

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

💳 Microservice 2 – HTTP Config
<VirtualHost *:80>
    ServerName microservice2.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5002/
    ProxyPassReverse / http://127.0.0.1:5002/

    ErrorLog ${APACHE_LOG_DIR}/ms2_error.log
    CustomLog ${APACHE_LOG_DIR}/ms2_access.log combined

    RewriteEngine on
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>


Enable sites:

sudo a2ensite aditechsphere.publicvm.com.conf
sudo a2ensite microservice1.aditechsphere.publicvm.com.conf
sudo a2ensite microservice2.aditechsphere.publicvm.com.conf
sudo apachectl configtest
sudo systemctl reload apache2

🔐 Step 7: Enable HTTPS with Let’s Encrypt
🔹 Step 7.1: Install Certbot
sudo apt install certbot python3-certbot-apache -y

🔹 Step 7.2: Generate SSL Certificate
sudo certbot --apache -d aditechsphere.publicvm.com


Certbot:

Verifies domain ownership

Generates SSL certificates

Stores them under /etc/letsencrypt/live/

Installs SSL helper config

🔹 Step 7.3: HTTPS VirtualHosts (443)

Each service has its own SSL VirtualHost using the same certificate.

Example (Homepage):

<VirtualHost *:443>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    SSLCertificateFile /etc/letsencrypt/live/aditechsphere.publicvm.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/aditechsphere.publicvm.com/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>


(Same pattern for microservice1 and microservice2.)

Enable SSL:

sudo a2enmod ssl
sudo a2ensite aditechsphere.publicvm.com-le-ssl.conf
sudo a2ensite microservice1.aditechsphere.publicvm.com-le-ssl.conf
sudo a2ensite microservice2.aditechsphere.publicvm.com-le-ssl.conf
sudo apachectl configtest
sudo systemctl reload apache2

🔁 How HTTP Continues to Work After HTTPS

Flask apps continue running on HTTP internally

Apache performs SSL termination

HTTP requests are redirected to HTTPS

Internal traffic remains unencrypted (trusted network)

Browser → HTTPS → Apache → HTTP → Flask


This is standard production architecture.

🔒 Security Notes

Flask ports are bound to localhost

Apache is the only public entry point

SSL auto-renews via Certbot

Ports 5000–5002 can be firewalled for hardening

🎯 Why This Project Is Strong for DevOps Roles

Real reverse-proxy configuration

HTTPS migration with zero downtime

Subdomain-based microservices

Production-grade documentation

Easily extendable to Docker / Kubernetes / ALB

👨‍💻 Author

Aditya Sirsam
DevOps Engineer | AWS | Linux | Docker | Kubernetes
