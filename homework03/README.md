## Homework 03: Implementing Good Practices for Programming

The objective of this project is to check the latest water quality data to assess whether it is safe to analyze samples. It implements the concepts of doc strings, code organization, unit testing, and logging messages. Two scripts are found in this folder:

* `analyze_water.py`: used to calculate the turbidity of water and to notify the user if the turbidity is below the threshold. If it is not, the program calculates the minimum time to fall below threshold turbidity.
* `test_analyze_water.py`: used to run five tests, checking methods from `analyze_water.py`.

### Running Instructions

The code must be run sequentially in three steps.

#### Step 1: Retrieve JSON File

```
$ wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

Use the command above to add a JSON file (`turbidity_data.json`) to the repository from the internet.

#### Step 2: Run Program

```
$ python3 analyze_water.py
```

After downloading the JSON file, run the script `analyze_water.py`. It imports `turbidity_data.json` and takes the five most recent readings to calculate the average turbidity of them. If the turbidity is below the threshold of 1.0 NTU, an informational message is printed stating the water is safe for use. If the turbidity is above the threshold, a warning message is printed stating that a certain time must elapse before the water is safe for use. The minimum time is then calculated using a formula, and if the water is safe, the result is 0 hours.

#### Step 3: Run Test Program

```
$ python3 test_analyze_water.py
```

After the turbidity, the logging message, and the minimum time are printed, run `test_analyze_water.py`. It runs five unit tests with `pytest` to ensure the math is correct in the functions, the argument types are valud, and the return types are valid. The first test sees if the output of the `calculate_turbidity` function is mathematically accurate, using sample data. The second test checks if `calculate_turbidity` returns a float. The third test sees if the output of `calculate_minimum_time` is mathematically accurate, using sample data. The fourth test sees if `calculate_minimum_time` returns a float. The final test catches a TypeError as the input for the function should be three floats, and the first argument of the test is a string. If nothing is printed, then all five tests passed.
