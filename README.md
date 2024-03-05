# Project: Backend/Infrastructure Engineer Challenge: Develop a key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue that can scale reliably across multiple pods/deployments. 

Brief description of your project.

## Getting Started

### Prerequisites

- Docker
- Kubernetes cluster (This can be a local cluster using Minikube or a cloud-based Kubernetes service)
- kubectl (configured to connect to your Kubernetes cluster)
- Docker Hub Account (Optional, if you plan to push your Docker image to Docker Hub)

### Building the Docker Image

First, you'll need to create a Docker image of your application. Here's how you can do that:

1. **Build Docker image**:

    ```sh
    docker-compose build
    ```

### Pushing the Docker Image to a Registry (Optional)

1. **Log in to the Docker Hub** from your command line:

    ```sh
    docker login --username=yourhubusername --email=youremail@company.com
    ```

2. **Push your image to the Docker Hub**:

    ```sh
    docker push yourusername/projectname:tag
    ```

### Deploying on Kubernetes

1. **Deploy your application to Kubernetes**:

    ```sh
    kubectl apply -f fastapi-deployment-service.yaml
    kubectl apply -f redis-deployment-service.yaml
    ```

2. **Accessing Your Application**:

    - If you're running your Kubernetes cluster locally (e.g., Minikube), you can make your application accessible by running:

        ```sh
        kubectl expose deployment fastapi-deployment --type=LoadBalancer --port=80
        ```

    - For cloud-based clusters, you might need to set up an Ingress or a LoadBalancer service depending on your cloud provider.

        ```sh
        minikube service fastapi-deployment
        ```
### accessing api
after everything done correctly you can go to <sytem's Kubernetes nad service host>:8000/<uri defined in main.py>

