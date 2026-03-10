# 🤖 AI-Powered Test Framework API on Kubernetes

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.35-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4o-orange)
![Helm](https://img.shields.io/badge/Helm-v3.20-purple)
![Docker](https://img.shields.io/badge/Docker-24.0-blue)

A production-grade AI-powered test case generator built with 
FastAPI and OpenAI GPT-4o, containerized with Docker, and 
deployed to Kubernetes with autoscaling and Helm packaging.

## 🏗️ Architecture
```
Client Request
      ↓
Kubernetes Service (NodePort)
      ↓
HPA (Auto-scales 1-5 pods based on CPU)
      ↓
FastAPI Pods (2 replicas by default)
      ↓
OpenAI GPT-4o (generates test cases)
      ↓
JSON Response
```

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10 + FastAPI | REST API framework |
| OpenAI GPT-4o | AI test case generation |
| Docker | Multi-stage containerization |
| Kubernetes | Container orchestration |
| Helm v3 | K8s package management |
| HPA | Horizontal autoscaling |
| WSL2 Ubuntu | Local development |
| Minikube | Local K8s cluster |

## 📁 Project Structure
```
test-api-k8s/
├── app/
│   ├── main.py              # FastAPI application
│   ├── ai_generator.py      # OpenAI integration
│   └── requirements.txt     # Python dependencies
├── k8s/
│   ├── namespace.yaml       # K8s namespace
│   ├── deployment.yaml      # K8s deployment
│   ├── service.yaml         # K8s service
│   ├── hpa.yaml             # Autoscaler config
│   └── secret.yaml          # API key secret (gitignored)
├── helm/
│   └── test-api-chart/      # Helm chart
├── Dockerfile               # Multi-stage build
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- WSL2 Ubuntu 22.04
- Docker
- Minikube
- kubectl
- Helm v3
- OpenAI API key

### 1. Clone the repo
```bash
git clone https://github.com/sabyag42/ai-test-framework-k8s.git
cd ai-test-framework-k8s
```

### 2. Start Minikube
```bash
minikube start --driver=docker --memory=3800 --cpus=2
```

### 3. Create secret with your OpenAI key
```bash
kubectl create namespace test-framework
kubectl create secret generic api-secrets \
  --from-literal=openai-key=YOUR_OPENAI_KEY \
  -n test-framework
```

### 4. Build and load Docker image
```bash
docker build -t test-api:v1 .
minikube image load test-api:v1
```

### 5. Deploy with Helm
```bash
cd helm
helm install test-api ./test-api-chart
```

### 6. Get service URL
```bash
minikube service test-api-service -n test-framework --url
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/generate-tests` | AI test generation |
| POST | `/run-tests` | Execute test cases |

## 🤖 AI Test Generation Example

### Request
```bash
curl -X POST http://YOUR_URL/generate-tests \
  -H "Content-Type: application/json" \
  -d '{
    "endpoint": "/login",
    "method": "POST", 
    "description": "Login with email and password",
    "num_cases": 3
  }'
```

### Response
```json
{
  "endpoint": "/login",
  "method": "POST",
  "test_cases": [
    {
      "name": "Valid login",
      "description": "Happy path test",
      "input_data": {"email": "user@test.com", "password": "correct123"},
      "expected_status": 200,
      "expected_response": {"token": "string"}
    }
  ],
  "generated_by": "GPT-4o",
  "count": 3
}
```

## ☸️ Kubernetes Features Demonstrated

- ✅ Namespace isolation
- ✅ Deployment with rolling updates
- ✅ NodePort Service
- ✅ Horizontal Pod Autoscaler (1-5 pods)
- ✅ Liveness and Readiness probes
- ✅ Resource requests and limits
- ✅ Secret management
- ✅ Helm packaging with upgrade/rollback

## 👤 Author

**Sabyasachi** — Senior SDET & AI Engineer  
AI-powered automation | Kubernetes | Python | DevOps

---
⭐ Star this repo if you found it useful!
