import json
import logging
import math

logging.basicConfig(level = logging.INFO, format = '%(levelname)s: %(message)s')

def create_new_list(turbidity_data: list) -> list:
    """
    This function takes the list, turbidity_data, and creates a new list of the five most recent dictionaries.
    
    Args:
        turbidity_data (list): This list is a list of dictionaries of hourly data about turbidity of water.
        
    Returns:
        most_recent (list): The function returns a list of five dictionaries, being the five most recent from the data.
    """
    
    most_recent = []
    
    for i in range(5):
        most_recent.append(turbidity_data['turbidity_data'][len(turbidity_data) - (6 - i)])
        
    return most_recent

def average_values(most_recent: list) -> float:
    """
    This function returns the average turbidity of the water based on the five most recent recordings in the data.
    
    Args:
        most_recent (list): This list is a list of the five most recent dictionaries from the data.
        
    Returns:
        average_turbidity (float): The function returns a float of the average turbidity of the five most recent recordings.
    """
    
    total = 0

    for i in range(5):
        total += calculate_turbidity(most_recent[i], 'calibration_constant', 'detector_current')
        
    average_turbidity = total/5
    return average_turbidity

def calculate_turbidity(dictionary: dict, a0: str, I90: str) -> float:
    """
    This function calculates the turbidity of the water, using the formula T = a0*I90.
    
    Args:
        dictionary (dict): The first argument is a specific dictionary whose calibration constant and detector current are multiplied.
        a0 (str): The second argument is a key string to find the calibration constant.
        I90 (str): The third argument is a key string to find the 90 degree detector current.
        
    Returns:
        T (float): The function returns the turbidity of the water.
    """

    T = dictionary[a0]*dictionary[I90]
    return T

def calculate_minimum_time(Ts: float, T0: float, d: float) -> float:
    """
    This function calculates the minimum time to fall below threshold turbidity, using the inequality Ts > T0(1 - d)^b.
    
    Args:
        Ts (float): The first argument is the turbidity threshold for safe water.
        T0 (float): The second argument is the current turbidity.
        d (float): The third argument is the decay factor per hour, expressed as a decimal.

    Returns:
        b (float): The function returns the minimum time to fall below threshold turbidity.
    """

    b = math.log(Ts/T0, 1 - d)
    return b

def main():
    with open('turbidity_data.json', 'r') as f:
        turbidity_data = json.load(f)
    
    print('Average turbidity based on most recent five measurements = ' + average_values(most_recent) + ' NTU')

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
