import json
import logging
import math

logging.basicConfig(level = logging.INFO)

def calculate_turbidity(a0: float, I90: float) -> float:
    """

    """

    T = a0*I90
    return T

def calculate_minimum_time(Ts: float, T0: float, d: float) -> float:
    """

    """

    b = math.log(Ts/T0, 1 - d)
    return b

def main():
    with open('turbidity_data.json', 'r') as f:
        turbidity_data = json.load(f)

    most_recent = []
    turbidity_values = []
    total = 0

    for i in range(5):
        most_recent.append(turbidity_data['turbidity_data'][len(turbidity_data) - (6 - i)])
        total += calculate_turbidity(most_recent[i]['calibration_constant'], most_recent[i]['detector_current'])

    average_turbidity = total/5
    print('Average turbidity based on most recent five measurements = ' + str(average_turbidity) + ' NTU')

    threshold = 1.0
    decay_factor = 0.02
    minimum_time = 0

    if (average_turbidity > threshold):
        logging.warning('Turbidity is above threshold for safe use')
        minimum_time = calculate_minimum_time(threshold, average_turbidity, decay_factor)
    else:
        logging.info('Turbidity is below threshold for safe use')

    print('Minimum time required to return below a safe threshold = ' + str(minimum_time) + ' hours')

if __name__ == "__main__":
    main()
