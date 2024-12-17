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

def main():
    book_path = "books/frankenstein.txt"
    read_text = get_book_text(book_path) # pass the parameter of book_path
    num_words = get_num_words(read_text)
    chars_dict = get_char_number(read_text)
    print(chars_dict)
    # print(f"{num_words} words found in the document")

main()
