class Flashcards:
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.flashcards_storage = {}

    def add_cards(self):
        counter = 0
        for card in range(self.number_of_cards):
            counter += 1
            print("The term for card #{}:".format(counter))
            while True:
                term = input()
                if term in self.flashcards_storage.keys():
                    print('The term "{}" already exists. Try again:'.format(term))
                    continue
                else:
                    break
            print("The definition for card #{}:".format(counter))
            while True:
                definition = input()
                if definition in self.flashcards_storage.values():
                    print('The definition "{}" already exists. Try again:'.format(definition))
                else:
                    break
            self.flashcards_storage[term] = definition

    def guess(self):
        for key, value in self.flashcards_storage.items():
            print('Print the definition of "{}":'.format(key))
            while True:
                answer = input()
                if answer == value:
                    print("Correct!")
                    break
                elif answer != value and answer in self.flashcards_storage.values():
                    print('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(value,
                                                                                                             list(
                                                                                                                 self.flashcards_storage.keys())[
                                                                                                                 list(
                                                                                                                     self.flashcards_storage.values()).index(
                                                                                                                     answer)]))
                    break
                else:
                    print('Wrong. The right answer is "{}".'.format(value))
                    break


def main():
    print("Input the number of cards:")
    flashcards_number = int(input())
    flashcards = Flashcards(flashcards_number)
    flashcards.add_cards()
    flashcards.guess()


if __name__ == "__main__":
    main()