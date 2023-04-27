"""
day01
"""
a = 0
if a==0:
    print("a=0")
elif a==1:
    print("a=1")

else :
    print("first the value of a is other")


"""
根据x的值，求y
已知 x>1,y=3x-5
-1<=x<=1, y=x+2
x<=-1 , y = 5x+3

"""
x = 0
if x > 1:
    y = 3*x-5
else:
    if x>=-1:
        y = x + 2
    else:
        y = 5*x +3
print("y = ",y)

"""
在python中，更倾向于下面这种扁平化的结构，避免多层嵌套

"""

if x > 1:
    y = 3*x-5
elif -1<=x<=1:
        y = x + 2
else:
    y = 5*x +3
print("y = ",y)


"""
实现1--100 之间的偶数求和
"""
result1 = 0
for i in range(101):
    if i % 2 ==0:
        result1 = result1 + i
        print (i)
print(result1)

result2 = 0
for i in range(2,101,2):
    result2 = result2 + i
    print (i)
print(result2)



"""
while/else
continue
break
"""

for i in range(1,15):
    if i == 5:
        continue
    elif i ==9:
        break
    print(i)


