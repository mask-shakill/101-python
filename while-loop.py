# basic while loop 
num1 = 1
while (num1<=10):
    print(num1)
    num1 +=1

# print 1 to 10 all odd numbers
num3 = 1
while num3<=10:
    print(f"Odd Numbers : {num3}")
    num3 += 2

# print 0 to 10 all even numbers
num2 = 0
while num2<=10:
    print(f"Even numbers : {num2}")
    num2 = num2 + 2

# break 

num4=1
while num4<=10:
    print(f"{num4}")
    num4 += 1 
    if num4 == 4:
        break

# continue 

num5 = 1
while num5 <= 10:
    
    if num5 == 5:
        num5 +=1
        continue
    print(num5)
    num5 += 1


    
    