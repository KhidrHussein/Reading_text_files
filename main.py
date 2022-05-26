# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from asyncore import read
from importlib.resources import contents


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as t:
        contents = t.read()    
    return contents


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    contents_list = text.split(' ')
    word_dict = {}
    for word in contents_list:
        word_dict[word] = contents_list.count(word)
    return word_dict


print(count_words())


