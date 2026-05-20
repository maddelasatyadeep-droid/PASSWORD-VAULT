import random
word=[]
w=0
num=[]
n=0
sc=[]
nsc=0
print("If you want to suggest the elements which are to be used press 1 or You can press 2 to randomly generate a password")
choice=int(input())
if choice==1:
    print("Note follow the given instructions to generate a strong and reliable password")
    print("---Enter two words which you would like to be in your password---")
    print("Ensure that you give the words with both capital and small letters")
    while w<2:
        x=input().strip()
        word.append(x)
        w+=1
    print("---Enter four numbers which you would like to be in your password---")
    while n<4:
        y=int(input()).strip()
        num.append(y)
        n+=1
    print("---Enter special characters that you would like to be added to your password---")
    print("To see the available special characters enter '1' in the input below.")
    print("To enter the special characters enter '2' in the input below.")
    a=int(input())
    if a==1:
        print("The available special characters in the manu are as follows: !,@,#,$,%,^,&,*,(,),*,~,<,>,.")
    elif a==2:
        while nsc<2:
            z=input().strip()
            sc.append(z)
            nsc+=1
    generatedpassword=""
    allgivens=word+num+sc
    
    for i in range(len(allgivens)):
        randomobject = random.choice(allgivens)
        generatedpassword+=str(randomobject)
        ind=allgivens.index(randomobject)
        del allgivens[ind]
       
        
       
    print(generatedpassword)
    
    
else :
    list=[1,2,3,4,5,6,7,8,9,0,"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","!","@","#","$","%","^","&","*","(",")","_","-","{","}","[","]","\\","|",":",'"',";","'","<",">","."]
    print("---Enter number of characters you are wishing to be in the password---")
    ran=int(input())
    generatedpassword=""
    for i in range(ran):
        randomobject=random.choice(list)
        generatedpassword+=str(randomobject)
        ind=list.index(randomobject)
        del list[ind]
    print(generatedpassword)