import math
global mul
##numbers=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
desirednumberlength=0
lengthofalphabets =len(alphabets)
numbers=[]
while(desirednumberlength<lengthofalphabets):
     givennumbers=str(input(f"Enter desired number in accordance with {alphabets[desirednumberlength]}"))
     numbers.append(givennumbers)
     desirednumberlength+=1
originalpassword="password is abcyzx"
sepration=list(originalpassword)
print(sepration)
lengthofpassword=len(sepration)

i=0
numbersforonedigit=[]
Mi=[]
Ci=[]

while(i<lengthofpassword):
    Indexofpassword=sepration[i]
    j=0
    while(j<lengthofalphabets):
        indexofalphabets=alphabets[j]
        if (Indexofpassword==indexofalphabets):
            numbersforonedigit.append(numbers[j])
            j=0
            break
        j+=1
    i+=1
print(numbersforonedigit)
seperationquantity=int(input("In how Many Words Do You want to break alphabets"))
index1=(lengthofpassword/seperationquantity)
index=math.floor(index1)
sub=index1-index
mul1=sub*index
mul=lengthofpassword-mul1
print(mul)
rr=numbersforonedigit[-1]
k=0
m99=[]
while(k<index):
    h=0
    while(h<seperationquantity):  
     m2=numbersforonedigit[h]
     m99.append(m2)
     if(h==seperationquantity-1):
        m995=''.join(m99)
        Mi.append(int(m995))
        m99=[]
        del numbersforonedigit[0:h+1]
      
        
     h+=1    
    k+=1
if(lengthofpassword%seperationquantity!=0):
         r=0
         while(r<mul1):
           m2=numbersforonedigit[int(r)]

           Mi.append(int(m2))
           r+=1
print(numbersforonedigit)
l=0
LengthofMi=len(Mi)
while(l<LengthofMi):
      q=((Mi[l])**17)%2773
      Ci.append(q)
      l+=1
r=0
while(r<len(Ci)):
      Ci[r]=str(Ci[r])
      Ci[r]=Ci[r].zfill(seperationquantity*2)
      Mi[r]=str(Mi[r])
      Mi[r]=Mi[r].zfill(seperationquantity*2)
      r+=1

print(Mi)
print(Ci)
ans=''.join (Ci)
print(ans)
      
    
