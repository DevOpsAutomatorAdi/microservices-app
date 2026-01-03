#!/bin/bash

echo "Starting all microservices in background..."

# Homepage
cd homepage || exit
nohup python3 app.py > homepage.log 2>&1 &
echo "Homepage running in background (port 5000)"
cd ..

# Microservice 1
cd microservice1 || exit
nohup python3 app.py > microservice1.log 2>&1 &
echo "Microservice1 running in background (port 5001)"
cd ..

# Microservice 2
cd microservice2 || exit
nohup python3 app.py > microservice2.log 2>&1 &
echo "Microservice2 running in background (port 5002)"
cd ..

echo "✅ All services started in background 🚀"

