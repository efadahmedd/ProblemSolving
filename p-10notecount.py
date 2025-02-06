num = 6666
note = [500,200,100,50,20,10,5,2,1]


for i in note:
    notecount = num // i
    if notecount > 0 :
        print(i,notecount)
    newvalue = num % i
    num = newvalue
