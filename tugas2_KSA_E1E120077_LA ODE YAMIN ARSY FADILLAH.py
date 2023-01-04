key_ascii = []
S = []
J = []
j = 0

key = input('Masukan key : ')

for char in key:
    ascii = ord(char)
    key_ascii.append(ascii)

for i in range(256):
    S.append(i)

for i in range(len(key_ascii)):
    j = (j + S[i] + key_ascii[i % len(key_ascii)]) % 256
    S[i],S[j] = S[j], S[i]
print(S)

