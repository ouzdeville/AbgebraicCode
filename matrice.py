from galois_field import *

#Afficher le coefficient d'une matrice

def mat_coeff(A, i, j):
    return A[i][j]


#L'ensemble des coefficients d'une matrice
def mat_set_coeff_to_one(A, n, m):
    for i in range(n):
        for j in range(m):
            print(A[i][j])


#Copier une matrice
def copier(a):
    n=len(a)
    b=[]
    for i in range(n):
        b.append(a[i])
    return b


#Changer le coefficient d'une matrice
def mat_change_coeff(A, i, j):
    n = int(input("Donner l'entier à cette position : "))
    A[i][j] = n
    return A


#Echanger deux lignes
def swaprows(A, i, k):
    l = A[i]
    A[i] = A[k]
    A[k] = l


#Somme de deux vecteurs(lignes)
def somp(p,q):
    n = len(p)
    s=[]
    for i in range(n):
        s.append(p[i]+q[i])
    return s

#Soustraction de deux vecteurs(lignes)
def sousp(p,q):
    n = len(p)
    s=[]
    for i in range(n):
        s.append(p[i]-q[i])
    return s

#Somme de deux matrices
def somm(a,b):
    n=len(a)
    s = []
    for i in range(n):
        s.append(somp(a[i],b[i]))
    return s


#produit de deux vecteurs (pour ligne et colonne)
def prodp(p,q):
    n = len(p)
    s=0
    for i in range(n):
        s = s + p[i]*q[i]
    return s


#Transposé d'une matrice
def transp(a):
    n = len(a)
    m = len(a[0])
    s = []
    r = []
    for i in range(m):
        for j in range(n):
            s.append(a[j][i])
        r.append(s)
        s=[]
    return r


#Produit de deux matrices
def prod(a,b):
    n = len(a)
    s=[]
    r=[]
    t=transp(b)
    for i in range(n):
        for j in range(n):
            s.append(prodp(a[i],t[j]))
        r.append(s)
        s=[]
    return r


#Multiplication d'une ligne(vecteur) par un scalaire
def prodscal(a,p):
    n = len(p)
    s=[]
    for i in range(n):
        s.append(p[i]*a)
    return s


#Rendre nul le coef i d'une ligne en faisant la difference avec une autre
def diffp(a,b,i):
    s=[]
    r=[]
    if b[i]==0:
        return b
    else:
        x = 1/b[i]
        r=prodscal(x,b)
        s = sousp(r,a)
    return s



#Rendre nul les coef i++ des autres lignes en faisant la difference avec la ligne v[i]
def diffmat(a,k):
    n=len(a)
    s=[]
    for i in range(k+1):
        s.append(a[k])
    for i in range(k+1,n):
        s.append(diffp(a[k],a[i],k))
    return s

#Echanger la ligne b[k] (si son premier coef est nul) avec un autre dont le premier coef est non nul 
def echangeline(b,k):
    n = len(b)
    s=[]
    a=copier(b)
    if a[k][k] == 0:
        for i in range(1,n):
            if a[n-i][k]!=0:
                swaprows(a,k,n-i)
                break
    return a



#Multiplication d'une ligne(vecteur) par l'inverse du coef à la position k
def prodcoefdd(p,k):
    n = len(p)
    
    r=[]
    if p[k]!=0:
        s=1/p[k]
        for i in range(n):
            r.append(p[i]*s)
        return r
    else:
        return p



#Elimination de Gauss
def GaussElim(H):
    a = copier(H)
    n=len(a)
    m=len(a[0])
    for i in range(n):
        if a[i][i] == 0:
            a = echangeline(a,i)
        a[i] = prodcoefdd(a[i],i)
        
        for j in range(i+1,n):
            a[j] = prodcoefdd(a[j],i)
            if a[j][i] != 0:
                a[j] = sousp(a[j],a[i])

    for i in range(n-1,0,-1):
        for k in range(i):
            a[k] = sousp(a[k],prodscal(a[k][i],a[i]))
    return a


#Matrice génératrice code cyclique
def mat_gen(p, k):
        n=len(p)
        a=p
        s=[a]
        for i in range(k-1):
            a = [0] + a
            del(a[n])
            s.append(a)
        return s

    

#Fonction theta qui renvoie le carré
def theta(x):
    return x*x

#Fonction theta qui renvoie x puissance p
def thetap(x, p):
    s=1
    for i in range(p):
        s=s*x
    return s

# x.g(x) 
def thev(p):
    s=[]
    n=len(p)
    for i in range(n):
        s.append(theta(p[i]))
    return s

# Matrice generatrice code theta-cyclique
def matg(p, k):
        n=len(p)
        a=p
        s=[a]
        for i in range(k-1):
            a = [0] + thev(a)
            del(a[n])
            s.append(a)
        return s

