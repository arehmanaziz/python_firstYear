a = [[50,3], [75,8],[10,6],[65,1],[35,5],[45,0],[15,9],[95,-1],[85,7],[20,4]]
min=a[0][0]
n=1
while n<len(a):
 if min>a[n][0]:
  min_i=n
  min=a[n][0]
 n+=1
print(min)
min_n=a[min_i][1]

#i = min_n
#while (i>=0):
 #val = a[i][0]
 #i = a[i][1]
 #print (val)

for i in range (0,len(a)-1):
 nf=a[min_n][0]
 min_n=a[min_n][1]
 print(nf)
 
