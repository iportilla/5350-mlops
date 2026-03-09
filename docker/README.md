# Spam Classifier Docker Container

A containerized REST API for spam classification using Flask and Docker.

---

## Architecture

```mermaid
flowchart TB
    subgraph Docker Container
        A["Flask API<br/>Port 8080"]
        B[trained_model.pkl]
        C[Feature Extractor]
    end
    
    D[HTTP Client] -->|POST /classify| A
    A --> C
    C --> B
    B -->|prediction| A
    A -->|JSON response| D
```

---

## API Endpoints

```mermaid
flowchart LR
    subgraph Endpoints
        A[GET /]
        B[GET /health]
        C[POST /classify]
    end
    
    A -->|API info| R1[JSON]
    B -->|status check| R2[healthy/unhealthy]
    C -->|message| R3[spam/ham prediction]
```

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and available endpoints |
| `/health` | GET | Health check for load balancers |
| `/classify` | POST | Classify a message as spam or ham |

---

## Request/Response Flow

```mermaid
sequenceDiagram
    participant Client
    participant Flask API
    participant Feature Extractor
    participant ML Model
    
    Client->>Flask API: "POST /classify<br/>{\"message\": \"...\"}"
    Flask API->>Feature Extractor: Extract features
    Feature Extractor-->>Flask API: {length, punct}
    Flask API->>ML Model: Predict
    ML Model-->>Flask API: "spam" | "ham"
    Flask API-->>Client: JSON response
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

## API Usage

### Classify a Message

**Request:**
```bash
curl -X POST http://localhost:8080/classify \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won a FREE prize!"}'
```

**Response:**
```json
{
  "message": "Congratulations! You won a FREE prize!",
  "features": {
    "length": 41,
    "punct": 2
  },
  "prediction": "spam"
}
```

### Health Check

```bash
curl http://localhost:8080/health
```

```json
{
  "status": "healthy"
}
```

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
| `PORT` | `8080` | API server port |
| `MODEL_PATH` | `/app/trained_model.pkl` | Path to model file |
| `DEBUG` | `false` | Enable Flask debug mode |

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
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
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
            path: /health
            port: 8080
        readinessProbe:
          httpGet:
            path: /health
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
| `app.py` | Flask API application |
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
- Using gunicorn with multiple workers: `gunicorn -w 4 -b 0.0.0.0:8080 app:app`
- Adding authentication (API keys, JWT)
- Implementing rate limiting
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
