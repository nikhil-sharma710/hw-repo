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

.. code-block:: console

   [isp02]$ ./ml_data_analysis Meteorite_Landings.json
   Summary data following meteorite analysis:

   Average mass of 30 meteor(s):
   83857.3 grams

   Hemisphere summary data:
   There were 21 meteors found in the Northern & Eastern quadrant
   There were 6 meteors found in the Northern & Western quadrant
   There were 0 meteors found in the Southern & Eastern quadrant
   There were 3 meteors found in the Southern & Western quadrant

   Class summary data:
   The L5 class was found 1 times
   The H6 class was found 1 times
   The EH4 class was found 2 times
   The Acapulcoite class was found 1 times
   The L6 class was found 6 times
   ... etc

Use the command above to run the program `ml_data_analysis.py` using the data fromm `Meteorite_Landings.json`. The program will summarize the findings from each of the sites listed in the data, including the average mass of each meteorite, the amount of meteorites that land in each quadrant (Northeastern, Northwestern, Southeastern, Southwestern), and the amount of each class of meteorites that occurs. If you'd like to download your own data, such as the sample data `ML_Data_Sample.json`, use the following command:

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

This will add the JSON file `ML_Data_Sample.json` to the repository. To run `ml_data_analysis.py` with the new data, replace `Meteorite_Landings.json` with `ML_Data_Sample.json` as so:

```
$ ./ml_data_analysis.py ML_Data_Sample.json
```

If you would like to use your own data, it would have to be in the following format as a JSON file:

{
  "meteorite_landings": [
    {
      "name": "",
      "id": "",
      "recclass": "",
      "mass (g)": "",
      "reclat": "",
      "reclong": "",
      "GeoLocation": ""
    },
    {
      "name": "",
      "id": "",
      "recclass": "",
      "mass (g)": "",
      "reclat": "",
      "reclong": "",
      "GeoLocation": ""
    },
    ...
  ]
  
}
    
#### Step 4:

```
$ python3 test_ml_data_analysis.py
```

Use the command above to run the containerized suite with pytest. It runs five tests for each of the methods in `ml_data_analysis.py` while using sample data. There should be no output as the code is error-free.
