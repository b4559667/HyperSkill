import re
import sys
import os


class StaticCodeAnalyzer:

    def __init__(self, file_path):
        self.list_ = []
        self.line_counter = 0
        self.error_codes = {"S001": "Too long line",
                            "S002": "Indentation is not a multiple of four",
                            "S003": "Unnecessary semicolon",
                            "S004": "Less than two spaces before inline comments",
                            "S005": "TODO found",
                            "S006": "More than two blank lines preceding a code line",
                            "s007": "Too many spaces after construction_name",
                            "s008": "Class name should be written in CamelCase",
                            "s009": "Function name should be written in snake_case"}
        self.file_path = file_path

    def create_message(self, index):
        self.list_.append("{path}: Line {line}: {code} {message}".format(line=self.line_counter,
                                                                         code=list(self.error_codes.keys())[index],
                                                                         message=list(self.error_codes.values())[index],
                                                                         path=self.file_path))

        def sort(s):
            return int(re.search(r"Line(.*?):", s).group(1))

        self.list_.sort(key=sort)

    def s001(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if len(line.strip()) > 79:
                    self.create_message(0)
        self.line_counter = 0

    def s002(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if len(line.split()) == 0:
                    continue
                if len(re.match(r"^\s*", line)[0]) % 4 != 0:
                    self.create_message(1)
        self.line_counter = 0

    def s003(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if line.startswith("#"):
                    continue
                elif "#" in line:
                    if line.split("#")[0].strip().endswith(";"):
                        self.create_message(2)
                elif line.strip().endswith(";"):
                    self.create_message(2)
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
                        self.create_message(3)
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
                        self.create_message(4)
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
                        self.create_message(5)
                if len(line.strip()) > 0:
                    empty_counter = 0
        self.line_counter = 0

    def s007(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if re.match(r"def\s{2,}", line.strip()):
                    self.create_message(6)
                if re.match(r"class\s{2,}", line.strip()):
                    self.create_message(6)
        self.line_counter = 0

    def s008(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if line.strip().startswith("class"):
                    if re.match(r"class\s*([A-Z]\w+[A-Z]\w+)|class\s([A-Z]\w*\()", line.strip()) is None:
                        self.create_message(7)
                else:
                    continue
        self.line_counter = 0

    def s009(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.line_counter += 1
                if line.strip().startswith("def"):
                    if re.match(r"def\s*[a-z]*_\w*\(|def\s*__|def\s*[a-z]*\(", line.strip()) is None:
                        self.create_message(8)
                else:
                    continue
        self.line_counter = 0


def main():
    def run(f_path):
        test = StaticCodeAnalyzer(f_path)
        test.s001()
        test.s002()
        test.s003()
        test.s004()
        test.s005()
        test.s006()
        test.s007()
        test.s008()
        test.s009()
        for result in test.list_:
            print(result)

    args = sys.argv
    if args[1].endswith(".py"):
        run(args[1])
    else:
        for dirpath, dirnames, files in os.walk(args[1]):
            for file_name in files:
                full_path = dirpath + "\\" + file_name
                run(full_path)


if __name__ == "__main__":
    main()