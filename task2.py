def given_length (string, length):
    split_words = string.split()
    i = 0
    newL = []
    for i in range (len(split_words)-1):
        if (len(split_words[i]) == length):
            newL.append(split_words[i])
    print(newL)

def longest_word (string):
    longest = 0
    i = 0
    split_words = string.split()
    for i in range (len (split_words)):
        if len(split_words[i]) >= len((split_words[longest])):
            longest = i
    print(split_words[longest])

def most_common(string):
    a = []

    
    for char in string:
        a.append(ord(char))
    print(a)

   
    
    
given_length("The white cat and the red fox.", 3)
longest_word("Hello CS2613! Python is fun.")
most_common("asdfsadfasdaaa")
most_common("This is")