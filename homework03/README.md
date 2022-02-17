## Homework 03: A Space Turbidity

The objective of this project is to simulate the operation of a robotic vehicle on Mars. Two scripts are found within:

* `analyze_water.py`: used to calculate the turbidity of water and to notify the user if the turbidity is below the threshold. If it is not, the program calculates the minimum time to fall below threshold turbidity.
* `test_analyze_water.py`: used to run five tests using methods from `analyze_water.py`.

### Running Instructions

The code must be run sequentially in three steps.

#### Step 1:

```
$ wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

Use the command above to add a JSON file (`turbidity_data.json`) to the repository from the internet.

#### Step 2:

```
$ python3 analyze_water
```

After generating the output (`sites.json`), run the second script `calculate_trip.py`.
It imports `sites.json` and uses the great-circle distance algorithm to calculate
the travel time, the sample time, and the total time of the trip, given that a robot
travels 10km/h and the sample time lasts 1, 2, or 3 hours  based on meteorite
composition. All output are printed to the screen
