author = "serkan korkusuz"

def myfunc(x):
    mylist=[]
    base=0
    for i in x:
        if i !="0" and i !="." and i !=",":
            mylist.append(i)
            break
    for j in range(len(x)):
        if mylist[0]==x[j]:
            mylist=x[j:]
            break
    k=0
    for i in x:
        k+=1
        if i=="." or i==",":
            base=-1*(len(x)-k)
    mynum=1
    if int(mylist)>=10:
        mynum=int(mylist)/(10**(len(mylist)-1))
        base+=len(mylist)-1
    else:
        mynum=mylist
    print(str(mynum)+"x10^"+str(base))
    print("Enter 'q' to quit or")
def loop():
    myinput=input("Enter your input: \n")
    myfunc(myinput)
    if myinput !="q":
        loop()
    elif str(myinput)=="q":
        print("Bye bye!")
loop()
