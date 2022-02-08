import json


def count(stop_name, stop_list):
    counter = 0
    for stop_ in stop_list:
        if stop_ == stop_name:
            counter += 1
    return counter


id_info_pair = {}
all_stops = []
start_stops = []
final_stops = []
transfer_stops = []
json_data = input()
for json_object in json.loads(json_data):
    id_info_pair.setdefault(json_object["bus_id"], [])
    id_info_pair[json_object["bus_id"]].append(json_object)

for key, value in id_info_pair.items():
    # if counter > 1 -> print error
    start_counter = 0
    finish_counter = 0
    for stop_type in value:
        if stop_type["stop_type"] == "S":
            start_counter += 1
        if stop_type["stop_type"] == "F":
            finish_counter += 1
    if start_counter != 1 or finish_counter != 1:
        print("There is no start or end stop for the line: {}.".format(key))
        break

for info in json.loads(json_data):
    all_stops.append(info["stop_name"])
    if info["stop_type"] == "S":
        start_stops.append(info["stop_name"])
    elif info["stop_type"] == "F":
        final_stops.append(info["stop_name"])
for stop in set(all_stops):
    if count(stop, all_stops) > 1:
        transfer_stops.append(stop)
start_stops = sorted(list(set(start_stops)))
transfer_stops = sorted(list(set(transfer_stops)))
final_stops = sorted(list(set(final_stops)))

print("Start stops:", len(start_stops), start_stops)
print("Transfer stops:", len(transfer_stops), transfer_stops)
print("Finish  stops:", len(final_stops), final_stops)
