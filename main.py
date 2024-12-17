def get_book_text(path):
    with open(path, 'r') as f: # added r, but it is an optional parameter. Being explicit here.
        return f.read() #read the file

def get_num_words(read_text):
    words = read_text.split() # splitting each character into individual elements to find count of each word
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    read_text = get_book_text(book_path) # pass the parameter of book_path
    num_words = get_num_words(read_text)
    print(f"{num_words} words found in the document")

main()
