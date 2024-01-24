import random
import sys
import csv
import os


script_dir = os.path.dirname(__file__)  # Get the directory of the current script
csv_path = os.path.join(script_dir, 'valid-words.csv')  # Join the script directory with the CSV file name


wordle_len = 5
wordle_tries = 6
selected_word = []


def read_csv(path):
    data = []
    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row[0].upper())  # Extract words and convert to uppercase
    return data


valid_word_data = read_csv(csv_path)

all_words = valid_word_data


def word_select():
    global selected_word
    selected_word = list(random.choice(valid_word_data).upper())
    return selected_word


def on_lose():
    global wordle_tries
    correct_word = ''.join(selected_word)
    print("Good Try, The correct word was " + correct_word + ".\nCare to Try Again?\ny/n")
    response = input().lower()
    if response == 'y' or response == 'yes':
        wordle_tries = 6
        main()
    elif response == 'n' or response == 'no':
        sys.exit()
    else:
        print("Incorrect Input, Try Again!")
        on_lose()


def wordle_visualizer(selected_word, guessed_word, wordle_tries):
    visualization = []

    for i, letter in enumerate(selected_word):
        if i < len(guessed_word):
            if guessed_word[i] == letter:
                visualization.append(letter.upper())
            elif guessed_word[i] in selected_word:
                visualization.append(guessed_word[i].lower())
            else:
                visualization.append('_')
        else:
            visualization.append('_')

    print(' '.join(visualization))
    print(f"Remaining Tries: {wordle_tries - 1}")



def remaining_letters():

    keyboardAlpha = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    for i in range (len(keyboardAlpha)):
        sorted_word = selected_word.sort()

    return 1

## FIX DOUBLE LETTERS



def main():
    global wordle_tries
    selected_word = word_select()
    


    while (wordle_tries != 0):
        guessed_word = input("Enter a Word: ").upper()


        if guessed_word in all_words:
            wordle_visualizer(selected_word, guessed_word, wordle_tries)


            if guessed_word == ''.join(selected_word):
                print("Congratulations, Your Guess Was Correct! The Word Was " + ''.join(selected_word))
                break
            else:
                wordle_tries -= 1
        else:
            print("Invalid Word Choice, Please Try Again.")

    if (wordle_tries == 0):
        on_lose()
            



if __name__ == '__main__':
    main()

