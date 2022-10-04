'''''
a=int(input("Число: "))
res=1
for x in range(1,a+1):
    res*=x
print("Факториал: ",res)
'''
'''''
def f(x,r=1):
    for i in range(1,x+1):
        r*=i
    return(r)
print(f(10))
'''
f=open('okl.txt','w+')
for x in range(1,101):
    if x%5==0 and x%3==0:
        f.write("Hello Wold\n")
    elif x%3==0:
        f.write("Hello\n")
    elif x%5==0:
        f.write("Wold\n")
    else:
        f.write(str(x)+'\n')
f.close()