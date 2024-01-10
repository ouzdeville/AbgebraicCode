from galois_field2 import *

"Degré d'un polynome"

def poly_deg(p):
    n = len(p)
    return n-1

"Le coefficient à la position i"

def poly_coeff(p, i):
    return p[i]

"Retourner un polynome avec son degré en supprimant les 0"

def polynome(p):
    n=len(p)
    while p[n-1]==0 and n>1:
        del(p[n-1])
        n=len(p)
    return p

"Une copie du polynome"

def poly_copy(p):
    q=p
    return q

# Passer de 0,n à n,0
def passe(p):
    n=len(p)
    q=[]
    for i in range(n):
        q.append(p[n-1-i])
    return q 

# Entier en polynome

def pole(k):
    a = bin(k)
    x=len(a)
    p=[]
    for i in range(x-2):
        p.append(int(a[i+2]))
    return p

# Polynome en entier avec alpha

def comp(p):
    for i in range(2**m):
        if pole(i)==p:
            return i
        

#Somme de deux polynomes

def poly_somme2(p,q):
    n=len(p)
    m=len(q)
    s=[]
    if n==m:
        for i in range(m):
            s.append((p[i] + q[i])%2)
        return polynome(s)
    elif n>m:
        for i in range(m):
            s.append((p[i] + q[i])%2)
        for i in range(n-m):
            s.append(p[m+i])
        return polynome(s)
    else:
        for i in range(n):
            s.append((p[i] + q[i])%2)
        for i in range(m-n):
            s.append(q[n+i])
        return polynome(s)
    

#Le polynome X^n 

def xn(n):
    p=[]
    for i in range(n):
        p.append(0)
    p.append(1)
    return p


#Produit de deux polynome sur F_{2^m}

def poly_mul2(p,q):

    a=comp(passe(p))
    b=comp(passe(q))
    c=gf_prod(a,b)
    return passe(pole(c))


"Quotient d'une division euclidienne sur F2^m"

def poly_quot2(a,b):
    #polynome(a)
    #polynome(b)
    y=0
    n=poly_deg(a)
    l=poly_deg(b)
    p=[]
    if l==0:
        return a
    else :
        while l<=n:
            q=poly_mul2(xn(n-l), b)
            p=poly_somme2(p,xn(n-l))
            print(p)
            a = poly_somme2(a,q)
            print(a)
            polynome(a)
            n=poly_deg(a)
        return p


"Reste d'une division euclidienne sur F2^m"

def poly_reste2(a,b):
    #polynome(a)
    #polynome(b)
    y=0
    n=poly_deg(a)
    l=poly_deg(b)
    p=[]
    if l==0:
        return a
    else :
        while l<=n:
            q=poly_mul2(xn(n-l), b)
            p=poly_somme2(p,xn(n-l))
            print(p)
            a = poly_somme2(a,q)
            print(a)
            polynome(a)
            n=poly_deg(a)
        return a
    
 
"Quotient et Reste d'une division euclidienne sur F2^m"

def poly_qr2(a,b):
    #polynome(a)
    #polynome(b)
    y=0
    n=poly_deg(a)
    l=poly_deg(b)
    p=[]
    if l==0:
        return a
    else :
        while l<=n:
            q=poly_mul2(xn(n-l), b)
            p=poly_somme2(p,xn(n-l))
            print(p)
            a = poly_somme2(a,q)
            print(a)
            polynome(a)
            n=poly_deg(a)
        return p, a
    

#Calcul du produit de p et q modulo f sur F2^m
def poly_mul_mod2(p,  q, mod):
    a = poly_mul2(p,q)
    b = poly_reste2(a,mod)
    return b


#pgcd de deux polynomes

def poly_gcd(a,b):
    polynome(a)
    polynome(b)
    U0 = [1]
    U1 = [0]
    V0 = [0]
    V1 = [1]
    R0 = a
    R1 = b
    while R1!=[0]:
        Q=poly_quot2(R0,R1)
        R2 = polynome(poly_somme2(R0,poly_mul2(Q,R1)))
        U2 = polynome(poly_somme2(U0,poly_mul2(Q,U1)))
        V2 = polynome(poly_somme2(V0,poly_mul2(Q,V1)))
        
        R0 = R1
        R1 = R2
        U0 = U1
        U1 = U2
        V0 = V1
        V1 = V2
    return R0


#L'évaluation d'un polynome sur Fk

def poly_eval(p,a):
    n=poly_deg(p)
    s = p[n]
    for i in range(n):
        s = (s*a + p[n-i-1])%2
    return s

#Afficher le polynome

def poly_display(p):
    n=poly_deg(p)
    a = str(p[n]) + ".X^n"
    for i in range(n-1):
        a = a + " + " + str(p[n-1-i]) + ".X^" + str(n-1-i)
    a = a + " + " + str(p[0])
    
    return a

