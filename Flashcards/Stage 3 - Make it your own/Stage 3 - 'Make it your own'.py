print("Input the number of cards:")
flashcards_number = int(input())
counter = 0
flashcards_storage = {}
for card in range(flashcards_number):
    counter += 1
    print("The term for card #{}:".format(counter))
    term = input()
    print("The definition for card #{}:".format(counter))
    definition = input()
    flashcards_storage[term] = definition
for key, value in flashcards_storage.items():
    print('Print the definition of "{}":'.format(key))
    answer = input()
    if answer == value:
        print("Correct!")
    else:
        print('Wrong. The right answer is "{}".'.format(value))