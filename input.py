import aes

plaintext = 'My name is Edmund Longsworth and I am a student in the CS455 class.'

print()
print("This is the plaintext: ", plaintext)

ciphertext = aes.encrypt('my secret key', plaintext)

print()
print("This is the cipher text: ", ciphertext)
print()


print("This is the decrypted cipher text: ", aes.decrypt('my secret key', ciphertext))
