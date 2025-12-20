# Build & Deploy Flask App with CI/CD Pipeline

🐍 Python Flask + 🐳 Docker + ⚙️ GitHub Actions + ☁️ AWS EC2

A complete CI/CD pipeline that automatically tests, builds, and deploys your Flask application.

## 🏗️ Architecture

```
Push Code → GitHub Actions → Run Tests → Build Docker Image → Push to Docker Hub → Deploy to EC2
```

## 📁 Project Structure

```
flask-cicd-demo/
├── app/
│   └── main.py           # Flask application
├── tests/
│   └── test_app.py       # Pytest tests
├── .github/workflows/
│   └── ci-cd.yml         # GitHub Actions pipeline
├── Dockerfile            # Production Docker image
├── requirements.txt      # Python dependencies
└── scripts/
    └── ec2-setup.sh      # EC2 setup script
```

## 🚀 Quick Start

### Run Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app/main.py

# Visit http://localhost:5000
```

### Run with Docker

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## 🔧 CI/CD Setup

### 1. Add GitHub Secrets

Go to: Repository → Settings → Secrets → Actions

| Secret | Value |
|--------|-------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token |
| `EC2_HOST` | EC2 public IP |
| `EC2_USERNAME` | `ec2-user` or `ubuntu` |
| `EC2_SSH_KEY` | Contents of your .pem file |

### 2. Setup EC2

```bash
# SSH into EC2
ssh -i your-key.pem ec2-user@your-ec2-ip

# Run setup script
curl -O https://raw.githubusercontent.com/YOUR_USERNAME/flask-cicd-demo/main/scripts/ec2-setup.sh
chmod +x ec2-setup.sh
./ec2-setup.sh
```

### 3. Push and Deploy

```bash
git push origin main
# Pipeline runs automatically!
```

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Create task |
| DELETE | `/tasks/<id>` | Delete task |

## 📝 License

MIT
