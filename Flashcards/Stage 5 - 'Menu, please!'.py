import os
import pickle
import random


class Flashcards:
    def __init__(self):
        self.flashcards_storage = {}

    def run(self):
        while True:
            print("Input the action (add, remove, import, export, ask, exit):")
            user_input = input()
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
                Flashcards.exit()

    def add_card(self):
        while True:
            print("The card:")
            term = input()
            if term in self.flashcards_storage.keys():
                print('The term "{}" already exists. Try again:'.format(term))
                continue
            else:
                break

        while True:
            print("The definition of the card:")
            definition = input()
            if definition in self.flashcards_storage.values():
                print('The definition "{}" already exists. Try again:'.format(definition))
            else:
                break
        self.flashcards_storage[term] = definition
        print('The pair ("{}":"{}") has been added.'.format(term, definition))

    def remove_card(self):
        print("Which card?")
        user_input = input()
        try:
            del self.flashcards_storage[user_input]
            print("The card has been removed.")
        except KeyError:
            print('Can\'t remove "{}": there is no such card.'.format(user_input))

    def import_cards(self):  
        counter = 0
        print("File name:")
        user_input = input()
        if os.path.exists(user_input):
            with open(user_input, "rb") as file:
                for key, value in pickle.load(file).items():
                    self.flashcards_storage.update({key: value})
                    counter += 1
            print("{} cards have been loaded.".format(counter))
        else:
            print("File not found.")

    def export_cards(self): 
        print("File name:")
        user_input = input()
        with open(user_input, "wb") as file:
            pickle.dump(self.flashcards_storage, file)
        print("{} cards have been saved.".format(len(self.flashcards_storage)))

    def ask_number(self):
        print("How many times to ask?")
        user_input = int(input())
        for number in range(user_input):
            random_card = random.choice([k for k in self.flashcards_storage.keys()])
            print('Print the definition of "{}":'.format(random_card))
            while True:
                answer = input()
                if answer == self.flashcards_storage[random_card]:
                    print("Correct!")
                    break
                elif answer != self.flashcards_storage[random_card] and answer in self.flashcards_storage.values():
                    print('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                        self.flashcards_storage[random_card],
                        list(
                            self.flashcards_storage.keys())[
                            list(
                                self.flashcards_storage.values()).index(
                                answer)]))
                    break
                else:
                    print('Wrong. The right answer is "{}".'.format(self.flashcards_storage[random_card]))
                    break

    @staticmethod
    def exit():
        print("Bye bye!")
        exit()


def main():
    flashcards = Flashcards()
    flashcards.run()


if __name__ == "__main__":
    main()