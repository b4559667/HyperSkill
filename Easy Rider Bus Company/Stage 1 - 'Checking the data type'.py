import json

test_string_ = input()


class EasyRider:
    error_counter = 0

    def __init__(self, json_string):
        self.json_string = json.loads(json_string)
        self.data_structure = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}

    def create_message(self):
        print("Type and required field validation: {} errors".format(EasyRider.error_counter))
        for key, value in self.data_structure.items():
            print(key + ":", value)

    def unpack(self):
        for object_ in self.json_string:
            if not isinstance(object_["bus_id"], int) or object_["bus_id"] == "":
                self.data_structure["bus_id"] += 1
                EasyRider.error_counter += 1
            if not isinstance(object_["stop_id"], int) or object_["stop_id"] == "":
                self.data_structure["stop_id"] += 1
                EasyRider.error_counter += 1
            if not isinstance(object_["stop_name"], str) or object_["stop_name"] == "":
                self.data_structure["stop_name"] += 1
                EasyRider.error_counter += 1
            if not isinstance(object_["next_stop"], int) or object_["next_stop"] == "":
                self.data_structure["next_stop"] += 1
                EasyRider.error_counter += 1
            if not isinstance(object_["stop_type"], str):
                self.data_structure["stop_type"] += 1
                EasyRider.error_counter += 1
            if isinstance(object_["stop_type"], str):
                if len(object_["stop_type"]) not in range(0, 2):
                    self.data_structure["stop_type"] += 1
                    EasyRider.error_counter += 1
            if not isinstance(object_["a_time"], str) or object_["a_time"] == "":
                self.data_structure["a_time"] += 1
                EasyRider.error_counter += 1


def main():
    test = EasyRider(test_string_)
    test.unpack()
    test.create_message()


if __name__ == "__main__":
    main()
