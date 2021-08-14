n=int(input("Enter a integer number:"))
if(n%2==0):
    if (n>=2 and n<6):
        print("Not Weird")
    #print("Weird")
    #elif (n>=2 and n<6):
    #print("Not Weird")
    elif (n>6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")
else:
    print("Weird")
