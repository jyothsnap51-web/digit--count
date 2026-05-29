number = int(input("Enter a whole number: ")) 
c = 0

if number == 0: 
    c = 1
else:
    while number > 0:
        c = c + 1
        number = number // 10 

print("The number of digits is:",c)