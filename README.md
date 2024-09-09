# Flask REST API Project

## Project Description

A REST API that includes features like domain lookup, IP validation, and query history retrieval.
It also integrates health checks and Prometheus metrics.
The project is containerized using Docker and supports Kubernetes deployments via Helm charts.
A CI pipeline is included for continuous integration and deployment.

## Prerequisites

To be installed on the system:

- **Docker**: To containerize the application.
- **Docker Compose**: To orchestrate multi-container Docker applications.
- **Python 3.11**: Required for local development.
- **MySQL**: The application uses MySQL as the database.
- **Helm**: For Kubernetes deployment with Helm charts.

## Project Setup

### 1. Clone the Repository

First, clone the project repository from your version control system:

```bash
git clone https://github.com/your-repo/flask-rest-api-project.git
cd flask-rest-api-project
```

### 2. Set Up Environment Variables

MySQL credentials should be stored in environment variables or secrets

```bash
export MYSQL_ROOT_PASSWORD=root_password
export MYSQL_DATABASE=db_name
export MYSQL_USER=db_user
export MYSQL_PASSWORD=db_password
```

### 3. Docker and Docker Compose Setup

#### 1. Build and start the containers:

```bash
docker-compose up -d --build

#### 2. Check the containers:

```bash
docker-compose ps
```

#### 3. Access the application:

Open your browser and navigate to http://localhost:3000/.
Access the Prometheus metrics at http://localhost:3000/metrics.
Perform health checks at http://localhost:3000/health.

##### Stop and remove the containers:

```bash
docker-compose down
```


### 4. Kubernetes Deployment with Helm

#### 1. Deploy the application using Helm charts.

```bash
helm package helm-chart/
```

#### 2. Install the Helm chart:

```bash
helm install my-flask-app ./helm-chart
```

#### 3. Check the pods:

```bash
kubectl get pods
```

#### 4. Upgrade the Helm chart:

```bash
helm upgrade my-flask-app ./helm-chart
```

#### 5. Rollback the Helm chart:

```bash
helm rollback my-flask-app
```


### 5. CI Pipeline with GitHub Actions

#### 1. Set Up Secrets

#### 2. Trigger the Pipeline:

```bash
git commit -am "Initial commit"
git push origin master
```


### 6. Running Tests Locally

Run the tests locally using pytest

```bash
pytest
```

### 7. Cleanup

#### Docker: To clean up Docker resources use:

```bash
docker-compose down --rmi all --volumes
```

#### Helm: To clean up Helm resources, use:

```bash
helm uninstall my-flask-app
```
