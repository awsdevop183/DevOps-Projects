#!/bin/bash
# ===========================================
# EC2 Docker Setup Script
# Supports Amazon Linux 2023 and Ubuntu 22.04
# ===========================================

set -e

echo "🚀 Setting up Docker on EC2..."

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
fi

if [ "$OS" == "amzn" ]; then
    echo "📦 Installing on Amazon Linux..."
    sudo yum update -y
    sudo yum install -y docker
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker ec2-user

elif [ "$OS" == "ubuntu" ]; then
    echo "📦 Installing on Ubuntu..."
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker ubuntu
fi

echo ""
echo "✅ Docker installed successfully!"
echo ""
echo "⚠️  Log out and log back in for changes to take effect"
echo ""
echo "Test with: docker run hello-world"
