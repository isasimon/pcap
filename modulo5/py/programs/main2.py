# import iota  # da un error

from sys import path  # path contiene las rutas donde python busca módulos

path.append('C:\\Users\\User\\PycharmProjects\\pcap\\modulo5\\py\\packages')

print(path)

import extra.ugly.omega

import extra.iota as iota

resI = iota.FunI()
print(resI)

from extra.good.alpha import FunA

resA = FunA()
print(resA)

from extra.good.best.sigma import FunS

resS = FunS()
print(resS)
