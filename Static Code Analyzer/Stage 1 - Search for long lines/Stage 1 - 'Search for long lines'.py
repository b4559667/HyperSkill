u_input = input()


class StaticCodeAnalyzer:

    def __init__(self, file_path):
        self.error_codes = {"S001": "Too long"}
        self.file_path = file_path

    def long_lines(self):
        line_counter = 0
        with open(self.file_path, "r") as file:
            for line in file:
                line_counter += 1
                if len(line.strip()) > 79:
                    print(
                        "Line {line}: {code} {message}".format(line=line_counter, code=list(self.error_codes.keys())[0],
                                                               message=list(self.error_codes.values())[0]))


test = StaticCodeAnalyzer(u_input)
test.long_lines()