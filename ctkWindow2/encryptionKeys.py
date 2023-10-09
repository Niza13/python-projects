# key generating and storing in pem file
# rsa library: asymmetric 

import rsa

# generating new keys and giving a size to it
publicK, privateK = rsa.newkeys(4096)

print(publicK)
print("\n\n\n")
print(privateK)

# storing keys in different files: .pem is extension for that format
# save_pkcs1 is to write and save in pem format
with open("publicK.pem","wb") as f:
    f.write(publicK.save_pkcs1("PEM"))


# sending privateK to a file
with open("privateK.pem","wb") as f:
    f.write(privateK.save_pkcs1("PEM"))


