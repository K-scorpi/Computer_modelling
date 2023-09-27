#task 1
a=[54,345,123,567,98,2345678]
def listends(a):
    print(a[0],a[len(a)-1])
    return listends
print (listends(a))
#task 1.2 and 1.1
import time
m=input("Vvedi message:") #message
d=int(input("cherez skolko vyvesti message?:")) #time delay
def message(m):
    t=time.time()
    nt=time.ctime(t)
    time.sleep(d)
    print(m,nt)
    return message
print(message(m))