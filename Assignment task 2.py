a=int(input("no. of terms:"))
x=0
y=1
if a<=0:
    print(x)
else:
    print(x,y,end=' ')
    for i in range(2,a):
        z=x+y
        print(z,end=' ')
        x=y
        y=z

