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

After the turbidity, the logging message, and the minimum time are printed, run `test_analyze_water.py`. It runs five unit tests with `pytest` to ensure the math is correct in the functions, the argument types are valud, and the return types are valid. The first test sees if the output of the `calculate_turbidity` function is mathematically accurate, using sample data. The second test checks if `calculate_turbidity` returns a float. The third test sees if the output of `calculate_minimum_time` is mathematically accurate, using sample data. The fourth test sees if `calculate_minimum_time` returns a float. The final test catches a TypeError as the input for the function should be three floats, and the first argument of the test is a string. If nothing is printed, then all five tests passed.
