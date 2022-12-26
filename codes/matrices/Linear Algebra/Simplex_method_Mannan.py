#_________________________FUNCTIONS______________________________
def Simplex_Method(M):
    row_multiply=lambda s,r:[r[0]]+[s*i for i in r[1:]]
    row_subtract=lambda r1,r2:[r1[0]]+[(r1[i]-r2[i]) for i in range(1,len(r1))]
    while True:
        col=min([i for i in range(1,len(M[-1])) if M[-1][i]<0],default=-1)
        if col==-1: break
        row=min([i for i in range(1,len(M)-1) if M[i][col]>0 and M[i][-1]>0],key=lambda x:M[x][-1]/M[x][col])
        for j in range(1,len(M)):
            if j==row:
                M[j]=row_multiply(1/M[row][col],M[j])
            else:
                M[j]=row_subtract(M[j],row_multiply((M[j][col]/M[row][col]),M[row]))
    return M
def Tableau_Print(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if type(M[i][j])== str:
                print('{:^10}'.format(M[i][j]),end='')
            else:
                print('{: 10.3f}'.format(M[i][j]),end='')
        print()
def Tableau_Input(uvar,ctr):
    M=[['\t']+[f'X{i+1}' for i in range(uvar)]+[f'S{i+1}' for i in range(ctr)]+['Max Output','RHV']]
    for i in range(ctr+1):
        r=[]
        print('-'*70)
        for j in range(uvar):
            if j==0:
                    r.append(input(f'Enter row {i+1} name :'))
            if i==ctr:
                a=(eval(input(f'Enter co-efficient of X{j+1} of objective Function :')))*-1
                r.append(a)
                if j==uvar-1:
                    r=r+[1 if k==i else 0 for k in range(ctr+2)]
            else:
                a=eval(input(f'Enter co-efficient of X{j+1} of Constraint {i+1} :'))
                r.append(a)
                if j==uvar-1:
                    s=eval(input(f'Enter co-efficient of Slack variable of Constraint {i+1} :'))
                    r=r+[s if k==i else 0 for k in range(ctr+1)]
                    r.append(eval(input(f'Enter constant value of Constraint {i+1} :')))
        M.append(r)
    return M
#______________________________MAIN________________________________
v=int(input('Enter number of Unknown variables :'))
c=int(input('Enter number of Constraints :'))
m=Tableau_Input(v,c)
print('='*70)
print('Initial Tableau :')
Tableau_Print(m)
print('='*70)
print('Optimal Solution :')
Tableau_Print(Simplex_Method(m))
    
