e=0.01
x=0.5

n=1
t=x
p=0
while abs(t)>e:
   
    p=p+t
    n=n+1
    t=((-1)**(n+1))*(x**n)/n
  
print(p)
