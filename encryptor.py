import rsa
import rsa.pkcs1

class Encryptor:
    private_key = None
    public_key = None

    def __init__(self, public_key=None, private_key=None):
        if (public_key == None or private_key == None):
            (self.public_key, self.private_key) = rsa.newkeys(512)
        else:
            self.public_key = rsa.PublicKey.load_pkcs1(public_key)
            self.private_key = rsa.PrivateKey.load_pkcs1(private_key)

    def encrypt(self, data):
        encrypted_message = rsa.encrypt(data, self.public_key)
        return encrypted_message
    
    def decrypt(self, data):
        decrypted_message = rsa.decrypt(data, self.private_key)
        return decrypted_message

    def sign_data(self, data):
        enc_data = enc.encrypt(data)
        print(f"""Сохрани себе: \
                Ключевая пара: 
                    Публичный ключ: {self.public_key.save_pkcs1()}
                    Приватный ключ: {self.private_key.save_pkcs1()}
                Зашифрованные данные: {enc_data.hex()}""")
        return enc_data
    
    def get_public_key(self):
        return self.public_key
    
    def get_private_key(self):
        return self.private_key

class DataManager:

    def get_data(self, file):
        with open(file, mode='rb') as rfile:
            return rfile.read()

    def store_data(self, file, data):
        with open(file, mode='wb') as wfile:
            wfile.write(data)

enc = Encryptor()
data = "Hello world!"

enc_data = enc.sign_data(data.encode())

dm = DataManager()
dm.store_data("tmp/private.pem", enc.get_private_key().save_pkcs1())
dm.store_data("tmp/public.pem", enc.get_public_key().save_pkcs1())
dm.store_data("tmp/enc_data.txt", enc_data)

priv = dm.get_data("tmp/private.pem")
pub = dm.get_data("tmp/public.pem")
data1 = dm.get_data("tmp/enc_data.txt")

enc1 = Encryptor(pub, priv)
dec_data = enc.decrypt(data1)
print(dec_data)

