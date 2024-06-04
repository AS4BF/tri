import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_passwords(N, K):
    passwords = set()
    while len(passwords) < N:
        passwords.add(generate_password(K))
    return list(passwords)

def main():
    N = int(input("Введите количество паролей: "))
    K = int(input("Введите длину пароля: "))

    unique_passwords = generate_unique_passwords(N, K)
    
    print(f"\nСгенерированные пароли длиной {K} символов:")
    for password in unique_passwords:
        print(password)

if __name__ == "__main__":
    main()
