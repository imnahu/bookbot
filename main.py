def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    def count_words(text):
        words = text.split()
        return len(words)
    
    def count_letters(text):
        letters = {}
        for char in text:
            lower_char = char.lower()
            if lower_char in letters:
                letters[lower_char] += 1
            else:
                letters[lower_char] = 1
        return letters
    
    print(f"There are {count_words(file_contents)} words in this text")
    print(f"Here are the characters and the amount of times they appear in the text {count_letters(file_contents)}")

main()