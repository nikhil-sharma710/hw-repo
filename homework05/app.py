from flask import Flask
import json
import redis

app = Flask(__name__)
rd = redis.Redis(host='172.17.0.24', port=6429, db=29)

ml_data = {}

@app.route('/data', methods=['GET', 'POST'])
def data():
    """
    This function reads a JSON file and converts it into dictionary.
    
    Args:
        None
    
    Returns:
        None
    """

    global ml_data

    if request.method == 'POST':
        with open('ML_Data_Sample.json', 'r') as f:
            ml_data = json.load(f)
    
        for i in range(len(ml_data)):
            rd.set(str(i), ml_data['meteorite_landings']][i])
    else:
        output = ""
        for i in range(len(ml_data)):
            output+=str(rd.get(str(i), ml_data[i]).decode('utf-8')\n)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
