def prvocisla(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
    
lower = int(input("napiš nejnišší: "))
upper = int(input("napiš nejvyšší: "))

print("Prvo číšla mezi", lower, "a", upper, "jsou:")

for i in range(lower, upper + 1):
  
   prvocisla(i)