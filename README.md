# Flask REST API Project

## Project Description

This project is a Flask-based REST API that includes features like domain lookup, IP validation, and query history retrieval. It also integrates health checks and Prometheus metrics. The project is containerized using Docker and supports Kubernetes deployments via Helm charts. A CI pipeline is included for continuous integration and deployment.

## Prerequisites

Ensure that you have the following installed on your system:

- **Docker**: To containerize the application.
- **Docker Compose**: To orchestrate multi-container Docker applications.
- **Python 3.11**: Required for local development (if needed).
- **MySQL**: The application uses MySQL as the database.
- **Helm**: For Kubernetes deployment with Helm charts.

## Project Setup

### 1. Clone the Repository

First, clone the project repository from your version control system (e.g., GitHub):

```bash
git clone https://github.com/your-repo/flask-rest-api-project.git
cd flask-rest-api-project
