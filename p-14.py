d = int(input("duration in days :"))
y = d//365 
restdays = d%365
m = restdays//30
restdays = restdays%30

print(f"{y} ano(s)")
print(f"{m} mes(es)")
print(f"{restdays} dia(s)")
