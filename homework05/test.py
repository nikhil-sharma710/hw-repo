import json
import redis

rd = redis.Redis(host='172.17.0.24', port=6429, db=29)

ml_data = {}

def read_data():
    return json.load(open('ML_Data_Sample.json', 'r'))

def load_redis(data):
    for d in data:
        rd.hset(d['id'], mapping=d)

def get_keys():
    return rd.keys()

if __name__ == "__main__":
    d = read_data()
    load_redis(d['meteorite_landings'])
    print(get_keys())
