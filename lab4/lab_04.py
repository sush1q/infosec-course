from cryptography.fernet import Fernet
import itertools
import string
import rsa

# Загрузка зашифрованного файла
with open('tmp/enc_data.txt', 'rb') as f:
    encrypted_data = f.read()

# Функция для генерации всех возможных комбинаций
def generate_keys(length):
    chars = string.ascii_letters + string.digits  # Используем буквы и цифры
    for combination in itertools.product(chars, repeat=length):
        yield ''.join(combination).encode()

# Функция для подбора ключа
def brute_force(encrypted_data, max_length=5):
    for length in range(1, max_length + 1):
        print("first cycle")
        true_key = """-----BEGIN RSA PRIVATE KEY-----
MIIBPgIBAAJBAIJw53XH07tMUobAy6hO8A2S+U5V/pcQbRmdHsWKN1FqgFD4EXJr
dhZjzlgIt02UX/ie2MJS/G7CfRjvYKeDLbcCAwEAAQJAJ7w1BhAFU70ANsRsRa0m
OzxWbaKMl4ANfAv837gmupfKzq5FHjfQ+b4/lgok6gnWL6oGeKapvP2QlbrJIDJJ
IQIjAM910aG6NP3RRrxKvKsjbgNZIPgCnDVyFlbduzu01Y6uC50CHwCg9ePlB+Nd
u4AlhIe/N+eg01C/1f3y16wmZm+gcGMCIwC51u3htR8RG24E7+IQYB2FjErXP+dU
jQ1r5RZ7BqOjO0+VAh8Aj/PZYVfwrD+ol+UzUny5F0hmC2titvDT8XPjmWVpAiMA
nG24GvoEVWRCICJ4f91Ou5gbqatXxJaFLv4vKGV1HLEc4w==
-----END RSA PRIVATE KEY-----"""
        for key in generate_keys(length):
            try:
                # cipher = Fernet(key)
                # decrypted_data = cipher.decrypt(encrypted_data)
                key_rsa = rsa.PrivateKey.load_pkcs1(true_key)
                decrypted_data = rsa.decrypt(encrypted_data, key_rsa)

                print(f"Ключ найден: {true_key.decode()}")
                print(f"Расшифрованные данные: {decrypted_data.decode()}")
                return
            except Exception as e:
                print(e)
                continue
    print("Ключ не найден.")

# Запуск Brute Force атаки
brute_force(encrypted_data)