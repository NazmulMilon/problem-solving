num = int(input("Enter an integer number:"))
sum=0
for i in range(num+1):
    for j in range(1,i+1):
        sum= sum+1
        print(sum,'\t', end="")
    print("\r")
