# Installing Prometheus using HELM

## Prerequisites

Before proceeding, ensure you have the following:

- Access to a Kubernetes cluster (version 1.16+ recommended)
- `kubectl` command-line tool configured to communicate with your cluster
- Helm 3 installed on your local machine

## Installation Steps

### 1. Install Prometheus

#### Add Prometheus Helm Repository

If you haven't added the Prometheus Helm repository yet, do so using the following command:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
## Deploy Prometheus

Create a namespace for Prometheus :

```
kubectl create namespace monitoring
```
Install Prometheus using Helm:

```
helm install prometheus prometheus-community/prometheus -n monitoring
```
## 2. Verify Prometheus Installation
Wait for all Prometheus components to be up and running. Check the pod status to ensure everything is deployed correctly:

```
kubectl get pods -n monitoring -l app=prometheus
```
## 3. Access Prometheus UI

To access the Prometheus web interface locally, set up port forwarding:

```
kubectl port-forward svc/prometheus-server -n monitoring 9090:80
```
Now, open your web browser and go to http://localhost:9090 to access the Prometheus UI.
