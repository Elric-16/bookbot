def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    
    count = count_words(text)
    
    count_char = charac(text)
    
    sorted_list = fullrep(count_char)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was fond {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]



def fullrep(count_char):
    sorted_list = []
    for char in count_char:
        sorted_list.append({"char": char, "num": count_char[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    



def charac(text):
    lowered_string = text.lower()
    charlist = list(lowered_string)
    chardict = {}
    for char in charlist:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict



def get_text(book_path):
    with open(book_path) as f:
        return f.read()
    


def count_words(text):
    words = text.split()
    num_words = len(words)

    return num_words




main()



   