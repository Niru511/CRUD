from django.db import models

# Create your models here.
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from django.db import models

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

class Data(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=256)

def encrypt_number(number):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted = cipher.encrypt(number.encode())
    return encrypted.hex()

def save(self, *args, **kwargs):
    encrypted_number = encrypt_number(self.number)
    self.number = encrypted_number
    super(Data, self).save(*args, **kwargs)

def decrypt_number(encrypted):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted = cipher.decrypt(bytes.fromhex(encrypted))
    return decrypted.decode()

def __str__(self):
    return f"{self.name}: {decrypt_number(self.number)}"

