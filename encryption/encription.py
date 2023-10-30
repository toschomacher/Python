from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


if __name__ == "__main__":
    p = int(input("Enter p = "))
    q = int(input("Enter q = "))
    N = p*q
    phiN = (p-1)*(q-1)

    # e*d%phiN==1
    # d=(e**-1)%phiN
    # The encryption (exponent) key (public key) e (e must satisfy two conditions):
    #   a number in between 1 and phi(N)
    #   a co-prime with N and phi(N)
    # The decryption key (private key) d:
    #   d must satisfy this condition (d*e)%phi(N) = 1
    #   d will always be within the 1-phiN ring of integers
    # Encryption - (M**e)%N
    #   ord('T')    returns ASCII value of 84  then (84**e)%N gives us the encrypted value of T
    # Decryption - (C**d)%N
    #   cypher text 7 (7**d)%N gives us the ASCII value of the encrypted character
    
    print("Co-prime numbers check\n==================")
    print('The numbers', p, 'and', q, 'are', f"{'co-primes' if coprime2(p, q) else 'NOT co-primes'}\n")
    for i in range(1, phiN):
        if coprime2(i, phiN):
            print(i)
    flag = input("Would you like to calculate d (y or n)?")
    if flag =="y":
        e = int(input("Enter e = "))
        for d in range(1, phiN):
            if (e * d) % phiN == 1:
                print('d=', d)
