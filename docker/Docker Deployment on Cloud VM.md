# **Docker Deployment on Cloud VM**





In this lab, we deploy the **spam classifier API inside a Docker container running on a cloud VM**.



Students will:



1. Connect to a remote VM
2. Clone the course repository
3. Build the Docker image
4. Run the containerized API





This stage represents **Level 2 in the MLOps maturity model**, where environments become **reproducible and portable**.



------





# **Step 1 — Connect to the VM**





Use SSH to access the cloud VM.

```
ssh ubuntu@VM_IP
```

Example:

```
ssh ubuntu@34.120.15.44
```



------





# **Step 2 — Create a Working Directory**





Create a directory for your lab work.

```
mkdir NAME
cd NAME
```

Example:

```
mkdir ivan
cd ivan
```



------





# **Step 3 — Clone the Course Repository**





Clone the course repository containing the MLOps exercises.

```
git clone https://github.com/iportilla/5350-mlops.git
```

Move into the project directory:

```
cd 5350-mlops
```



------





# **Step 4 — Build the Docker Image**





Use the Makefile to build the Docker image.

```
make build
```

This step will:



- build the Docker container
- install Python dependencies
- package the spam classifier model





------





# **Step 5 — Run the Docker Container**





Start the spam classifier API.

```
make run
```

The API will start inside the container.



------





# **Test the API**





From another terminal:

```
curl -X POST http://VM_IP:8000/classify \
-H "Content-Type: application/json" \
-d '{"message":"You won a free iPhone!"}'
```

Example response:

```
{
  "prediction": "spam"
}
```



------





# **Architecture**



```
flowchart LR
StudentLaptop --> SSH
SSH --> CloudVM
CloudVM --> GitClone
GitClone --> DockerBuild
DockerBuild --> DockerContainer
DockerContainer --> SpamClassifierAPI
SpamClassifierAPI --> ClientRequest
```



------





# **Learning Goals**





Students learn how to:



- deploy ML systems on cloud infrastructure
- create reproducible environments with Docker
- run inference APIs in containers
- prepare models for cloud deployment





This prepares the next stages of the course:



- **IBM Code Engine serverless deployment**
- **Azure Functions deployment**
- **Full MLOps pipelines**



