# read file name and open it
name = input('Enter file name to find most common word: ')
handle = open(name)

# count the word frequency
dictionary = dict()
for line in handle:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word,0) + 1

# find the most common word and its count
bigcount = None
bigword = None
for word,count in dictionary.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)