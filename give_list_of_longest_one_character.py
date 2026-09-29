lis = input("Enter a list with some strings (space separated) : ")
words_list = lis.split()
word_len = []
for n in words_list:
    word_len.append((len(n),n))
    print(word_len)
    word_len.sort()
    print(word_len)
print("Longest word : ",word_len[-1][1])