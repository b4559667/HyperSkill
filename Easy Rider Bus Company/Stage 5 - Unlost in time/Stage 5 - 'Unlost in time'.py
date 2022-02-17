import json

id_time = {}
check = True
json_data = input()
print("Arrival time test:")
for json_object in json.loads(json_data):
    id_time.setdefault(json_object["bus_id"], [])
    id_time[json_object["bus_id"]].append(json_object)
for key, value in id_time.items():
    last_time = value[0]["a_time"]
    for j in value[1:]:
        if last_time > j["a_time"]:
            check = False
            print("bus_id line {}: wrong time on station {}".format(key, j['stop_name']))
            break
        last_time = j["a_time"]
if check:
    print("OK")
