from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))



# Leyendo el archivo
data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    # data = bytearray(bf.read())
    # data = bytearray(bf.read(5))
    bf.close()
    for b in data:
        print(hex(b), '  ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))