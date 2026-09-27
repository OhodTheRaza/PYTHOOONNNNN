def matchwords(words):
    ctr = 0
    lst = []
    for word in words:
        if  len(word) > 1 and word[0] == word[-1]:
          ctr += 1
          lst.append(words)
    print("List of words with first and last letters are the same\n", lst)
    return ctr
count = matchwords(['abc', 'cdc', 'brok', '112141', 'refer', 'dad'])
print("Numbers of words having the last and first letter same :", count)