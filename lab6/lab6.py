from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os

fname ="/tmp/hash"

# Генеруємо новий ключ
key = RSA.generate(1024, os.urandom)
# Отримуємо хеш файлу
h = SHA256.new()
with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)

# Підписуємо хеш
signature = pkcs1_15.new(key).sign(h)

# Отримуємо відкричий ключ з закритого
pubkey = key.publickey()

# Пересилаємо користувачу файл, публічний ключ та підпис
# На боці користувача обраховуємо хеш файлу та перевіряємо підпис
pkcs1_15.new(pubkey).verify(h, signature)

# Не правильний хеш не має пройти перевірку
pkcs1_15.new(pubkey).verify(SHA256.new(b'test'), signature)
raise ValueError("Invalid signature")
