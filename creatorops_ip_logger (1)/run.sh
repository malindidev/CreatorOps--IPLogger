#!/bin/bash

clear

# CreatorOps ASCII Art
echo "╔══════════════════════════════╗"
echo "║      🔧 CreatorOps Tool      ║"
echo "╚══════════════════════════════╝"
echo
echo "An ethical, test-only IP logger powered by LocalXpose"
echo

# Prompt for token
read -p "🔑 Enter your LocalXpose tunnel token: " token

# Cool ASCII loading effect
echo
echo "🚀 Launching server..."
echo
sp="/-\\|"
for i in $(seq 1 15); do
  printf "\r⏳ Loading... ${sp:i%4:1}"
  sleep 0.1
done
echo
echo "✅ Ready."

# Start Flask server
echo "🌐 Starting local Flask IP logger on port 5000..."
pip install -q flask
python3 ip_logger.py &

sleep 2

# Start LocalXpose tunnel
echo "🔌 Connecting LocalXpose tunnel..."
lx serve http --token $token --port 5000
