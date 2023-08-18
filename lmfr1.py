x=lambda x:x+5
print("x+x=",x(1))

b=lambda a,b:a+b
print(b(2,3))

y=(lambda x,y:x if (x>y) else y)
print("greater number is",y(4,8))

c=lambda a:a*a
print("squre of the number is",c(3))

#map
m=(10,5,9,24,31,20)
l=list(map(lambda x:x+5,m))
print("to add 5 number to m",l)

#filter
lst=[10,1,2,3,5]
z=list(filter(lambda x:x%2,lst))
print(z)

#reduce
from functools import reduce
lst1=[10,5,9,6,47,7,54]
a=reduce(lambda x,y:x-y,lst1)
print(a)


