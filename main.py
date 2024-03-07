def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    alphabet = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for letter in text:
        if letter.lower() in alphabet:
            alphabet[letter.lower()] += 1
    return alphabet

def main():
    with open('./books/frankenstein.txt', 'r') as file:
        text = file.read()
        word_count = count_words(text)
        print('--- Begin report of books/frankenstein.txt ---\n')
        print('The book has {} words \n'.format(word_count))
        letter_count = count_letters(text)
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        for letter in sorted_letter_count:
            print('The letter "{}" appears {} times'.format(letter[0], letter[1]))
        print('\n--- End report ---')

if __name__ == '__main__':
    main()
