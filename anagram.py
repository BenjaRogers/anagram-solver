"""get user input for a word or phrase to find anagrams for"""
def get_phrase():
    phrase = input("Enter a phrase to see if there are anagrams: ")
    return phrase

"""sort strings into alphabetical order and make all characters uppercase
    if strings match -- they are anagrams"""
def anagrams(string1, string2):
    string1 = sorted(string1.upper())
    string2 = sorted(string2.upper())
    return string1 == string2

"""create empty list to place anagrams into
    open text file to check user phrase against
    checks every word in text file to see if it matches
    appends word to anagram list"""
def find_the_anagrams(string):
    anagrams_list = []
    with open('Lexicon.txt', 'r') as wordlist:
        for line in wordlist:
            word = line.strip()
            if anagrams(string, word):
                anagrams_list.append(word)
    print(anagrams_list)

def main():
    while True:
        string = get_phrase()
        find_the_anagrams(string)

if __name__ == "__main__":
    main()




