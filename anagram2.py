import tkinter as tk

HEIGHT = 50
WIDTH = 100
root = tk.Tk()
"""get user input for a word or phrase to find anagrams for"""
def get_phrase():
    phrase = entry.get()
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
    return(anagrams_list)
"""return anagrams based on entry from tkinter window"""
def main():
    return (find_the_anagrams(get_phrase()))

"""change label to show solutions from anagram algorithm 
based on return from main function"""
def create_label():
    result.config(text=main())

"""create all widgets and labels for tkinter window"""
label = tk.Label(root, text="Enter the word you would like to find anagrams for: ")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
result = tk.Label(root, text="")
entry = tk.Entry(root)
button = tk.Button(root, text="Submit", bg='gray', command=create_label)
label2 = tk.Label(root, text="Here are your possible solutions!")

"""Pack it all up"""
label.pack()
entry.pack()
button.pack()
canvas.pack()
label2.pack()
result.pack()

root.mainloop()