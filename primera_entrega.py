import random

# Función para calcular el MCD usando el algoritmo de Euclides
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para encontrar el inverso modular usando el algoritmo extendido de Euclides
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Función para generar un número primo grande
def is_prime(n, k=5):  # k es el número de pruebas de Miller-Rabin a realizar
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Generar llaves RSA
def generate_keys(bits):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # e comúnmente elegido
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))

# Encriptar un mensaje
def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Desencriptar un mensaje
def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Ejemplo de uso
bits = 60  # Número de bits para los números primos

public_key, private_key = generate_keys(bits)
print("Clave pública:", public_key)
print("Clave privada:", private_key)

mensaje = "Hola, mundo!"
print("Mensaje original:", mensaje)

mensaje_encriptado = encrypt(mensaje, public_key)
print("Mensaje encriptado:", mensaje_encriptado)

#mensaje_desencriptado = decrypt(mensaje_encriptado, private_key)
#print("Mensaje desencriptado:", mensaje_desencriptado)

import time
import matplotlib.pyplot as plt

# Función para medir el tiempo de generación de llaves
def measure_time(bits):
    start_time = time.time()
    generate_keys(bits)
    end_time = time.time()
    return end_time - start_time

# Medir tiempo de ejecución para cada número de bits de 1 a 60
bit_range = range(10, 61, 10)
times = [measure_time(bits) for bits in bit_range]

# Graficar los resultados
plt.plot(bit_range, times, marker='o')
plt.xlabel('Número de bits')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de generación de llaves RSA en función del número de bits')
plt.grid(True)
plt.show()
