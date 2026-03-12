# Spam Classifier on Lightweight Kubernetes (k3s/k3d)

This guide provides instructions for deploying the Spam Classifier to a lightweight Kubernetes cluster. Since native `k3s` is built for Linux, we recommend using **k3d** (K3s in Docker) for **macOS** and **Windows** users.

---

## Prerequisites

### 🍏 macOS
1.  **Docker Desktop** (or OrbStack/Colima) installed and running.
2.  **Homebrew** installed.
3.  **Install k3d and kubectl**:
    ```bash
    brew install k3d kubectl
    ```

### 🪟 Windows
1.  **Docker Desktop** installed with **WSL2** backend.
2.  **Install k3d**:
    ```powershell
    # Using Chocolatey
    choco install k3d
    # OR using Winget
    winget install k3d
    ```
3.  **Install kubectl**: `winget install kubernetes-cli`.

### 🐧 Linux
1.  **k3s installed**:
    ```bash
    curl -sfL https://get.k3s.io | sh -
    ```

---

## Setup Your Cluster

### 1. Create a Cluster (Mac/Windows)
Use `k3d` to spin up a k3s cluster inside Docker:

```bash
k3d cluster create my-cluster --port 8080:80@loadbalancer
```
*This command creates a cluster and maps your local port 8080 to the Kubernetes LoadBalancer.*

### 2. Verify Connection
Ensure `kubectl` can see your new cluster and is correctly configured:

```bash
# Check cluster status and control plane
kubectl cluster-info

# Output should look like:
# Kubernetes control plane is running at https://0.0.0.0:60799...
```

---

## Deployment Steps

### 1. Build the Docker Image
Build the image locally in the `docker/` directory:

```bash
docker build -t spam-classifier:latest .
```

### 2. Import the Image into the Cluster
For `k3d`, you must explicitly "push" your local image into the cluster nodes:

```bash
k3d image import spam-classifier:latest -c my-cluster
```

### 3. Apply the Manifests
Deploy the application and its service:

```bash
# From the docker directory
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 4. Verify the Pod Status
Check if your pods are running successfully:

```bash
kubectl get pods

# Expected Output:
# NAME                               READY   STATUS    RESTARTS   AGE
# spam-classifier-57d5599577-qdpwc   1/1     Running   0          96s
```

### 4. Access the Web UI (Reliable Method)
Since the `LoadBalancer` might stay **pending** on local Mac/Windows environments, the most reliable way to access your application is using **port-forwarding**:

```bash
# In a separate terminal
kubectl port-forward service/spam-classifier-service 8080:80
```

Now you can open your browser and navigate to `http://localhost:8080`.

**Note:** The application now provides a Streamlit Web UI. The previous Flask REST API endpoints (like `/classify`) are no longer available.

---

## Troubleshooting

### Connection Refused?
If `kubectl apply` worked but the browser fails to connect, your `LoadBalancer` is likely still pending. Use the **Port-Forward** command above.
```bash
kubectl config get-contexts
kubectl config use-context k3d-my-cluster
```

### Pod not starting?
Check for errors in the pod description:
```bash
kubectl get pods
kubectl describe pod <pod-name>
```
*Usually, this is due to `ImagePullBackOff` if you forgot to run `k3d image import`.*

---

## 🧹 Cleanup and Stop

Once you are finished with the lab, it is important to clean up your resources.

### Option A: Stop and Clean k3d (Mac/Windows)
If you are using `k3d`, you can delete the entire cluster and all its resources with one command:
```bash
k3d cluster delete my-cluster
```

### Option B: Stop and Clean k3s (Linux)
If you are using a native `k3s` cluster, delete the specific manifests:
```bash
# Delete the service and deployment
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml

# (Optional) Stop the k3s service
sudo systemctl stop k3s
```

### Option C: Port-Forwarding
If you have a `port-forward` running, simply press `Ctrl + C` in that terminal to stop it.
