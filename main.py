def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)

    print(f"{num_words} words found in the document")
    
    for letter in num_letters.keys():
        print(f"The '{letter}' was found {num_letters[letter]} times")
        


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text: str):
    letters = {}

    for letter in text.lower():
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters


main()
