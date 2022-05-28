# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    f = open('story.txt','r')
    file = f.read()
    f.close()
    return file
print(read_file_content('story.txt'))


def count_words():
    text = read_file_content('story.txt')

    for word in text:
        split_text = word.split(" ")
    count_words = {}
    for word in split_text:
        if word in count_words:
            count_words[word] +=1
        else:
            count_words[word] =1
            
    return count_words
print(count_words())
