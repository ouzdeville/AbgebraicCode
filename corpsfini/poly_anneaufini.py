from poly_corps import*

m=6
p=11
f=poly_diffq(xn(m),xn(1),11)

# Détermination des solutions v_i
def solution(p,m):
    S = []
    for i in range(p):
        if (i**m - i)%p == 0:
            S.append(i)
    return S


# On pose f_i = v - v_i pour chaque solution

def factf(p,m):
    S = solution(p,m)
    #a=len(S)
    F=[]
    for i in range(m):
        F.append(poly_diffq(xn(1),[S[i]], p))
    return F
    
# On pose g_i = f/f_i
def factg(p,m,f):
    F = factf(p,m)
    #a=len(F)
    G=[]
    for i in range(m):
        G.append(poly_quotq(f,F[i],p))
    return G


# Détermination des a_i et b_i tels que a_i.f_i + b_i.g_i = 1

def ab(p,m,f):
    F = factf(p,m)
    G = factg(p,m,f)
    A=[]
    B=[]
    for i in range(m):
        r,v,u = poly_gcdq(G[i], F[i], p)
        A.append(mcq(inverseq(poly_tete(r),p),u,p))
        B.append(mcq(inverseq(poly_tete(r),p),v,p))
    return A,B

# Mis en place des idempotemps e_i = b_i.g_i

def idempotent(p,m,f):
    E=[]
    F = factf(p,m)
    G = factg(p,m,f)
    A,B = ab(p,m,f)
    for i in range(m):
        E.append(poly_mul_modq(B[i], G[i], f, p))
    return E

A,B = ab(p,m,f)
F = factf(p,m)
G = factg(p,m,f)
dd= poly_sommeq(poly_mul_modq(A[1],F[1],f,p),poly_mul_modq(B[1],G[1],f,p),p)
ee = idempotent(p,m,f)
print(ee)
print(poly_mul_modq([10,8,6,4,7],[0, 3, 1, 4, 5, 9],f,p))
print(solution(p,m))