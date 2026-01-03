# 🚀 DevOps Microservices Platform  
### HTTP → HTTPS using Apache Reverse Proxy on AWS EC2

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

```mermaid
flowchart TB
    U[User Browser]
    U -->|HTTPS 443| A[Apache Reverse Proxy<br/>(AWS EC2)]
    A -->|aditechsphere.publicvm.com| H[Homepage Service<br/>127.0.0.1:5000]
    A -->|microservice1.aditechsphere.publicvm.com| O[Orders Service<br/>127.0.0.1:5001]
    A -->|microservice2.aditechsphere.publicvm.com| P[Payments Service<br/>127.0.0.1:5002]
```

---

## 🧩 Microservices

| Service Name | Description | Internal Port |
|-------------|------------|---------------|
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

## 📁 Project Structure

```text
microservices-app/
├── homepage/
│   └── app.py
├── microservice1/
│   └── app.py
├── microservice2/
│   └── app.py
└── README.md
```

---

## 🌐 Domain Mapping

| Public URL | Service |
|-----------|---------|
| http://aditechsphere.publicvm.com | Homepage |
| http://microservice1.aditechsphere.publicvm.com | Orders Service |
| http://microservice2.aditechsphere.publicvm.com | Payments Service |

> ⚠️ All HTTP traffic is permanently redirected to **HTTPS**.

---

## 🛠️ Deployment Guide

### 1️⃣ Launch EC2 Instance

- Ubuntu Server  
- Open ports **80** and **443**  
- Attach Elastic IP  

---

### 2️⃣ Install Required Packages

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv apache2 -y
```

```bash
sudo a2enmod proxy proxy_http headers rewrite ssl
sudo systemctl restart apache2
```

---

### 3️⃣ Setup Python Virtual Environment

```bash
mkdir ~/microservices-app
cd ~/microservices-app
python3 -m venv venv
source venv/bin/activate
pip install flask
```

---

### 4️⃣ Run Flask Microservices

```bash
python homepage/app.py
python microservice1/app.py
python microservice2/app.py
```

---

## 👨‍💻 Author

**Aditya Sirsam**  
DevOps Engineer | AWS | Linux | Docker | Kubernetes
