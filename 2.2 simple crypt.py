import simplecrypt


with open(r"C:\1\encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open(r"C:\1\passwords.txt", "r") as pwd:
    for p in pwd:
        try:
            print(simplecrypt.decrypt(p.strip('\n'), encrypted).decode('utf8'))
        except simplecrypt.DecryptionException:
            print("DecrException")

