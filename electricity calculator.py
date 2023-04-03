a=int(input("cunsumed units:"))
if(a>0 and a<100):
    print("your bill =",a*1.5)
elif(a>=100 and a<200):
    print("your bill =",a*2.5)
elif(a>=200 and a<300):
    print(a*4)
elif(a>=300 and a<350):
    print("your bill =",a*5)
elif(a>=350):
    print("your bill =",a*5+1500)