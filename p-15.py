n = int(input("duration in seconds :"))
m = n//60
h = m//60
m = m%60
n = n%60
print(f"{h}:{m}:{n}")