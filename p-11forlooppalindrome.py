s = input("give me the word :")
length = len(s)
count = 0

for i in range(0,length//2) :
    if s[i] != s[length -1 -i]:
        print("False")
        break
    else:
        print("True")
        break



# a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run
























# s2 = s[::-1]
# print(s2)
