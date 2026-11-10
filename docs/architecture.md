# Cloud Infrastructure Lab Architecture

## Architecture Diagram

```mermaid
flowchart TB
    subgraph Docker_Compose["Docker Compose Environment"]
        User["Client / Browser"]
        Nginx["Nginx Reverse Proxy<br/>127.0.0.1:8080"]
        App["Python Backend<br/>Port 8000"]

        User --> Nginx
        Nginx --> App
    end

    subgraph Terraform["Terraform Managed Infrastructure"]
        TF["Terraform"]
        Network["Docker Bridge Network<br/>172.20.0.0/16"]
        Alpine["Alpine Container<br/>64 MB RAM Limit"]

        TF --> Network
        TF --> Alpine
        Alpine --- Network
    end

    subgraph CI["GitHub Actions"]
        Push["Git Push / Pull Request"]
        Workflow["Automated Tests"]
        Pytest["Pytest<br/>3 Test Cases"]

        Push --> Workflow
        Workflow --> Pytest
    end

```

## Components

### Docker Compose
- Nginx acts as a reverse proxy.
- Python Backend handles HTTP requests and returns JSON responses.
- Nginx exposes the application through `127.0.0.1:8080`.

### Terraform
- Creates a dedicated Docker bridge network.
- Deploys an Alpine Linux container.
- Configures container memory and swap limits.

### GitHub Actions
- Runs automatically on pushes to `main` and pull requests targeting `main`.
- Installs Python 3.12 and pytest.
- Executes automated backend tests.
