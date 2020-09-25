# Alice and Bob will be running Diffie-Hellman and has agreed on the group (Z/241Z)* with generator g=7.

# 1) If Alice picks the secret a=237 and Bob picks the secret b=9, what will the secret be?

# 2) In the same group, with the same generator, Alberte and Benjamin runs Diffie-Hellman.
#If the adversary observes the messages A=26 (from Alberte to Benjamin) and B=85(from Benjamin to Alberte), what is the shared secret s?

# 3) If the adversary observes instead the messages A=44 and B=201, what is the shared secret s?

p = 241
g = 7 # generator of Z_p*

a = 237 # Alice's secret
b = 9 # Bob's secret

# 1)

A = g**a % p # Alice sends to Bob A
B = g**b % p # Bob sends to Alice B
print("Alice sends to Bob ", A)
print("Bob sends to Alice", B)

s_Alice = B**a % p # Alice computes the secret
s_Bob = A**b % p # Bob computes the secret
assert(s_Alice == s_Bob)

print("Alice computes the secret ", s_Alice)
print("Bob computes the secret ", s_Bob)

# 2)

A = 26
B = 85

def brute_force_secret(A, B):
    for i in range(1, p):
        if g**i % p == A:
            print("Alberte secret bruteforced!")
            a = i
        if g**i % p == B:
            print("Benjamine secret bruteforced!")
            b = i

    print("Alberte secret was ", a)
    print("Benjamine secret was ", b)

    assert(A**b % p == B**a % p)
    s = A**b % p

    print("The adversary computes the secret ", s)

brute_force_secret(A,B)

# 3)

A = 44
B = 201

brute_force_secret(A,B)
