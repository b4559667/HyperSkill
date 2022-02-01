import re


class StaticCodeAnalyzer:

    def __init__(self, file_path):
        self.list_ = []
        self.line_counter = 0
        self.error_codes = {"S001": "Too long line",
                            "S002": "Indentation is not a multiple of four",
                            "S003": "Unnecessary semicolon",
                            "S004": "Less than two spaces before inline comments",
                            "S005": "TODO found",
                            "S006": "More than two blank lines preceding a code line"}
        self.file_path = file_path

    def print_message(self, index):
        self.list_.append("Line {line}: {code} {message}".format(line=self.line_counter,
                                                                 code=list(self.error_codes.keys())[index],
                                                                 message=list(self.error_codes.values())[index]))

        def sort(s):
            return int(re.search(r"\s(.*?):", s).group(1))

        self.list_.sort(key=sort)

    def s001(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if len(line.strip()) > 79:
                    self.print_message(0)
        self.line_counter = 0

    def s002(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if len(line.split()) == 0:
                    continue
                if len(re.match(r"^\s*", line)[0]) % 4 != 0:
                    self.print_message(1)
        self.line_counter = 0

    def s003(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if line.startswith("#"):
                    continue
                elif "#" in line:
                    if line.split("#")[0].strip().endswith(";"):
                        self.print_message(2)
                elif line.strip().endswith(";"):
                    self.print_message(2)
        self.line_counter = 0

    def s004(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                try:
                    index_ = line.index("#")
                    if index_ == 0:
                        continue
                    elif line[index_ - 2:index_] != "  ":
                        self.print_message(3)
                except ValueError:
                    continue
        self.line_counter = 0

    def s005(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                try:
                    index_ = line.index("#")
                    if "todo" in line[index_:].lower():
                        self.print_message(4)
                except ValueError:
                    continue
        self.line_counter = 0

    def s006(self):
        with open(self.file_path, "r") as file:
            empty_counter = 0
            for line in file:
                self.line_counter += 1
                if len(line.strip()) == 0:
                    empty_counter += 1
                if empty_counter > 2:
                    if len(line.strip()) > 0:
                        self.print_message(5)
                if len(line.strip()) > 0:
                    empty_counter = 0
        self.line_counter = 0


def main():
    u_input = input()
    test = StaticCodeAnalyzer(u_input)
    test.s001()
    test.s002()
    test.s003()
    test.s004()
    test.s005()
    test.s006()
    for result in test.list_:
        print(result)


if __name__ == "__main__":
    main()