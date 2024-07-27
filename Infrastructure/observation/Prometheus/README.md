# Installing Grafana using HELM

## 1. install Grafana
Add Grafana Helm Repository

If you haven't added the Grafana Helm repository yet, do so using the following command:

```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```
Deploy Grafana

Install Grafana using Helm:

```
helm install grafana grafana/grafana -n monitoring
```

## 2. Verify Grafana Installation
Wait for all Grafana components to be up and running. Check the pod status to ensure everything is deployed correctly:

```
kubectl get pods -n monitoring -l app.kubernetes.io/name=grafana
```
## 3. access grafana dashboard

Retrieve Grafana Admin Password

Retrieve the default admin password for Grafana:

```
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Access Grafana Web UI

To access the Grafana web interface locally, set up port forwarding:

```
kubectl port-forward svc/grafana -n monitoring 3000:80
```
Now, open your web browser and go to http://localhost:3000 to access the Grafana login page. Use admin as the username and the password retrieved earlier to log in.

after siging in you should be able to use the grafna dashboard 

