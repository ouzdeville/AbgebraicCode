primes=[
    1,		#/* extension degree 0 (!) never used */
    3,		#/* extension degree 1 (!) never used */
    7, 		#/* extension degree 2 */
    13, 	#	/* extension degree 3 */
    23, 	#	/* extension degree 4 */
    45, 	#	/* extension degree 5 */
    103, 	#	/* extension degree 6 */
    203, 	#	/* extension degree 7 */
    435, 	#	/* extension degree 8 */
    1041, 	#	/* extension degree 9 */
    2011,	#	/* extension degree 10 */
    4005,	#	/* extension degree 11 */
    10123,	#	/* extension degree 12 */
    20033,	#	/* extension degree 13 */
    42103,	#	/* extension degree 14   */
    100003,	#	/* extension degree 15 */
    210013	#	/* extension degree 16 */
]

m=3
prime=primes[m];

# Produit de deux polynomes
def gf_prod(a,b):
    c=a;
    s=0
    if b==0 or a==0:
        return 0
    s=a if (b&(1)) else 0
    for i in range(1,m):
        bit_i=b&(1<<i)
        c=c<<1
        c=c^prime if c&(1<<m) else c
        if(bit_i):
            # s+(a<<i)
            s=s^c
    return s


# au carré
def gf_square(x):
    return gf_prod(x,x)


# à la puissance i
def gf_pow(x, i):
        a=1
        for j in range(i):
                a = gf_prod(a,x)
        return a


# Racine carré
def gf_sqrt(x):
    a = gf_pow(x, 2**{m-1})
    return a


# inverse

def gf_inv(x):
    return gf_pow(x, 2**{m}-2)


# Division
def gf_div(x, y):
    return gf_prod(x, gf_inv(y))