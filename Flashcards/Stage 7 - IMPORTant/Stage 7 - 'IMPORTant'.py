import os
import pickle
import random
import io
import argparse


class Flashcards:

    def __init__(self):
        self.flashcards_storage = {}
        self.mistakes = {}
        self.mem_file = io.StringIO()
        self.args_filename = None

    def run(self):
        self.mem_file.read()
        while True:
            print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            self.mem_file.write(
                "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):" + "\n")
            user_input = input()
            self.mem_file.write(user_input + "\n")
            if user_input == "add":
                Flashcards.add_card(self)
            elif user_input == "remove":
                Flashcards.remove_card(self)
            elif user_input == "import":
                Flashcards.import_cards(self)
            elif user_input == "export":
                Flashcards.export_cards(self)
            elif user_input == "ask":
                Flashcards.ask_number(self)
            elif user_input == "exit":
                Flashcards.exit(self)
            elif user_input == "log":
                Flashcards.log(self)
            elif user_input == "hardest card":
                Flashcards.hardest_card(self)
            elif user_input == "reset stats":
                Flashcards.reset_stats(self)

    def log(self):
        print("File name:")
        self.mem_file.write("File name:" + "\n")
        file_name = input()
        self.mem_file.write(file_name + "\n")
        with open(file_name, "w") as log:
            for line in self.mem_file.getvalue():
                log.write(line)
        print("The log has been saved.")
        self.mem_file.write("The log has been saved." + "\n")

    def hardest_card(self):  
        most_errs = 0
        most_errs_counter = 0
        for value in self.mistakes.values():
            if value > most_errs:
                most_errs = value
        if most_errs == 0:
            print("There are no cards with errors.")
            self.mem_file.write("There are no cards with errors." + "\n")
        else:
            for value in self.mistakes.values():
                if value == most_errs:
                    most_errs_counter += 1
            if most_errs_counter == 1:
                for key in self.mistakes.keys():
                    if self.mistakes[key] == most_errs:
                        print('The hardest card is "{term}". You have {N} errors answering it'.format(N=most_errs,
                                                                                                      term=key))
                        self.mem_file.write(
                            'The hardest card is "{term}". You have {N} errors answering it'.format(N=most_errs,
                                                                                                    term=key) + "\n")
            else:
                several_values = 'The hardest cards are '
                test_counter = 0
                for key in self.mistakes.keys():
                    if self.mistakes[key] == most_errs:
                        test_counter += 1
                        if test_counter < most_errs_counter:
                            several_values = several_values + "key, ".format()
                        elif test_counter == most_errs_counter:
                            several_values = several_values + "key".format()
                print(several_values)
                self.mem_file.write(several_values + "\n")

    def add_card(self):
        while True:
            print("The card:")
            self.mem_file.write("The card:" + "\n")
            term = input()
            self.mem_file.write(term + "\n")
            if term in self.flashcards_storage.keys():
                print('The term "{}" already exists. Try again:'.format(term))
                self.mem_file.write('The term "{}" already exists. Try again:'.format(term) + "\n")
                continue
            else:
                break

        while True:
            print("The definition of the card:")
            self.mem_file.write("The definition of the card:" + "\n")
            definition = input()
            self.mem_file.write(definition + "\n")
            if definition in self.flashcards_storage.values():
                print('The definition "{}" already exists. Try again:'.format(definition))
                self.mem_file.write('The definition "{}" already exists. Try again:'.format(definition) + "\n")
            else:
                break
        self.flashcards_storage[term] = definition
        print('The pair ("{}":"{}") has been added.'.format(term, definition))
        self.mem_file.write('The pair ("{}":"{}") has been added.'.format(term, definition) + "\n")

    def remove_card(self):
        print("Which card?")
        self.mem_file.write("Which card?" + "\n")
        user_input = input()
        self.mem_file.write(user_input + "\n")
        try:
            del self.flashcards_storage[user_input]
            print("The card has been removed.")
            self.mem_file.write("The card has been removed." + "\n")
        except KeyError:
            print('Can\'t remove "{}": there is no such card.'.format(user_input))
            self.mem_file.write('Can\'t remove "{}": there is no such card.'.format(user_input) + "\n")

    def import_cards(self, filename=None):
        counter = 0
        self.mem_file.write("File name:" + "\n")
        if filename is not None:
            user_input = filename
        else:
            print("File name:")
            user_input = input()
        self.mem_file.write(user_input + "\n")
        if os.path.exists(user_input):
            with open(user_input, "rb") as file:
                for key, value in pickle.load(file, encoding='utf-8')[0].items():
                    self.flashcards_storage.update({key: value})
                    counter += 1
            print("{} cards have been loaded.".format(counter))
            self.mem_file.write("{} cards have been loaded.".format(self.flashcards_storage) + "\n")
            with open(user_input, "rb") as file:
                for key, value in pickle.load(file)[1].items():
                    self.mistakes.update({key: value})
        else:
            print("File not found.")
            self.mem_file.write("File not found.".format(counter) + "\n")

    def export_cards(self, filename=None):
        self.mem_file.write("File name:" + "\n")
        if filename is not None:
            user_input = filename
        else:
            print("File name:")
            user_input = input()
        self.mem_file.write(user_input + "\n")
        with open(user_input, "wb") as file:
            pickle.dump([self.flashcards_storage, self.mistakes], file)
        print("{} cards have been saved.".format(len(self.flashcards_storage)))
        self.mem_file.write("{} cards have been saved.".format(len(self.flashcards_storage)) + "\n")

    def ask_number(self):
        print("How many times to ask?")
        self.mem_file.write("How many times to ask?" + "\n")
        user_input = int(input())
        self.mem_file.write(str(user_input) + "\n")
        for number in range(user_input):
            random_card = random.choice([k for k in self.flashcards_storage.keys()])
            print('Print the definition of "{}":'.format(random_card))
            self.mem_file.write('Print the definition of "{}":'.format(random_card) + "\n")
            self.mistakes.setdefault(random_card, 0)
            while True:
                answer = input()
                if answer == self.flashcards_storage[random_card]:
                    print("Correct!")
                    self.mem_file.write("Correct!" + "\n")
                    break
                elif answer != self.flashcards_storage[random_card] and answer in self.flashcards_storage.values():
                    print('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                        self.flashcards_storage[random_card],
                        list(
                            self.flashcards_storage.keys())[
                            list(
                                self.flashcards_storage.values()).index(
                                answer)]))
                    self.mem_file.write(
                        'Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                            self.flashcards_storage[random_card],
                            list(
                                self.flashcards_storage.keys())[
                                list(
                                    self.flashcards_storage.values()).index(
                                    answer)]) + "\n")
                    self.mistakes.update({random_card: self.mistakes[random_card] + 1})
                    break
                else:
                    print('Wrong. The right answer is "{}".'.format(self.flashcards_storage[random_card]))
                    self.mem_file.write(
                        'Wrong. The right answer is "{}".'.format(self.flashcards_storage[random_card]) + "\n")
                    self.mistakes.update({random_card: self.mistakes[random_card] + 1})
                    break

    def reset_stats(self):
        self.mistakes = {}
        print("Card statistics have been reset.")
        self.mem_file.write("Card statistics have been reset." + "\n")

    def exit(self):
        print("Bye bye!")
        self.mem_file.write("Bye bye!" + "\n")
        print("{} cards have been saved.".format(len(self.flashcards_storage)))
        self.mem_file.write("{} cards have been saved.".format(len(self.flashcards_storage)) + "\n")
        if self.args_filename is not None:
            Flashcards.export_cards(self, filename=self.args_filename)
        exit()


def main():
    flashcards = Flashcards()
    parser = argparse.ArgumentParser()
    parser.add_argument("--import_from")
    parser.add_argument("--export_to")
    args = parser.parse_args()
    if args.import_from is not None:
        flashcards.import_cards(args.import_from)
        flashcards.run()
    elif args.export_to is not None:
        flashcards.args_filename = args.export_to
        flashcards.run()
    else:
        flashcards.run()


if __name__ == "__main__":
    main()