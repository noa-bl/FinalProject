
# Jenkins server establishment on docker-desktop

Running a Jenkins server on your Docker Desktop Kubernetes cluster using Helm is a straightforward process.

  

## Steps:

### Step 1: Install Helm

First, you need to have Helm installed on your system. If you haven't installed it yet, you can follow these instructions:

  

For Windows, you can download Helm using Chocolatey:

```sh

brew install  helm

```

  

Verify Helm Installation:

  

```sh

helm version

```

  

### Step 2: Add Jenkins Helm Repository

Add the Jenkins Helm chart repository to your Helm configuration:

  

```sh

helm repo  add  jenkins  https://charts.jenkins.io

  

helm repo  update

```

  

### Step 3: Install Jenkins Using Helm

Now you can install Jenkins using the Helm chart.

It's a good practice to create a separate namespace for Jenkins.

Here’s how you can do it with default settings:

```sh

helm upgrade  --install  myjenkins  jenkins/jenkins  --namespace  jenkins  --create-namespace

```

### Step 4: Monitor the Deployment

Check the status of the Jenkins pods to ensure they are running:

```sh

kubectl get  pods  --namespace  jenkins  --watch

```

You should see the Jenkins pod listed with a status of Running after few minutes.

  

### step 5: Retrieve the Admin Password

The Jenkins admin password is stored in a Kubernetes secret. Retrieve it using:

```sh

kubectl exec  --namespace  jenkins  -it  myjenkins-0  --  cat  /run/secrets/additional/chart-admin-password

```

  

### step 6: Change jenkins ip type

change jenkins from clusterip to nodeport to access the Jenkins UI:

```sh

kubectl edit  svc  myjenkins  -n  jenkins

```

swith to type NodePort save and quit

  

### step 7: Access jenkins

Browse into the jenkins web and enter with the admin password above:

```sh

localhost:8080

```

  

### step 8: Install plugins

Now, let's install the relevant plugins:

  

- kubernetes

- workflow-aggregator

- git

- configuration-as-code

- gitlab-plugin

- blueocean

- workflow-multibranch

- login-theme

- prometheus

- github-oauth

  
note: you should install suggested plugins on first login

  


```