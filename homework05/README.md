## Homework 05: Back to the Flask

The objective of this project is to write and containerize a Flask application for that utilizes Redis. Two scripts are found in this repository:

* `app.py`: A Flask application that parses ISS positional and sighting data to return information about epochs, countries, regions, and cities through routes.
* `Dockerfile`: text file that contains all commands to build the image.

### Running Instructions

The code must be run sequentially as follows.

#### Step 1: Retrieve JSON File

Use the following commands to retrieve `ML_Data_Sample.json` from the web. The JSON file is the data used by `app.py`.

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

#### Step 2: Pull or Build Docker Image

```
$ docker pull
```

Use the command above to pull and use he existing image on Docker Hub. The image is called `hw05` and the tag is `1.0`.

OR

```
$ docker build -t <username>/hw05:1.0 .
```

Use the command above to build the Docker image using the Dockerfile. Replace `<username>` with your Docker username.


#### Step 3: Run Docker Image

```
$ docker run -d -p 6429:6379 -v $(pwd):/data:rw --name=nikhil-redis redis:6 --save 1 1
```

Use the command above the run the Docker image.
    
#### Step 4: Use Flask Applicaton

```
$ curl localhost:5029/
```

Use the command above to run the Flask application `app.py`. This will provide information on how to interact with the application. In order to get information from the data, use the following command:

```
$ curl localhost:5029/data -X POST
```

This will use the `POST` operation to load the data from file into memory. Below is a list of commands that return information:
