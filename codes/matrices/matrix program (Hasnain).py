##i=0
##k=0
##while (k<=2):
##    i=0
##    while(i<=4):
##        print("-",end=" ")
##        i=i+1
##    k=k+1
##    print(" ")
##nR=float(input("no. of rows:"))
##nC=float(input("no. of columns:"))
##m1=[]
##R=0
##r1=[]
##while (R<nR):
##    a=float(input("row:"))
##    r1.append (a)
##    R=R+1
##C=0
##r2=[]
##while (C<nC):
##    a=float(input("row2:"))
##    r2.append (a)
##    C=C+1
##m1.append (r1)
##m1.append (r2)
##print(m1)
nR2=float(input("no. of rows:"))
nC2=float(input("no. of columns:"))
m2=[]
R=0
r1=[]
while (R<nR2):
    a=float(input("row:"))
    r1.append (a)
    R=R+1
    C=0
    r2=[]
    while (C<nC2):
        a=float(input("row2:"))
        r2.append (a)
        C=C+1
m2.append (r1)
m2.append (r2)
print(m2)

