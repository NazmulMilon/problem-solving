num = int(input("Enter a number:"))
sum = 0

for i in range(num+1):
    for j in range(1, i+1):
        print(j, end="")
        sum=sum+1
    print("\r")