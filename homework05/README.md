## Homework 05: Using Redis and Flask Together

The objective of this project is to write and containerize a Flask application for that utilizes Redis. Two scripts are found in this repository:

* `app.py`: A Flask application that parses ISS positional and sighting data to return information about epochs, countries, regions, and cities through routes.
* `Dockerfile`: text file that contains all commands to build the image.
* `Makefile`: text file that contains shortcuts of commands to utilize in the command line.

### Running Instructions

The code must be run sequentially as follows.

#### Step 1: Retrieve JSON File

Use the following commands to retrieve `ML_Data_Sample.json` from the web. The JSON file is the data used by `app.py`.

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

The file is a JSON file that contains a dictionary with the key `meteorite_landings` that contains a list of dictionaries. Each dictionary contains seven keys and corresponding values. The keys are:

* `name`: the name of the meteorite
* `id`: the numerical ID of the meteorite
* `recclass`: the classification of the meteorite
* `mass (g)`: the mass of the meteorite, in grams
* `reclat`: the latitude of the location of the meteorite
* `reclong`: the longitude of the location of the meteorite
* `GeoLocation`: combines quanities in `reclat` and `reclong` into coordinate form

#### Step 2: Pull or Build Docker Image

```
$ make pull
```

Use the command above to pull and use he existing image on Docker Hub. The image is called `hw05` and the tag is `1.0`. The command `make pull` can be used because `docker build -t ${NAME}/hw05:1.0 .` is already in `Makefile`.

OR

```
$ docker build -t <username>/hw05:1.0 .
```

Use the command above to build the Docker image using the Dockerfile. Replace `<username>` with your Docker username.


#### Step 3: Run Redis Container

```
$ make run-redis
```

Use the command above the run the Redis container. The command `make run-redis` can be used because `docker run -d -p 6429:6379 -v $(pwd)/data:/data:rw --name=nikhil-redis redis:6 --save 1 1 -u 876850:816966` is already in `Makefile`. Each piece of the command serves a different purpose. The piece `docker run` calls for the Redis container to run. The tag `-d` runs the container in background and prints the container ID, while the tag `-p` publishes a container's ports to the host, which in this case publishes port 6429 to the host 6379. The tag `-v` bind mounts a volume to `$(pwd)/data:/data:rw`. The container ID is named using `--name=nikhil-redis`. Lastly, `redis:6` pulls the official Redis image for version 6, and `--save 1 1` saves one backup everyone 1 second.

#### Step 4: Run Flask Container

```
$ make run-flask
```

Use the command to build the Flask container. The command `make run-flask` can be used because of `docker run --rm -d -p 5029:5000 --name nikhil-flask ${NAME}/hw05:1.0`, which runs on the port 5029. To stop and rebuild the Flask container, use the following commands:

```
$ make stop
$ make run
```

#### Step 5: Use Flask Applicaton

```
$ curl localhost:5029/data -X POST
```

This will use the `POST` operation to load the data from file into memory. You must do this before using the next curl request.

```
$ curl localhost:5029/data
```

This will use the `GET` operation to get data about meteorite landings, returned as a JSON list.
