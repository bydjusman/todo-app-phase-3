<!--
Sync Impact Report:
- Version change: 1.1.0 → 2.0.0
- Modified principles: Complete overhaul from AI-Powered Todo Chatbot to Cloud-Native Kubernetes Deployment
- Added sections: Cloud-Native Architecture, Kubernetes Deployment Standards, AI-Assisted DevOps, Containerization Requirements
- Removed sections: MCP Tooling Standards, Agent Behavior Rules from previous version
- Templates requiring updates: ✅ plan-template.md, ✅ spec-template.md, ✅ tasks-template.md
- Follow-up TODOs: None
-->
# Phase IV – Local Kubernetes Deployment of Todo Chatbot Constitution

## Core Principles

### Accuracy
All infrastructure and deployment steps must be reproducible locally. Every command, configuration, and deployment manifest must produce identical results across different developer machines. All Docker builds, Kubernetes deployments, and service configurations must be deterministic and verifiable.

### Clarity
Instructions must be explicit for developers with basic Kubernetes knowledge. All documentation, commands, and configuration files must be comprehensible to team members with fundamental understanding of containerization and orchestration concepts. No assumptions about advanced Kubernetes expertise should be made.

### Spec-Driven Development
Use Claude Code to generate all Docker, Helm, and Kubernetes resources automatically. All infrastructure-as-code artifacts must be generated through AI assistance following the Spec-Driven methodology. Manual coding is prohibited except for specification and validation scripts.

### AI-Assisted DevOps
Leverage Gordon (Docker AI) for containerization tasks and kubectl-ai / Kagent for Kubernetes orchestration. All Dockerfile creation, image building, and Kubernetes resource generation must be performed with AI assistance. Human intervention should be limited to validation and approval.

### Safety
Ensure environment variables, secrets, and ports are correctly managed for local deployment. All security best practices must be followed, including proper secret management, secure port exposure, and appropriate network policies. No hardcoded credentials or insecure configurations are permitted.

### Cloud-Native Architecture
Design and deploy using cloud-native principles with containerized microservices. Applications must be designed to run effectively in containerized environments with stateless components where possible. Services should be independently deployable and scalable.

## Kubernetes Deployment Standards

- Deployments must be reproducible on any local machine with Docker Desktop 4.53+ and Kubernetes enabled
- Use Minikube for local Kubernetes cluster setup and validation
- Implement proper service discovery between frontend and backend components
- Configure appropriate resource limits and requests for containers
- Implement health checks (liveness and readiness probes) for all services
- Use ConfigMaps for configuration parameters and Secrets for sensitive data
- Ensure proper namespace organization for application components

## Containerization Requirements

- Create Docker container images for both frontend and backend applications
- Optimize Dockerfiles for minimal attack surface and reduced image size
- Use multi-stage builds where appropriate to minimize production image footprint
- Implement proper .dockerignore files to exclude unnecessary files
- Tag images appropriately for version tracking and deployment

## Helm Chart Standards

- Package Kubernetes manifests into Helm charts for easier deployment management
- Use parameterized Helm charts that allow customization of deployment properties
- Implement proper upgrade/rollback strategies in Helm charts
- Include appropriate default values and documentation for chart parameters
- Structure charts to support both development and production configurations

## AI-Assisted DevOps Practices

- All Dockerfile creation must be generated through AI assistance (Gordon)
- Kubernetes manifests must be created with AI assistance (kubectl-ai / Kagent)
- Helm charts must be generated using AI tools with proper templating
- Infrastructure changes must follow the Spec-Driven workflow
- All automation scripts must be AI-generated and human-reviewed

## Scalability Requirements

- Support scaling of frontend/backend replicas as needed
- Implement horizontal pod autoscaling where appropriate
- Design services to handle load balancing effectively
- Ensure stateless design to enable seamless scaling
- Validate performance under scaled conditions

## Validation and Testing

- Deployment validation: Local Minikube pods running successfully
- Frontend accessibility at port 3000
- Backend accessibility at port 8080
- Service-to-service communication functioning properly
- Proper ingress configuration if required
- Successful scaling of replica sets

## Development Workflow

- No manual coding; all commands and manifests must be generated through Claude Code or AI DevOps agents
- All Docker, Helm, and Kubernetes resources generated via AI assistance
- Spec-driven approach for all infrastructure changes
- Reproducible deployments on local machines with Docker Desktop 4.53+ and Kubernetes enabled
- Comprehensive documentation of the Spec-Driven workflow used

## Governance

All implementations must adhere to cloud-native and Kubernetes best practices. Any deviation from the specified containerization and deployment standards is prohibited. All changes must maintain local reproducibility across different developer environments. Compliance with security requirements must be verified during deployment validation. The constitution supersedes all other deployment practices.

**Version**: 2.0.0 | **Ratified**: 2026-02-09 | **Last Amended**: 2026-02-09