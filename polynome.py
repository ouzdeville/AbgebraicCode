from galois_field import *

#Degré d'un polynome

def poly_deg(p):
    n = len(p)
    return n-1

#Le coefficient à la position i

def poly_coeff(p, i):
    return p[i]

#Le coefficient dominant

def poly_tete(p):
    """Return the leading terme of the polynomial."""
    return p[len(p)-1]


#Retourner un polynome avec son degré en supprimant les 0

def polynome(p):
    n=len(p)
    while p[n-1]==0 and n>1:
        del(p[n-1])
        n=len(p)
    return p


#Retourner le polynome modulo q
def polynomeq(p,q):
    n=len(p)
    s=[]
    for i in range(n):
        s.append(p[i]%q)
    return polynome(s)


#Une copie du polynome

def poly_copy(p):
    q=p
    return q


#L'inverve d'un élément dans Fq

def inverseq(k,q):
    for i in range(q):
        if (k*i)%q==1:
            return i
        

#Multiplier un coefficient par un polynome

def mcp(a,p):
    q=[]
    n=len(p)
    for i in range(n):
        q.append(a*p[i])
    return polynome(q)


#Multiplier un coefficient par un polynome sur Fq

def mcq(a,p,q):
    f=[]
    n=len(p)
    for i in range(n):
        f.append((a*p[i])%q)
    return polynome(f)



#Multiplier par l'inverve du coefficient dominant

def mip(p):
    polynome(p)
    n=poly_deg(p)
    s=1/p[n]
    q = mcp(s,p)
    return q


#Multiplier par l'inverve du coefficient dominant sur Fq

def miq(p,q):
    polynome(p)
    n=poly_deg(p)
    s=inverseq(p[n],q)
    k = mcq(s,p,q)
    return k



#Somme de deux polynomes

def poly_somme(p,q):
    n=len(p)
    m=len(q)
    s=[]
    if n==m:
        for i in range(m):
            s.append(p[i] + q[i])
        return polynome(s)
    elif n>m:
        for i in range(m):
            s.append(p[i] + q[i])
        for i in range(n-m):
            s.append(p[m+i])
        return polynome(s)
    else:
        for i in range(n):
            s.append(p[i] + q[i])
        for i in range(m-n):
            s.append(q[n+i])
        return polynome(s)
    


#Somme de deux polynomes sur Fk

def poly_sommeq(p,q,k):
    n=len(p)
    m=len(q)
    s=[]
    if n==m:
        for i in range(m):
            s.append((p[i] + q[i])%k)
        return polynome(s)
    elif n>m:
        for i in range(m):
            s.append((p[i] + q[i])%k)
        for i in range(n-m):
            s.append(p[m+i])
        return polynome(s)
    else:
        for i in range(n):
            s.append((p[i] + q[i])%k)
        for i in range(m-n):
            s.append(q[n+i])
        return polynome(s)
    


# Différence de deux polynomes

def poly_diff(p,q):
    return poly_somme(p,mcp(-1,q))


# Différence de deux polynomes sur Fk

def poly_diffq(p,q,k):
    return poly_sommeq(p,mcp(-1,q,k),k)


#Le polynome X^n 

def x(n):
    p=[]
    for i in range(n):
        p.append(0)
    p.append(1)
    return p

#Le polynome X^n 

def xn(n):
    p=[]
    for i in range(n):
        p.append(0)
    p.append(1)
    return p


#Produit de deux polynymes

def poly_mul(p,q):
    n = len(p)
    m = len(q)
    s=0
    r=[]
    for i in range(n+m-1):
        for j in range(n):
            for k in range(m):
                if j+k == i:
                    s = s + p[j]*q[k]
        r.append(s)
        s=0
    return r


#Produit de deux polynymes sur Fk

def poly_mulq(p,q,k):
    n = len(p)
    m = len(q)
    s=0
    r=[]
    for i in range(n+m-1):
        for j in range(n):
            for l in range(m):
                if j+l == i:
                    s = (s + p[j]*q[l])%k
        r.append(s)
        s=0
    return r


