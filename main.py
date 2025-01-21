def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        dict = {}
        count = len(file_contents.split())
        for letters in file_contents:
            if letters.isalpha():
                if letters in dict:
                    dict[letters] += 1
                else:
                    dict[letters] = 1
        print("--- Begin report of books/frankenstein.txt ---")
        print(count, "words found in the document")
        print()

        for characters in dict:
            print(f"The '{characters}' character was found {dict[characters]} times")

        print()
        print("--- End report ---")
        
main()
