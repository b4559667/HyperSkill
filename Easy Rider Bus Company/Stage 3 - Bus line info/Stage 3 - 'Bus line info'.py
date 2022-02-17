import json
import re
from collections import Counter

json_input = input()


class EasyRider:
    error_counter = 0
    stop_name_pattern = re.compile(r"^[A-Z].+\s(Road|Avenue|Boulevard|Street)$")
    stop_type_pattern = re.compile(r"(^[SOF]$)|(^$)")
    a_time_pattern = re.compile(r"^([01]\d|2[0-3]):?([0-5]\d)$")

    def __init__(self, json_string):
        self.json_string = json.loads(json_string)
        self.data_structure = {"stop_name": 0, "stop_type": 0, "a_time": 0}
        self.stops = []

    def create_message(self):
        tmp_list = []
        result = {}
        for list_ in self.stops:
            tmp_list.append(list_[0])
        freq_collection = Counter(tmp_list)
        for pair in freq_collection:
            result[pair] = freq_collection[pair]
        for key, value in result.items():
            print("bus_id:", str(key) + ",", "stops:", value)

    def bus_id_check(self, object_):
        if not isinstance(object_["bus_id"], int) or object_["bus_id"] == "":
            self.data_structure["bus_id"] += 1
            EasyRider.error_counter += 1

    def stop_id_check(self, object_):
        if not isinstance(object_["stop_id"], int) or object_["stop_id"] == "":
            self.data_structure["stop_id"] += 1
            EasyRider.error_counter += 1

    def stop_name_check(self, object_):
        if not isinstance(object_["stop_name"], str) or object_["stop_name"] == "":
            self.data_structure["stop_name"] += 1
            EasyRider.error_counter += 1
        if not re.match(EasyRider.stop_name_pattern, object_["stop_name"]):
            self.data_structure["stop_name"] += 1
            EasyRider.error_counter += 1

    def next_stop_check(self, object_):
        if not isinstance(object_["next_stop"], int) or object_["next_stop"] == "":
            self.data_structure["next_stop"] += 1
            EasyRider.error_counter += 1

    def stop_type_check(self, object_):
        if not re.match(EasyRider.stop_type_pattern, object_["stop_type"]):
            self.data_structure["stop_type"] += 1
            EasyRider.error_counter += 1

    def a_time_check(self, object_):
        if not isinstance(object_["a_time"], str) or object_["a_time"] == "":
            self.data_structure["a_time"] += 1
            EasyRider.error_counter += 1
        if not re.match(EasyRider.a_time_pattern, object_["a_time"]):
            self.data_structure["a_time"] += 1
            EasyRider.error_counter += 1

    def run(self):
        for object_ in self.json_string:
            EasyRider.bus_id_check(self, object_)
            EasyRider.stop_id_check(self, object_)
            EasyRider.stop_name_check(self, object_)
            EasyRider.next_stop_check(self, object_)
            EasyRider.stop_type_check(self, object_)
            EasyRider.a_time_check(self, object_)
            self.stops.append([object_["bus_id"], object_["stop_id"]])


def main():
    test = EasyRider(json_input)
    test.run()
    test.create_message()


if __name__ == "__main__":
    main()
