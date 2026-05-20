password=input()
d=len(password)
ncaps=0
nsmall=0
nspc=0
nnums=0
alphas=0
for i in password:
    m=ord(i)
    if m>=65 and m<=90:
        ncaps+=1
    elif m>=97 and m<=122:
        nsmall+=1
    elif i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="<" or i==">" or i=="/" or i==".":
        nspc+=1
    elif m>=48 and m<=57:
        nnums+=1
alphas=ncaps+nsmall 
    
marks=0



if ncaps>=1:
    marks+=1
if nsmall>1:
    marks+=1
if alphas>4:
    marks+=1
if alphas>0 and alphas<4:
    marks+=0.5
if d>=8 and d<12:
    marks+=0.5
if d>12:
    marks+=1
if nspc>=2:
    marks+=1
if nspc<2 and nspc>=1:
    marks+=0.5
    
if nspc>1 and ncaps>=1 and nsmall>1 and nnums>1:
    marks+=1
print(marks)
if marks>5:
    print("Great you created a strong password.....")
elif marks>=4 and marks<=5:
    print("That is a good password but, you could make it more complex.....")
    print("Make sure you follow all the steps to generate a stronger password")
    print("1. Length of the password should be more than 12 characters")
    print("2. It should consist both capital and small letters")
    print("3. Make sure you add atleast you add 2 special characters in the password")
    print("4. Make sure you atleast gave more than 4 alphabets")
    print("5. Make you use all of them alphabets(both capital and small), numbers, special characters.")
elif marks<4:
    print("That password is not strong enough should i help you to generate a strong password....")
    print("If yes ")