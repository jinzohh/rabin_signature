#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Program that calculates square roots of a mod p where p is an odd prime.

import math

def euc(a, b):
    # This function calculates the GCD using recursion method.
    # Find the modulus of a and b.
    r = a % b
    
    # If remainder does not equal 0, call the euc() function again. If remainder equals 0, return b which is the GCD.
    if r != 0:
        result = euc(b, r)
    else:
        result = b

    return result

def crt_solve(congruences):
    # Initialize variables. Collect all modulus values.
    m_val = [congruences[i][1] for i in range(len(congruences))]
    pair_set = []
    gcd_val = set()

    # Collect all modulus pairs and run Euclidean algorithm to check whether they are all relatively prime.
    for i in range(len(m_val)):
        for j in range(len(m_val)):
            if j != i:
                pair = sorted([m_val[i], m_val[j]])
                if pair not in pair_set:
                    pair_set.append(pair)
                else:
                    pass
            else:
                continue

    for pair in pair_set:
        gcd = euc(pair[0], pair[1])
        gcd_val.add(gcd)

    # Check that there is only one value of 1 in gcd_val. Flag it as True, if so. If not, flag it as False.
    if len(gcd_val) == 1 and 1 in gcd_val:
        r_prime = True
    else:
        r_prime = False

    # If gcd value calculated above is 1, this means that the modulus values are relatively prime. If not, return None.
    if r_prime == True:
        # Formula: x ≡ ri mod mi
        # Collect all the ri values.
        rmy_set = []
        ri = [congruences[i][0] for i in range(len(congruences))]

        # Run a loop to calculate Mi, yi(modular inverse of Mi), and the product of ri, Mi, and yi.
        # Get the sum of all riMiyi mod M.
        for i in range(len(ri)):
            Mi = math.prod(m_val) // m_val[i]
            yi = pow(Mi, -1, m_val[i])
            rmy = ri[i] * Mi * yi
            rmy_set.append(rmy)
        
        result = (sum(rmy_set) % math.prod(m_val), math.prod(m_val))
        
    else:
        result = None
    
    return result

def zn(num):
    # This function calculates all values mod num relatively prime to num.
    result = []

    for i in range(1, num+1):
        gcd = euc(num, i)
        if gcd == 1:
            result.append(i)
        else:
            continue

    return result

def square_roots_mod_p(a, p):
    # Make sure a and p are relatively prime.
    if euc(a, p) == 1:
        # Simplify a mod p.
        while a != a % p:
            a = a % p

        if len(str(p)) <= 6:
            # Finding Zn which are integers mod p relatively prime to p.
            Zn = zn(p)
    
            # Check if there is a square root by finding the quadratic residues mod p.
            for i in Zn:
                x = pow(i, 2, p)
                if x == a:
                    quad_residue = True
                    break
                else:
                    quad_residue = False
                    continue
        
        else:
            quad_residue = True
        
        # If a quadratice residue mod p exists, proceed to calculating square roots of a mod p. If not, return empty list.
        if quad_residue:
            # Because we know that a mod p is a square, check Hoffstein's Proposition to see if we can run the formula for faster calculation.
            hoffstein_check = (p+1) % 4 == 0
            
            if hoffstein_check:
                # Find b using Hoffsetin's Proposition.
                exp_comp = (p + 1) // 4
                b = pow(a, exp_comp, p)
                sq_roots = [b, -1*b+p]
            elif hoffstein_check == False and len(str(p)) <= 6:
                # Since Hoffstein's Proposition check is False, perform brute force method on all quadratice residues mod p.
                # Initialize list variable.
                sq_roots = []
                # Find square roots for all values Zn and collect the roots that equal value of a.
                for i in Zn:
                    x = pow(i, 2, p)
                    if x == a:
                        sq_roots.append(i)
                    else:
                        continue
            else:
                sq_roots = None
                print("\np value may be too long to calculate.")
        else:
            sq_roots = None
    else:
        sq_roots = None
    
    return sq_roots

def square_roots_mod_pq(a, p, q):
    # Find the square roots of a mod p and a mod q separately.
    Y = square_roots_mod_p(a, p)
    Z = square_roots_mod_p(a, q)

    if Y is not None and Z is not None:
        # Use CRT to find the square roots of a mod pq.
        sq_roots = []
        for i in range(len(Y)):
            for j in range(len(Z)):
                sq_root = crt_solve([(Y[i], p), (Z[j], q)])
                sq_roots.append(sq_root[0])
    else:
        sq_roots = None

    return sq_roots

def main():
    # This is the main function.
    try:
        print(
'''
1. Square roots with modulus p
2. Square roots with modulus p*q
'''
        )
        
        choice = int(input("Choose from options above (1 or 2): "))
        print()
        
        if choice == 1:
            modulus = int(input("Enter the modulus value p: "))
            print()
            a_val = int(input("Enter the 'a' value: "))
        
            sq_r = square_roots_mod_p(a_val, modulus)
            print("\nSquare roots are:", sq_r)
        
        elif choice == 2:
            modulus_p = int(input("Enter the modulus value p: "))
            modulus_q = int(input("Enter the modulus value q: "))
            a_val = int(input("Enter the 'a' value: "))

            sq_r_pq = square_roots_mod_pq(a_val, modulus_p, modulus_q)
            print("\nSquare roots are:", sq_r_pq)

        else:
            raise ValueError
            
    except ValueError:
        print("\nInvalid input. Please try again. All input values must be integers.\n")

if __name__ == "__main__":
    main()


# In[ ]:




