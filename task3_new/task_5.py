a=int(input("Введите a"))
b=int(input("Введите b"))
c=int(input("Введите c"))
x=int(input("Введите x"))
y=int(input("Введите y"))
if (x>=a and y>=b) or (x>=c and y>=b):
    print("кирпич прошел")
else:
    print ("не прошел")