v = "aeiou" 
s = "aeiou" 
count = 0 

for i in v:
    if i in s :
        count+=1        
res = "True" if  count == 5 else "False"

print(res)

