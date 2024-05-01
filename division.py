x=int(input("Enter x:"))
y=int(input("Enter y:"))
if(y!=0):
     if((type(x)==int and type(y)==int) or (type(x)==float and type(y)==float) or(type(x)==float and type(y)==int) or (type(x)==int and    type(y)==float)):
         print(x/y)
else:
    print("division not possible")
