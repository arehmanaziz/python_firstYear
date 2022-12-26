a=[1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
b=a.copy()
print (a)
np=4

def hm_msg(a,np):
    for i in range (np):
        a.insert((2**i)-1,-1)
    return(a)

def check(a,np):
    l=len(a)
    chk=[]
    for i in range (np):
        chk1=[]
        # if i==0:
        #     for j in range (2**(np-1)):
        #         jj=2*j
        #         chk1.append(a[jj])
        #    # chk.append(chk1)
        # #else:
        #
        j=(2**i)-1
        k=j+2**i
        while j<l and k<l:
            for v in range(j,k):
                chk1.append(a[v])
            j=k+2**i
            k=j+2**i
        chk.append(chk1)
    return(chk)

def odd_scheme(ab):
    ham_bt=[]
    for i in range (len(ab)):
        sum_abi=(sum (ab[i]))+1
        if sum_abi % 2 ==0:
            ham_bt.append(1)
        else:
            ham_bt.append(0)
    return ham_bt

def forward_msg(a,hb):
    for i in range (len(hb)):
        p=(2**i)-1
        a.insert(p,hb[i])
    return(a)
ab=hm_msg(a,np)
checker=check(ab,np)
hm_bits=odd_scheme(checker)
final_msg=forward_msg(b,hm_bits)
print (checker)
print(hm_bits)
print("****")
print(final_msg)