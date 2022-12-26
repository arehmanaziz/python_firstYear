
def mid_point():
   
    mid=int((start+end)/2)         
    mid_p=a[mid]
    return (mid_p,mid)



array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
a=sorted(array)
i=0
start=i                        # STARTING INDEX
end=len(a)-1                   # END  INDEX
s = int(input("enter key: "))  # DESIRED NUMBER
h,m=mid_point()

while start < end :

    
    if h > s:
        end = m - 1
        mid_point()
        h,m=mid_point()

    if h < s:
        start = m + 1
        mid_point()
        h,m=mid_point()
       

    if h == s:
        print(s,"number found at",m+1)
        break
else:

    print(" Not Found ")
