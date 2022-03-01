## Homework 04: Once Upon a Time in Containers

The objective of this project is to package the contents of a repository into a container using Docker commands. Five scripts are found within:

* `ml_data_analysis.py`: used to calculate the average mass of meteorites, the amount of meteorites that land in each quadrant, and the amount of each class of meteorites that occurs.
* `test_ml_data_analysis.py`: contains three methods each with five tests to check functionality of methods from `ml_data_analysis.py`.
* `Meteorite_Landings.json`: contains data for meteorite landings, such as name, ID, class, mass, longitude, and latitude.
* `Dockerfile`: text file that contains all commands to build the image.

### Running Instructions

The code must be run sequentially as follows.

#### Step 1:

```
$ docker pull nikhilsharma710/ml_data_analysis:hw04
```

Use the command above to pull and use the existing image on Docker Hub. The image is called `ml_data_analysis` and the tag is `hw04`.

#### Step 2:

```
$ docker build -t nikhilsharma710/ml_data_analysis:hw04 .
```

Use the command above to build the Docker image using the Dockerfile.

#### Step 3:

```
$ ./ml_data_analysis.py Meteorite_Landings.json
```

Use the command above to run the program `ml_data_analysis.py` using the data fromm `Meteorite_Landings.json`. The program will summarize the findings from each of the sites listed in the data, including the average mass of each meteorite, the amount of meteorites that land in each quadrant (Northeastern, Northwestern, Southeastern, Southwestern), and the amount of each class of meteorites that occurs. If you'd like to download your own data, such as the sample data `ML_Data_Sample.json`, use the following command:

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

This will add the JSON file `ML_Data_Sample.json` to the repository. To run `ml_data_analysis.py` with the new data, replace `Meteorite_Landings.json` with `ML_Data_Sample.json` as so:

```
$ ./ml_data_analysis.py ML_Data_Sample.json
```
