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
    
    def dict_to_list(dict):
        list_dict = []
        for elemn in dict:
            if elemn.isalpha():
                new_dict = {"char" : elemn, "amnt" : dict[elemn]}
                list_dict.append(new_dict)
        return list_dict
    
    def sort_desc(list):
        return sorted(list, key=lambda x: x['amnt'], reverse=True)
    
    def report():
        chardic = count_letters(file_contents)
        charlist = dict_to_list(chardic)
        sorted_charlist = sort_desc(charlist)
        print("---- BEGIN OF FRANKSTEIN REPORT ----")
        print(f"{count_words(file_contents)} words found in the text.\n")
        for char in sorted_charlist:
            print(f"character '{char['char']}' was found {char['amnt']} times")
        print("---- END OF REPORT ----")

    report()

main()