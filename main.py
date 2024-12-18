"""
With statement implements context managers which are used to manage
resources, files, connections, locks,etc. Basically they invoke __enter__()
and __exit__()

Consider a block of code at the start (entry) and end of block (exit).
This ensures that it is released/closed when finished.

__enter__() - defines what happens when context is entered
__exit__() defines when is exited, cleanup, exceptions ,etc.

In the background, python loads both __enter__() and __exit__() when the content
expression is evaluated to obtain the context manager to be be invoked later.

"""
def main():
    book_path = "books/frankenstein.txt"
    read_text = get_book_text(book_path) # pass the parameter of book_path
    num_words = get_num_words(read_text)
    chars_dict = get_char_number(read_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


    print("--- End Report ---")
    # print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path, 'r') as f: # added r, but it is an optional parameter. Being explicit here.
        return f.read() #read the file

def get_num_words(read_text):
    words = read_text.split() # splitting each character into individual elements to find count of each word
    return len(words)

def get_char_number(read_text):
    chars = {} # defining new dicitionary
    for char in read_text: # iterating through each character in text (including white space)
        lowered = char.lower() # make everything case-sensitive
        if lowered in chars: # check to see if a key-value pair exist in dicitionary
            chars[lowered] += 1 # add to the key-value pair if present
        else:
            chars[lowered] = 1 # if not, first appearance is added
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
