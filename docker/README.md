# Spam Classifier Docker Container

A containerized Streamlit web application for spam classification using Docker.

---

## Architecture

```mermaid
flowchart TB
    subgraph Docker Container
        A["Streamlit App<br/>Port 8080"]
        B[trained_model.pkl]
        C[Feature Extractor]
        D[utils.py]
    end
    
    E[Web Browser] -->|HTTP Port 8080| A
    A --> D
    D --> C
    C --> B
    B -->|prediction| A
    A -->|UI Update| E
```

---

## Web Interface

The container provides a user-friendly Streamlit interface for classifying messages.

```mermaid
flowchart LR
    subgraph UI Components
        A[Text Area]
        B[Classify Button]
        C[Results Panel]
    end
    
    A -->|User Input| B
    B -->|Triggers| C
```

| Component | Description |
|-----------|-------------|
| **Message text** | Input field for typing or pasting the message to classify |
| **Classify** | Button to run the classification model |
| **Results** | Visual feedback showing if the message is SPAM or HAM |

---

## UI Interaction Flow

```mermaid
sequenceDiagram
    participant user as User (Browser)
    participant st as Streamlit App
    participant utils as utils.py
    participant model as ML Model
    
    user->>st: Enter text & click Classify
    st->>utils: extract_features()
    utils-->>st: features {length, punct}
    st->>model: model.predict()
    model-->>st: "spam" | "ham"
    st-->>user: Display SPAM/HAM indicator
```

---

## Quick Start

### Prerequisites

- Docker installed
- Trained model (`trained_model.pkl`)

### Build and Run

```bash
# Copy the trained model
cp ../trained_model.pkl .

# Build the image
make build

# Run the container
make run

# Test the API
make test
```

---

## Makefile Commands

```mermaid
flowchart TD
    A[make help] --> B[Show all commands]
    
    C[make build] --> D[Build Docker image]
    E[make run] --> F[Start container]
    G[make stop] --> H[Stop container]
    I[make test] --> J[Test API endpoints]
    K[make logs] --> L[View container logs]
    M[make clean] --> N[Remove image & container]
    O[make push] --> P[Push to registry]
```

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make build` | Build the Docker image |
| `make run` | Run the container (detached) |
| `make run-fg` | Run in foreground (debug mode) |
| `make stop` | Stop and remove the container |
| `make logs` | View container logs |
| `make shell` | Open shell in container |
| `make test` | Test all API endpoints |
| `make clean` | Remove image and container |
| `make push` | Push image to registry |
| `make pull` | Pull image from registry |

---

## Usage

### Accessing the Web UI

Once the container is running, open your web browser and navigate to:

```
http://localhost:8080
```

### Health Check

The container includes a health check endpoint used by Docker and container orchestrators:

```bash
# Check if the healthy endpoint is active
curl http://localhost:8080/_stcore/health
```

Expected response: `ok`

---

## Container Configuration

```mermaid
flowchart LR
    subgraph Environment Variables
        A[PORT=8080]
        B[MODEL_PATH=/app/trained_model.pkl]
        C[DEBUG=false]
    end
    
    subgraph Docker Settings
        D[Exposed Port: 8080]
        E[Health Check: /health]
        F[Restart: unless-stopped]
    end
```

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8080` | Streamlit server port |
| `MODEL_PATH` | `trained_model.pkl` | Path to model file |

---

## Deployment Options

```mermaid
flowchart TB
    A[Docker Image] --> B[Local Docker]
    A --> C[Docker Compose]
    A --> D[Kubernetes]
    A --> E[AWS ECS/Fargate]
    A --> F[Google Cloud Run]
    A --> G[Azure Container Instances]
    
    style A fill:#2496ED
    style B fill:#2496ED
    style C fill:#2496ED
    style D fill:#326CE5
    style E fill:#FF9900
    style F fill:#4285F4
    style G fill:#0078D4
```

### Docker Compose Example

```yaml
version: '3.8'
services:
  spam-classifier:
    build: .
    ports:
      - "8080:8080"
    environment:
      - PORT=8080
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/_stcore/health"]
      interval: 30s
      timeout: 3s
      retries: 3
```

### Kubernetes Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spam-classifier
spec:
  replicas: 3
  selector:
    matchLabels:
      app: spam-classifier
  template:
    metadata:
      labels:
        app: spam-classifier
    spec:
      containers:
      - name: spam-classifier
        image: spam-classifier:latest
        ports:
        - containerPort: 8080
        livenessProbe:
          httpGet:
            path: /_stcore/health
            port: 8080
        readinessProbe:
          httpGet:
            path: /_stcore/health
            port: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: spam-classifier
spec:
  selector:
    app: spam-classifier
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

---

## Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit application |
| `utils.py` | Feature extraction utilities |
| `Dockerfile` | Container build instructions |
| `requirements.txt` | Python dependencies |
| `Makefile` | Build and deployment commands |
| `trained_model.pkl` | Default model (copy of v1 or v2) |
| `trained_model_v1.pkl` | Model v1 (trained on 1k dataset) |
| `trained_model_v2.pkl` | Model v2 (trained on 4k dataset) |

---

## Model Versions

Two model versions are available for class exercises:

| Version | Dataset | Samples | Description |
|---------|---------|---------|-------------|
| v1 | smsspamcollection-1k.csv | 1000 | Original 1k dataset |
| v2 | smsspamcollection-4k.csv | 999 | Extended 4k dataset |

### Switch Model Version

```bash
# Use v1
cp trained_model_v1.pkl trained_model.pkl

# Use v2
cp trained_model_v2.pkl trained_model.pkl

# Rebuild the image
make build
```

---

## Production Recommendations

```mermaid
flowchart LR
    subgraph Security
        A[Use HTTPS]
        B[Add authentication]
        C[Rate limiting]
    end
    
    subgraph Performance
        D[Use gunicorn]
        E[Horizontal scaling]
        F[Caching]
    end
    
    subgraph Monitoring
        G[Logging]
        H[Metrics]
        I[Alerting]
    end
```

For production, consider:
- Adding authentication (Proxy, Auth0)
- Implementing rate limiting at the ingress level
- Setting up monitoring (Prometheus, Grafana)
- Using a reverse proxy (nginx, traefik)

---

## 🧹 Cleanup

To stop and remove the container and image, you can use the Makefile or manual commands:

### Using Makefile
```bash
# Stop and remove the container
make stop

# Remove the container AND the image
make clean
```

### Manual Commands
```bash
# List running containers
docker ps

# Stop the container
docker stop spam-classifier

# Remove the container
docker rm spam-classifier

# Remove the image
docker rmi spam-classifier:latest
```