# Quotient d'une division euclidienne

def poly_quot(a,b):
    polynome(a)
    polynome(b)
    y=0
    n=poly_deg(a)
    m=poly_deg(b)
    p=[]
    if m==0:
        return mcp(1/b[0],a)
    else :
        while m<=n:
            q=poly_mul(x(n-m),mcp(a[n],mip(b)))
            o=mcp(a[n],x(n-m))
            z=mcp(1/b[m],o)
            p=poly_somme(p,z)
            a = poly_diff(a,q)
            polynome(a)
            n=poly_deg(a)
        return p
    

# Quotient d'une division euclidienne sur Fq

def poly_quotq(a,b,q):
    a=polynomeq(a,q)
    b=polynomeq(b,q)
    y=0
    n=poly_deg(a)
    m=poly_deg(b)
    p=[]
    if m==0:
        return mcq(inverseq(b[0]),a,q)
    else :
        while m<=n:
            k=poly_mulq(xn(n-m),mcq(a[n],miq(b,q),q),q)
            o=mcq(a[n],xn(n-m),q)
            z=mcq(inverseq(b[m],q),o,q)
            p=poly_sommeq(p,z,q)
            a = poly_diffq(a,k,q)
            polynome(a)
            n=poly_deg(a)
        return p
    


# Reste d'une division euclidienne

def poly_reste(a,b):
    polynome(a)
    polynome(b)
    y=0
    n=poly_deg(a)
    m=poly_deg(b)
    p=[]
    if m==0:
        return [0]
    else:
        while m<=n:
            q=poly_mul(x(n-m),mcp(a[n],mip(b)))
            a = poly_diff(a,q)
            polynome(a)
            n=poly_deg(a)
        return a
    

#Reste d'une division euclidienne sur Fq

def poly_resteq(a,b,q):
    a=polynomeq(a,q)
    b=polynomeq(b,q)
    y=0
    n=poly_deg(a)
    m=poly_deg(b)
    p=[]
    if m==0:
        return [0]
    else :
        while m<=n:
            k=poly_mulq(xn(n-m),mcq(a[n],miq(b,q),q),q)
            a = poly_diffq(a,k,q)
            #polynome(a)
            n=poly_deg(a)
        return a 


# Quotient et reste d'une division euclidienne

def qre(a,b):
    polynome(a)
    polynome(b)
    y=0
    n=poly_deg(a)
    m=poly_deg(b)
    p=[]
    if m==0:
        return mcp(1/b[0],a), [0]
    else :
        while m<=n:
            q=poly_mul(x(n-m),mcp(a[n],mip(b)))
            o=mcp(a[n],x(n-m))
            z=mcp(1/b[m],o)
            p=poly_somme(p,z)
            a = poly_diff(a,q)
            polynome(a)
            n=poly_deg(a)
        return p,a


def poly_mul_mod(p,  q, mod):
    a = poly_mul(p,q)
    b = poly_reste(a,mod)
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
        Q=poly_quot(R0,R1)
        R2 = polynome(poly_diff(R0,poly_mul(Q,R1)))
        U2 = polynome(poly_diff(U0,poly_mul(Q,U1)))
        V2 = polynome(poly_diff(V0,poly_mul(Q,V1)))
        
        R0 = R1
        R1 = R2
        U0 = U1
        U1 = U2
        V0 = V1
        V1 = V2
    return R0


#L'évaluation d'un polynome

def poly_eval(p,a):
    n=poly_deg(p)
    s = p[n]
    for i in range(n):
        s = s*a + p[n-i-1]
    return s


#Afficher le polynome

def poly_display(p):
    n=poly_deg(p)
    a = str(p[n]) + ".X^n"
    for i in range(n-1):
        a = a + " + " + str(p[n-1-i]) + ".X^" + str(n-1-i)
    a = a + " + " + str(p[0])
    
    return a