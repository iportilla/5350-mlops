# Spam Classifier Azure Function

Serverless HTTP API for spam classification using Azure Functions.

## Endpoints

### POST /api/classify
Classify a message as spam or ham.

**Request:**
```json
{
  "message": "Congratulations! You've won a free prize!"
}
```

**Response:**
```json
{
  "message": "Congratulations! You've won a free prize!",
  "features": {
    "length": 45,
    "punct": 3
  },
  "prediction": "spam"
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Local Development

### Prerequisites
- Python 3.9+
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local)

### Setup
```bash
cd azure_function
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run locally
```bash
func start
```

The function will be available at `http://localhost:7071/api/classify`

### Test
```bash
curl -X POST http://localhost:7071/api/classify \
  -H "Content-Type: application/json" \
  -d '{"message": "You won a free iPhone! Click here now!"}'
```

## Deploy to Azure

### Using Azure CLI
```bash
# Login to Azure
az login

# Create resource group
az group create --name spam-classifier-rg --location eastus

# Create storage account
az storage account create --name spamclassifierstorage --location eastus --resource-group spam-classifier-rg --sku Standard_LRS

# Create function app
az functionapp create --resource-group spam-classifier-rg --consumption-plan-location eastus --runtime python --runtime-version 3.11 --functions-version 4 --name spam-classifier-func --storage-account spamclassifierstorage --os-type Linux

# Deploy
func azure functionapp publish spam-classifier-func
```

### Using Azure Developer CLI (azd)
```bash
azd init
azd up
```

## Files

- `function_app.py` - Main function code with HTTP endpoints
- `requirements.txt` - Python dependencies
- `host.json` - Azure Functions host configuration
- `local.settings.json` - Local development settings (not deployed)
- `trained_model.pkl` - Default model (copy of v1 or v2)
- `trained_model_v1.pkl` - Model v1 (trained on 1k dataset)
- `trained_model_v2.pkl` - Model v2 (trained on 4k dataset)

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
```

After switching, restart the function for changes to take effect.
