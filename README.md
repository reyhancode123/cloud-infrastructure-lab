# Cloud Infrastructure Lab

A hands-on infrastructure project using Docker, Docker Compose, and Terraform.

## Project Overview

This project demonstrates a containerized application environment with infrastructure provisioning using Terraform.

The infrastructure consists of:
- Python HTTP backend
- Nginx reverse proxy
- Docker Compose
- Terraform-managed Docker network and Alpine container
- Container resource limits

## Architecture

```text
Client
  |
  v
Nginx Reverse Proxy
127.0.0.1:8080
  |
  v
Python Backend
Internal Port: 8000
  |
  v
JSON Response
```

## Technologies

- Linux Mint
- Docker
- Docker Compose
- Terraform
- Python 3.12
- Nginx
- Alpine Linux

## Project Structure

```text
cloud-infrastructure-lab/
├── docker/
│   ├── app/
│   │   ├── app.py
│   │   └── Dockerfile
│   └── nginx/
│       └── default.conf
├── terraform/
│   ├── main.tf
│   ├── providers.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Run Application

Start containers:

```bash
docker compose up -d --build
```

Check containers:

```bash
docker compose ps
```

Test application:

```bash
curl -i http://127.0.0.1:8080
```

## Terraform

Enter Terraform directory:

```bash
cd terraform
```

Initialize:

```bash
terraform init
```

Validate:

```bash
terraform validate
```

Review infrastructure:

```bash
terraform plan
```

Apply configuration:

```bash
terraform apply
```

View outputs:

```bash
terraform output
```

## Infrastructure Configuration

| Resource | Configuration |
|---|---|
| Docker Network | Bridge |
| Network Subnet | 172.20.0.0/16 |
| Alpine Image | alpine:3.22 |
| Container Memory | 64 MB |
| Total Memory + Swap | 128 MB |

## Security

- Backend port is not directly exposed to the host.
- Nginx listens on localhost port 8080.
- Docker containers use isolated networks.
- Container memory is limited.
- Terraform state files are excluded from Git.

## Verification

- Docker Compose containers running successfully.
- Python backend returns healthy JSON response.
- Nginx reverse proxy returns HTTP 200 OK.
- Terraform validation successful.
- Terraform plan reports no infrastructure changes.
- Terraform outputs generated successfully.

## Project Goals

This project demonstrates practical experience with:

- Infrastructure as Code (IaC)
- Containerization
- Linux administration
- Docker networking
- Reverse proxy configuration
- Infrastructure security

---

**Project Status:** Infrastructure deployment and verification completed. Documentation and GitHub publication in progress.
