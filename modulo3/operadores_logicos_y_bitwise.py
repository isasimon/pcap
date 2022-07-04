# Diferencia entre operadores lógicos y bitwise

i = 15
j = 22
# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110


# i y j, al no ser solo ceros, se consideran True
log = bool(i) and bool(j)


bit = i & j
# bit =
# 0000000000000000000000000 0001111
# &
# 0000000000000000000000000 0010110
# =
# 0000000000000000000000000 0000110


neg = ~i

# neg: 1111111111111111111111111111 0000 = -16
