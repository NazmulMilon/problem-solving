
num = int(input("Enter the number of elements: "))
a = list(map(int,input("Enter the numbers:\t").strip().split()))[:num]
s = sorted(list(set(a)))
# print("The output is:", s)
print("The runner-up numbers:", s[-2])



'''
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr))[-2])
'''

'''
num = int(input("Enter the number of elements: "))
a = list(map(int,input("Enter the numbers:\n").strip().split()))[:num]
s = sorted(list(set(a)))
# print("The list is: ", a)
# s = sorted(a)
# a.sort(reverse=True)
print("The output is:", s)
print("The runner-up numbers:", s[-2])


'''


'''n = int(input())
a = sorted(map(int, input().split()), reverse=True)
print(a[a.count(a[0])])
'''

























