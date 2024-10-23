def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        # print(text)
    count_words(text)

    print()

    frequencies = count_char(text)
    for char, count in sorted(frequencies.items()):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

def count_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")
    return len(words)

def count_char(text):
    char_count ={}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
main()