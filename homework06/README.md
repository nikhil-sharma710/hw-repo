## Homework 06: Deploying a Test Environment in Kubernetes

The objective of this project was to use Kubernetes to deploy a test environment that can interact with the Flask application from Homework 05, which uses a Redis database to load and retrieve data. Seven scripts are found in this folder:

* `app.py`: A Flask application that parses ISS positional and sighting data to return information about epochs, countries, regions, and cities through routes.
* `Dockerfile`: text file that contains all commands to build the image.
* `nsharma-test-redis-pvc.yml`: A YAML file that stores data from the deployment file.
* `nsharma-test-redis-deployment.yml`: A YAML file that creates a deployment for the Redis database.
* `nsharma-test-redis-service.yml`: A YAML file that provides a persistent IP address to interact with the Redis database.
* `nsharma-test-flask-deployment.yml`: A YAML file that creates a deployment for the Flask application.
* `nsharma-test-flask-service.yml`: A YAML file that provides a persistent IP address to interact with the Flask application.

### Running Instructions

The code must be run sequentially in the Kubernetes cluster as follows.

#### Step 1: Retrieve JSON File

Use the following commands to retrieve `ML_Data_Sample.json` from the web. The JSON file is the data used by `app.py`.

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

#### Step 2: Apply a Configuration to Each YAML File

Make sure you create a Python debug deployment to use for testing the functionality of the program. Then, apply a configuration of each of the YAML files using the following command:

```
$ kubectl apply -f <file name>
```

#### Step 3: Retrieve Flask IP Address

Use the command below to retrieve the IP address for your Flask application. You will use the value under `CLUSTER-IP` later.

```
$ kubectl get services
NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
nsharma-flask-service   ClusterIP   10.100.200.144   <none>        5000/TCP   14h
```

#### Step 4: Retrieve Debug Deployment ID

Use the command below to retrieve the ID of the Python debug deployment. You will use the value under `NAME` to enter the pod.

```
$ kubectl get pods
NAME                                        READY   STATUS    RESTARTS        AGE
py-debug-deployment-5dfcf7bdd9-2wlv7        1/1     Running   0               13h
```

#### Step 5: Enter the Debug Pod

Use the command below to enter the debug pod. This is where you will be able to test the Flask application.

```
$ kubectl exec -it <debug pod ID> -- /bin/bash
```

#### Step 6: Run Applicaton

```
$ curl -X POST <Flask IP address>:5000/data
```

This will use the `POST` operation to load the data from file into memory. You must do this before using the next curl request. In place of `<Flask IP address>`, use the Flask IP address you found in Step 3.

```
$ curl <Flask IP address>:5000/data
```

This will use the `GET` operation to get data about meteorite landings, returned as a JSON list. In place of `<Flask IP address>`, use the Flask IP address you found in Step 3.
