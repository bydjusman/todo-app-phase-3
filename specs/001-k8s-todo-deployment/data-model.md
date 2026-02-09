# Data Model: Kubernetes Todo Chatbot Deployment

## Key Entities

### Backend Deployment
- **Name**: Kubernetes resource managing backend application pods
- **Fields**: 
  - replicaCount (integer, 1-2)
  - image (string, Docker image reference)
  - port (integer, 8080)
  - resources (object, CPU/memory limits)
  - envVars (array, environment variables)
- **Relationships**: Connected to Backend Service for network access
- **Validation**: Replica count must be between 1-2, image must be valid Docker reference

### Frontend Deployment
- **Name**: Kubernetes resource managing frontend application pods
- **Fields**: 
  - replicaCount (integer, 1-2)
  - image (string, Docker image reference)
  - port (integer, 3000)
  - resources (object, CPU/memory limits)
  - envVars (array, environment variables)
- **Relationships**: Connected to Frontend Service for network access
- **Validation**: Replica count must be between 1-2, image must be valid Docker reference

### Backend Service
- **Name**: Kubernetes resource exposing backend application
- **Fields**:
  - type (string, ClusterIP or NodePort)
  - port (integer, 8080)
  - targetPort (integer, 8080)
  - selector (object, labels to match backend pods)
- **Relationships**: Connects to Backend Deployment
- **Validation**: Port must match backend application port

### Frontend Service
- **Name**: Kubernetes resource exposing frontend application
- **Fields**:
  - type (string, ClusterIP or NodePort)
  - port (integer, 3000)
  - targetPort (integer, 3000)
  - selector (object, labels to match frontend pods)
- **Relationships**: Connects to Frontend Deployment
- **Validation**: Port must match frontend application port

### Helm Charts
- **Name**: Package format for Kubernetes applications
- **Fields**:
  - name (string, chart name)
  - version (string, semantic version)
  - appVersion (string, application version)
  - templates (array, Kubernetes manifest templates)
  - values (object, configurable parameters)
- **Relationships**: Contains Deployments, Services, ConfigMaps, and Secrets
- **Validation**: Must follow Helm chart standards

### Docker Images
- **Name**: Containerized versions of applications
- **Fields**:
  - name (string, image name)
  - tag (string, version tag)
  - registry (string, image registry)
  - size (integer, image size in bytes)
- **Relationships**: Referenced by Deployments
- **Validation**: Must be buildable from Dockerfile

### ConfigMaps
- **Name**: Kubernetes objects storing configuration data
- **Fields**:
  - name (string, object name)
  - data (object, key-value pairs of configuration)
  - namespace (string, Kubernetes namespace)
- **Relationships**: Referenced by Deployments
- **Validation**: Keys must be valid DNS subdomain names

### Secrets
- **Name**: Kubernetes objects storing sensitive information
- **Fields**:
  - name (string, object name)
  - data (object, base64 encoded key-value pairs)
  - type (string, secret type)
  - namespace (string, Kubernetes namespace)
- **Relationships**: Referenced by Deployments
- **Validation**: Must be properly encoded and secured