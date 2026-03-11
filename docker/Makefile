# Spam Classifier Docker Configuration
# =====================================

# Image settings
IMAGE_NAME ?= spam-classifier
IMAGE_TAG ?= latest
CONTAINER_NAME ?= spam-classifier-ui
PORT ?= 8080

# Docker registry (optional)
REGISTRY ?= 

# Full image reference
ifdef REGISTRY
	FULL_IMAGE = $(REGISTRY)/$(IMAGE_NAME):$(IMAGE_TAG)
else
	FULL_IMAGE = $(IMAGE_NAME):$(IMAGE_TAG)
endif

.PHONY: help build run stop logs shell test clean push pull

# Default target
help:
	@echo "Spam Classifier Docker Commands"
	@echo "================================"
	@echo ""
	@echo "  make build    - Build the Docker image"
	@echo "  make run      - Run the container"
	@echo "  make stop     - Stop and remove the container"
	@echo "  make logs     - View container logs"
	@echo "  make shell    - Open a shell in the container"
	@echo "  make test     - Test the app health check"
	@echo "  make clean    - Remove image and container"
	@echo "  make push     - Push image to registry"
	@echo "  make pull     - Pull image from registry"
	@echo ""
	@echo "Variables:"
	@echo "  IMAGE_NAME=$(IMAGE_NAME)"
	@echo "  IMAGE_TAG=$(IMAGE_TAG)"
	@echo "  PORT=$(PORT)"
	@echo "  REGISTRY=$(REGISTRY)"

# Build the Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(FULL_IMAGE) .
	@echo "Image built: $(FULL_IMAGE)"

# Run the container
run:
	@echo "Starting container..."
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8080 \
		--restart unless-stopped \
		$(FULL_IMAGE)
	@echo "Container started at http://localhost:$(PORT)"

# Run in foreground (for debugging)
run-fg:
	@echo "Starting container in foreground..."
	docker run --rm \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8080 \
		-e DEBUG=true \
		$(FULL_IMAGE)

# Stop and remove the container
stop:
	@echo "Stopping container..."
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)
	@echo "Container stopped"

# View container logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Open a shell in the running container
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Test the application health check
test:
	@echo "Testing health endpoint..."
	@curl -s http://localhost:$(PORT)/_stcore/health
	@echo ""

# Clean up image and container
clean: stop
	@echo "Removing image..."
	-docker rmi $(FULL_IMAGE)
	@echo "Cleanup complete"

# Push to registry
push:
ifndef REGISTRY
	$(error REGISTRY is not set. Use: make push REGISTRY=your-registry.com)
endif
	@echo "Pushing to $(REGISTRY)..."
	docker push $(FULL_IMAGE)

# Pull from registry
pull:
ifndef REGISTRY
	$(error REGISTRY is not set. Use: make pull REGISTRY=your-registry.com)
endif
	@echo "Pulling from $(REGISTRY)..."
	docker pull $(FULL_IMAGE)

# Build for multiple architectures (requires docker buildx)
build-multi:
	@echo "Building multi-architecture image..."
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		-t $(FULL_IMAGE) \
		--push \
		.
