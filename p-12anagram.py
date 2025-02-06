s = input("give me the anagram p-1 :")
s1 = input("give me the anagram p-2 :")
a = sorted(s.lower())
b = sorted(s1.lower())

if a == b :
    print("true")
else:
    print("false")    

# anagram is a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
