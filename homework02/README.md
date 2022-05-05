## Homework 02: Writing and Loading Data to and from a JSON File

The objective of this project was to become familiar with writing data to and loading data from files of common data formats, specifically JSON. The 

* `generate_sites.py`: a Python script that randomly generates data about meteorite landing sites and writes the data to a JSON file.
* `calculate_trip.py`: a Python script that reads the data from the file and calculates the total time of the trip.

### Running Instructions

The code must be run sequentially as follows.

#### Step 1: Generate and Load Data to JSON File

Use the following command to run `generate_sites.py`.

```
$ python3 generate_sites.py
```

The program creates a dictionary called `sites` that contains a list of dictionaries. Each sub-dictionary contains a site ID from 1 to 5, a latitude value from 16 to 18, a longitude value from 82 to 84, and a composition, which could be either stony, iron, or stony-iron. The dictionary is then uploaded to create a JSON file, `sites.json`, which contains all the data from the program.

#### Step 2: Read Data and Calculate Total Time

Use the following command to run `calculate_trip.py`.

```
$ python3 calculate_trip.py
```

The program calculates the travel time, the sample time, and the total time of the trip. This file imports `sites.json`. To calculate the distance, the great-circle distance algorithm is used. Each leg is summed up to find the total distance, and that value is divided by 10 km/h to find the travel time. The sample time is based on the composition of the site, lasting 1, 2, or 3 hours depending on if the composition is stony, iron, or stony-iron, respectfully. The times are summed to get the total sample time. Lastly, the times are added to get the total time.
