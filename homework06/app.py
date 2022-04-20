from flask import Flask, request
import json
import redis
import os

redis_ip = os.environ.get('REDIS_IP')
app = Flask(__name__)
rd = redis.Redis(host=redis_ip, port=6379, db=0)

@app.route('/data', methods=['GET', 'POST'])
def data():
    """
    If the request method is POST, this function reads a JSON file and converts it into dictionary. If the request method is GET, the function returns a JSON list of the meteorite landing data.
    
    Args:
        None
    
    Returns:
        If request.method == 'POST', the function returns a string stating the data was loaded from the file.
        If request.method =- 'GET', the function returns a JSON list of meteorite landing data.
    """

    ml_data = {}

    if request.method == 'POST':
        with open('ML_Data_Sample.json', 'r') as f:
            ml_data = json.load(f)
    
        for i in range(len(ml_data['meteorite_landings'])):
            rd.set(str(i), json.dumps(ml_data['meteorite_landings'][i]))

        return "Data loaded from file\n"
    else:
        ml_data = {}
        ml_data['meteorite_landings'] = []
        
        for i in rd.keys():
            ml_data['meteorite_landings'].append(json.loads(rd.get(i).decode('utf-8')))

        return (json.dumps(ml_data, indent = 2))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
