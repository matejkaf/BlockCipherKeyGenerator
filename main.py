import os

#
# generate key & IV
#
key = os.urandom(32) # 256 Bit key
iv = os.urandom(16)  # 128 bit initialization vector
print(key)
print(iv)

#
# write to binary file
#
f = open('key.bin', 'wb') # write / binary mode
data = key + iv
f.write(data)
f.close()

#
# read from binary file
#
print('*** READ ***')
f = open('key.bin','rb')
data_read = f.read()
f.close()
print(data_read)
key_read = data_read[:32]
iv_read = data_read[32:]
print(key_read)
print(iv_read)
