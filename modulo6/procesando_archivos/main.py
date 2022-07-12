"""
Se recomienda no editar los archivos con procesadores de texto avanzados como
MS Word o LibreOffice sino más bien con gedit, vim, etc para evitar que contenga
algo más que texto oculto.

Para abrir archivos que puedan contener más caracteres que el código ASCII hay
que especificar un encoding
"""
from os import strerror


def read_txt(file):
    stream = open(file, "rt", encoding="utf-8")
    print(stream.read())


def read_each_character(file):
    try:
        cnt = 0
        s = open(file, "rt")
        ch = s.read(1)
        while ch != '':
            print(ch, end='')
            cnt += 1
            ch = s.read(1)
        s.close()
        print("\n\nCaracteres en el archivo: ", cnt)
    except IOError as e:
        # metodo strerror pinta un mensaje específico de cada errno
        print("Se produjo un error de E/S: ", strerror(e.errno))


def read_each_line(file):
    try:
        ccnt = lcnt = 0
        s = open('text.txt', 'rt')
        line = s.readline()
        while line != '':
            lcnt += 1
            for ch in line:
                print(ch, end='') # devuelve cadena vacía cuando no hay más líneas
                ccnt += 1
            line = s.readline() # readline puede tomar un argumento con el número de líneas que imprime
        s.close()
        print("\n\nCaracteres en el archivo: ", ccnt)
        print("Lineas en el archivo:     ", lcnt)
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def open_file_as_iterable(file):
    """
    Al abrir un fichero se obtiene un objeto iterable
    donde cada línea apunta a un __next__ como una linked list
    """
    try:
        ccnt = lcnt = 0
        for line in open(file, 'rt'):
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        print("\n\nCaracteres en el archivo: ", ccnt)
        print("Lineas en el archivo:     ", lcnt)
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def write_something(file):
    try:
        fo = open(file, 'wt')  # un nuevo archivo (newtext.txt) es creado
        for i in range(10):
            fo.write("línea #" + str(i + 1) + "\n")
        fo.close()
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


if __name__ == '__main__':
    def I(n):
        s = ''
        for i in range(n):
            s += '*'
            yield s

    for x in I(3):
        print(x, end='')