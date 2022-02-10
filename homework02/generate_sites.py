import random
import json

def create_list():
    site_id = [1,2,3,4,5]
    latitude  = []
    longitude = []
    composition_list = ["stony","iron","stony-iron"]
    composition = []

    for i in range(5):
        latitude.append(random.random()*2 + 16)
        longitude.append(random.random()*2 + 82)
        composition.append(composition_list[random.randint(0,2)])

    list_of_dicts = []

    for i in range(5):
        dicts = {
            "site_id": site_id[i],
            "latitude": latitude[i],
            "longitude": longitude[i],
            "composition": composition[i]
        }

        list_of_dicts.append(dicts)

    return list_of_dicts

def main():
    list_of_dicts = create_list()
    dictionary = {
        "sites": list_of_dicts
    }

    json_object = json.dumps(dictionary, indent = 4)
    
    with open("sites.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    main()
