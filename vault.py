print("---Password store---")
passwordlist=[]
print("Enter 1 if you want to add a new password to the existing passwords or 2 if you want to view the existing passwords or 3 if you want to know a password for a particular website.")

choice=int(input())
if choice==1:
    name=input()
    pas=input()
    passwordlist.append([name]+[pas])
    print(passwordlist)
        
elif choice==2:
    for i in passwordlist:
        print("Name of the browser:"+i[0])
        print("Password of the website is:"+i[1])
elif choice==3:
    name=input()
    for i in passwordlist:
        if name == i[0]:
            print("Password for the inputted website is:"+i[1])