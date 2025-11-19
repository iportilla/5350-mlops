 ## How to Reduce Cost When Using Azure ML Deployments

Azure ML can get expensive very quickly if not configured correctly.
Here are the top cost-saving strategies, ordered by impact.

⸻

### 1. Use Serverless Endpoints for Inference (BIGGEST SAVINGS)

Instead of provisioning compute (VMs running 24/7), serverless charges only per request.

When to use serverless:

✔ Classroom demos
✔ Light workloads
✔ Occasional model testing
✔ Low-volume inference

Why it saves money:
	•	No idle running VMs
	•	No need to manage scaling
	•	Costs approach zero when unused
	•	No GPU charges unless you explicitly choose GPU serverless

⸻

### 2. Avoid Persistent Compute for Deployments

If you deploy using Managed Online Endpoints with compute, Azure allocates a VM like:
	•	Standard_F2s
	•	Standard_DS3
	•	GPU nodes 😱 (EXPENSIVE)

These VMs run 24/7 until you delete the endpoint.

✔ After class → DELETE the endpoint
✔ Or scale to 0 instances if supported
✔ Use smallest SKU (F2s_v2 or B-series)

⸻

### 3. Use Lower-Cost SKU for Training/Compute

When you must use compute:
	•	Prefer CPU clusters unless GPU needed
	•	Use F2s_v2, B2s, B4ms
	•	Use low priority or spot instances for huge discounts

⸻

### 4. Enable Autoscaling Wisely

Default autoscaling is often wasteful.

Recommended autoscale for demos:
	•	Min nodes = 0
	•	Max nodes = 1–2
	•	Idle time before scale down = 5–10 min

This alone can save 50–80%.

⸻

###  5. Turn Off Compute Instances After Use

Compute Instances (like notebook VMs) are a hidden cost trap.

Always:
✔ Stop the instance when done
✔ Set policies to auto-stop after X hours
✔ Use shared compute for the whole class

⸻

###  6. Use Free or Included Models Where Possible

Azure sometimes provides “included quota” on certain models.
Prefer:
	•	Azure-OpenAI small models
	•	Built-in classical models
	•	Pretrained MLflow models

Avoid expensive foundation models unless needed.

⸻

###  7. Use Batch Endpoints Instead of Online Endpoints

For anything not real-time:
✔ Batch can run on spot compute
✔ Cost is >80% cheaper than online endpoints
✔ No VM running when idle

⸻

### 8. Delete Everything After Class

The top cause of unexpected bills:
forgotten endpoints + forgotten compute.

Teach students to clean up:
	•	Endpoints
	•	Managed deployments
	•	Compute clusters
	•	Compute instances
	•	Storage logs

⸻

### Quick Classroom Example

If students deploy a model to Standard_F2s_v2:
	•	$0.14/hr
	•	$3.36/day
	•	~$100/month (for one student!)

But serverless:
	•	$0 when idle
	•	Only pay for requests
	•	A classroom can cost < $1 total

This is why serverless is preferred for teaching and MLOps inference workloads.

⸻

### Summary for Students (One Slide Version)

Best Cost-Saving Practices in Azure ML
	1.	Use serverless endpoints for inference
	2.	Choose smallest compute SKU
	3.	Set autoscaling with min=0
	4.	Use batch endpoints for non-real-time workloads
	5.	Stop or delete compute after use
	6.	Prefer CPU over GPU
	7.	Use spot instances for training
	8.	Clean up endpoints after class
