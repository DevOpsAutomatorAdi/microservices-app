#  DevOps Microservices Platform  
### HTTP → HTTPS using Apache Reverse Proxy on AWS EC2


::contentReference[oaicite:0]{index=0}


---

## 📌 Project Overview

This project demonstrates a **production-grade DevOps microservices architecture** deployed on **AWS EC2** using **Python Flask**, **Apache Reverse Proxy**, and **HTTPS with Let’s Encrypt**.

Multiple independent microservices run internally on HTTP and are securely exposed to users through **subdomain-based routing**. Apache acts as a **single secure entry point**, handling:

- Reverse proxy routing  
- SSL termination  
- HTTP → HTTPS redirection  

A key highlight of this project is a **real-world HTTP to HTTPS migration**, which is a critical responsibility of DevOps engineers in production environments.

---

## 🏗️ Architecture (Logical View)



flowchart TB
    U[User Browser]

    U -->|HTTPS 443| A[Apache Reverse Proxy<br/>(AWS EC2)]

    A -->|aditechsphere.publicvm.com| H[Homepage Service<br/>127.0.0.1:5000]
    A -->|microservice1.aditechsphere.publicvm.com| O[Orders Service<br/>127.0.0.1:5001]
    A -->|microservice2.aditechsphere.publicvm.com| P[Payments Service<br/>127.0.0.1:5002]



---

## 🧩 Microservices

| Service Name | Description | Internal Port |
|-------------|-------------|---------------|
| Homepage Service | Central dashboard / landing page | 5000 |
| Orders Service | Independent backend microservice | 5001 |
| Payments Service | Independent backend microservice | 5002 |

---

## 🚀 Tech Stack

- **Python 3**
- **Flask**
- **Apache HTTP Server**
- **Reverse Proxy & SSL Termination**
- **AWS EC2 (Ubuntu Linux)**
- **DNS & Subdomains**
- **Let’s Encrypt (Certbot)**

---

## 📂 Project Structure



microservices-app/
│
├── homepage/
│ └── app.py
│
├── microservice1/
│ └── app.py
│
├── microservice2/
│ └── app.py
│
└── README.md


---

## 🌐 Domain Mapping

| Public URL | Service |
|-----------|---------|
| http://aditechsphere.publicvm.com | Homepage |
| http://microservice1.aditechsphere.publicvm.com | Orders Service |
| http://microservice2.aditechsphere.publicvm.com | Payments Service |

> ⚠️ All HTTP traffic is permanently redirected to HTTPS.

---

## 🛠️ Deployment Guide

### 1️⃣ Launch EC2 Instance

- Ubuntu Server
- Open inbound ports:
  - **80 (HTTP)**
  - **443 (HTTPS)**
- Attach **Elastic IP** (recommended)

---

### 2️⃣ Install Required Packages

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv apache2 -y


Enable Apache modules:

sudo a2enmod proxy proxy_http headers rewrite ssl
sudo systemctl restart apache2

3️⃣ Setup Python Virtual Environment
mkdir ~/microservices-app
cd ~/microservices-app
python3 -m venv venv
source venv/bin/activate
pip install flask

4️⃣ Run Flask Microservices
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

5️⃣ DNS Configuration

Create A records pointing to EC2 public IP:

aditechsphere.publicvm.com               → EC2_IP
microservice1.aditechsphere.publicvm.com → EC2_IP
microservice2.aditechsphere.publicvm.com → EC2_IP

🔄 Apache Reverse Proxy (HTTP → HTTPS)
Homepage – HTTP VirtualHost
<VirtualHost *:80>
    ServerName aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

Orders Service – HTTP VirtualHost
<VirtualHost *:80>
    ServerName microservice1.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5001/
    ProxyPassReverse / http://127.0.0.1:5001/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

Payments Service – HTTP VirtualHost
<VirtualHost *:80>
    ServerName microservice2.aditechsphere.publicvm.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5002/
    ProxyPassReverse / http://127.0.0.1:5002/

    RewriteEngine On
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>


Enable sites:

sudo a2ensite *.conf
sudo apachectl configtest
sudo systemctl reload apache2

🔐 Enable HTTPS with Let’s Encrypt
Install Certbot
sudo apt install certbot python3-certbot-apache -y

Generate SSL Certificate
sudo certbot --apache -d aditechsphere.publicvm.com


Certbot automatically:

Verifies domain ownership

Issues SSL certificates

Configures Apache

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

🔁 HTTP & HTTPS Flow Explained
Browser → HTTPS → Apache → HTTP → Flask


✔ Flask runs internally on HTTP
✔ Apache performs SSL termination
✔ External traffic is fully encrypted

This is standard production architecture.

🔒 Security Highlights

Flask services bound to localhost

Apache is the only public entry point

SSL certificates auto-renew via Certbot

Internal ports can be firewalled

Clear separation of edge & application layers

🎯 Why This Project Is Valuable for DevOps Roles

Real Apache reverse-proxy setup

Practical HTTPS migration

Subdomain-based microservices routing

Strong security posture

Production-ready documentation

Easily extendable to Docker, Kubernetes, ALB, CI/CD

🔮 Future Enhancements

Docker & Docker Compose

Kubernetes deployment

CI/CD using GitHub Actions

Monitoring with Prometheus & Grafana

AWS ALB integration

👨‍💻 Author

Aditya Sirsam
DevOps Engineer | AWS | Linux | Docker | Kubernetes


---

### ✅ What this README fixes
✔ Clean layout  
✔ Professional tone  
✔ Easy to scan for recruiters  
✔ Proper headings & spacing  
✔ Looks **premium on GitHub**

If you want next:
- 🔥 **Badges (AWS, HTTPS, Python, Apache)**
- 📸 **Where to add your real screenshots**
- 🐳 **Docker version README**
- ☸️ **Kubernetes extension README**

Just tell me.
