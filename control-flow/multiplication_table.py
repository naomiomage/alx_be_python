#Ask user for value
number = int(input("Enter a number to see its multiplication table: "))
  
n = 0

#Multiplication

for i in range(1, 11):
    n+= 1
    value = number * n
    print(f"{number} * {n} =  {value}")