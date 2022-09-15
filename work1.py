import sys
ls=list()

num = input("Please Enter once number: ")
max=min=num
ls.append(num)
while (1):
    num = input("Please Enter once number: ")

    if num=='done':
        break
    if not num.isdigit():
        print("Invalid input")
        sys.exit(0)

    ls.append(num)

    if int(num)>int(max):
        max=num
    if int(num)<int(min):
        min=num
sum=0
i=1
for i in range(len(ls)):
    sum =sum+int(ls[i])
print("The array sum is",sum)
average=sum/len(ls)
print("The array average is",average)
print("count is",len(ls))
print("max is",max)
print("min is ",min)