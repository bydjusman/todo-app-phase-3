# Quickstart Guide: Kubernetes Todo Chatbot Deployment

## Prerequisites

- Docker Desktop 4.53+ with Kubernetes enabled
- Helm CLI installed
- kubectl configured to connect to Docker Desktop Kubernetes cluster
- Internet access for pulling images and dependencies

## Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Enable Kubernetes in Docker Desktop**
   - Open Docker Desktop
   - Go to Settings > Kubernetes
   - Check "Enable Kubernetes"
   - Click Apply & Restart

3. **Verify Kubernetes connection**
   ```bash
   kubectl cluster-info
   ```

4. **Install Gordon (optional, if available)**
   - Enable Docker Desktop Beta features if Gordon is available
   - Or install Gordon separately if it's a standalone tool

5. **Build Docker images**
   ```bash
   # Build backend image
   cd backend
   docker build -t todo-backend:latest .
   
   # Build frontend image
   cd ../frontend
   docker build -t todo-frontend:latest .
   ```

## Deployment Steps

1. **Navigate to Helm charts**
   ```bash
   cd helm
   ```

2. **Install backend Helm chart**
   ```bash
   helm install todo-backend ./backend
   ```

3. **Install frontend Helm chart**
   ```bash
   helm install todo-frontend ./frontend
   ```

4. **Verify deployment**
   ```bash
   kubectl get pods
   kubectl get services
   ```

## Verification

1. **Check all pods are running**
   ```bash
   kubectl get pods
   # All pods should show STATUS as "Running"
   ```

2. **Access the applications**
   - Backend health check: `http://localhost:8080/health`
   - Frontend: `http://localhost:3000`

3. **Scale the applications (optional)**
   ```bash
   # Scale backend to 2 replicas
   kubectl scale deployment/todo-backend --replicas=2
   
   # Scale frontend to 2 replicas
   kubectl scale deployment/todo-frontend --replicas=2
   ```

## Cleanup

1. **Uninstall Helm releases**
   ```bash
   helm uninstall todo-backend
   helm uninstall todo-frontend
   ```

2. **Remove Docker images (optional)**
   ```bash
   docker rmi todo-backend:latest
   docker rmi todo-frontend:latest
   ```