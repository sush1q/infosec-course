
def generate_shared_key():
    g1 = 42453345345345
    g2 = g1
    p = 162259276829213363391578010288127

    a_secret = 2344
    a_public = (g1 ** a_secret) % p

    b_secret = 3455
    b_public = (g2 ** b_secret) % p

    a_shared_key = (b_public ** a_secret) % p

    print(a_shared_key)
    b_shared_key = (a_public ** b_secret) % p 
    print(b_shared_key)

    print(len(str(a_shared_key)))
    print(hex(a_shared_key))

    return;

if __name__ == "__main__":
    generate_shared_key()
