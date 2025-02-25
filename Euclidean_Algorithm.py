def extended_euclidean(a, b):
    """Returns a tuple (GCD, x, y) such that GCD = a * x + b * y."""
    if b == 0:
        return a, 1, 0  # Base case: GCD(a, 0) = a, with x=1 and y=0
    else:
        GCD, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return GCD, x, y

def modular_inverse(a, m):
    """Returns the modular inverse of a under modulo m."""
    GCD, x, _ = extended_euclidean(a, m)
    if GCD != 1:
        raise ValueError(f"{a} has no modular inverse under modulo {m}")
    return x % m

def main():
    # User inputs
    print("Welcome to the Extended Euclidean Algorithm!")
    
    # Get values for a and m from user
    a = int(input("Enter the value of 'a': "))
    m = int(input("Enter the value of 'm': "))
    
    # Find GCD and coefficients
    GCD, x, y = extended_euclidean(a, m)
    print(f"\nGCD of {a} and {m}: {GCD}")
    print(f"Coefficients x and y: x = {x}, y = {y}")
    
    # Find modular inverse
    if GCD == 1:
        mod_inv = modular_inverse(a, m)
        print(f"\nModular Inverse of {a} modulo {m}: {mod_inv}")
    else:
        print(f"\nSince GCD is not 1, {a} has no modular inverse under modulo {m}.")

if __name__ == "__main__":
    main()
